import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Iterable, TypeVar

from .bible_book_enums import BibleBookEnum
from .language_enums import BibleLanguageEnum
from .languages import BOOK_ABBREVIATIONS_BY_LANGUAGE, BOOK_NAMES_BY_LANGUAGE

ReferenceT = TypeVar("ReferenceT", bound="BaseReference")


class ParseVerseRefError(ValueError):
    """Raised when a verse reference string cannot be parsed."""

    def __init__(
        self,
        *,
        code: str = "invalid_reference",
        details: str | None = None,
    ) -> None:
        self.code = code
        self.details = details
        super().__init__("invalid verse reference")

    def __str__(self) -> str:
        return "invalid verse reference"

    def to_dict(self) -> Dict[str, str]:
        """Return machine-readable diagnostics for callers."""
        data = {"code": self.code}
        if self.details is not None:
            data["details"] = self.details
        return data


_VERSE_REF_PATTERN = re.compile(
    r"^\s*(?P<book>.+?)\s+(?P<chapter>\d+)\s*[:.]\s*(?P<verse>\d+)\s*$"
)

_VERSE_RANGE_REF_PATTERN = re.compile(
    r"^\s*(?P<start_book>.+?)\s+(?P<start_chapter>\d+)\s*[:.]\s*(?P<start_verse>\d+)\s*"
    r"[-\u2013\u2014]\s*(?:(?P<end_book>.+?)\s+)?(?:(?P<end_chapter>\d+)\s*[:.]\s*)?"
    r"(?P<end_verse>\d+)\s*$"
)


class _BookTermLookup:
    """Resolve localized book names/abbreviations into ``BibleBookEnum`` values.

    Attributes:
        _english (dict[str, BibleBookEnum]): English-only terms.
        _all_languages (dict[str, BibleBookEnum]): Terms merged across languages.
        _by_language (dict[str, dict[str, BibleBookEnum]]): Terms by language code.
    """

    AUTO_LANGUAGE_PRECEDENCE: tuple[str, ...] = (
        BibleLanguageEnum.ARABIC.code,
        BibleLanguageEnum.CHINESE.code,
        BibleLanguageEnum.FRENCH.code,
        BibleLanguageEnum.GERMAN.code,
        BibleLanguageEnum.HEBREW.code,
        BibleLanguageEnum.HINDI.code,
        BibleLanguageEnum.INDONESIAN.code,
        BibleLanguageEnum.KOREAN.code,
        BibleLanguageEnum.PORTUGUESE.code,
        BibleLanguageEnum.RUSSIAN.code,
        BibleLanguageEnum.SPANISH.code,
        BibleLanguageEnum.TAGALOG.code,
    )

    def __init__(
        self,
        names_by_language: Dict[str, Dict[BibleBookEnum, Iterable[str]]],
        abbreviations_by_language: Dict[str, Dict[BibleBookEnum, Iterable[str]]],
    ) -> None:
        """Build lookup tables for English-only, per-language, and auto-detect parsing.

        Args:
            names_by_language: Canonical names keyed by language and book.
            abbreviations_by_language: Abbreviations keyed by language and book.
        """

        self._english = self._build_english_lookup()
        self._all_languages: Dict[str, BibleBookEnum] = dict(self._english)
        self._auto_collisions: Dict[str, set[BibleBookEnum]] = {}

        self._register_terms_by_language(
            self._all_languages,
            names_by_language,
            prefer_existing=True,
            collisions=self._auto_collisions,
        )
        self._register_terms_by_language(
            self._all_languages,
            abbreviations_by_language,
            prefer_existing=True,
            collisions=self._auto_collisions,
        )

        self._by_language: Dict[str, Dict[str, BibleBookEnum]] = {}
        language_codes = tuple(
            code
            for code in self.AUTO_LANGUAGE_PRECEDENCE
            if code in names_by_language or code in abbreviations_by_language
        )
        unordered_codes = tuple(
            code
            for code in (set(names_by_language) | set(abbreviations_by_language))
            if code not in language_codes
        )

        for code in (*language_codes, *unordered_codes):
            table: Dict[str, BibleBookEnum] = {}
            names = names_by_language.get(code)
            if names is not None:
                self._register_terms(table, names)
            abbreviations = abbreviations_by_language.get(code)
            if abbreviations is not None:
                self._register_terms(table, abbreviations)
            self._by_language[code] = table

        self._by_language[BibleLanguageEnum.ENGLISH.code] = dict(self._english)

    @property
    def auto_collisions(self) -> Dict[str, tuple[BibleBookEnum, ...]]:
        """Return ambiguous AUTO-mode terms mapped to all colliding books."""
        return {
            term: tuple(sorted(books, key=lambda book: book.name))
            for term, books in self._auto_collisions.items()
        }

    @staticmethod
    def normalize_language(
        language: BibleLanguageEnum | str | None,
    ) -> BibleLanguageEnum:
        """Normalize ``language`` into a ``BibleLanguageEnum`` value.

        Args:
            language: Language enum, language code string, or ``None``.

        Returns:
            BibleLanguageEnum: Normalized language enum.

        Raises:
            ValueError: If ``language`` is not a supported type/value.
        """
        if language is None:
            return BibleLanguageEnum.AUTO
        if isinstance(language, BibleLanguageEnum):
            return language
        if isinstance(language, str):
            return BibleLanguageEnum.from_str(language)
        raise ValueError("language must be a BibleLanguageEnum, string, or None")

    def parse_book_name(self, book_text: str, language: BibleLanguageEnum) -> BibleBookEnum:
        """Parse a raw book token using the selected language strategy.

        Args:
            book_text: Input book token from the user string.
            language: Language strategy used for lookup.

        Returns:
            BibleBookEnum: Parsed book enum.

        Raises:
            ParseVerseRefError: If parsing fails.
        """
        normalized = " ".join(book_text.split()).casefold()
        if not normalized:
            raise ParseVerseRefError(
                code="empty_book_token",
                details="book token is empty after normalization",
            )

        compact = normalized.replace(".", "").replace(" ", "")
        lookup: Dict[str, BibleBookEnum] | None

        if language == BibleLanguageEnum.AUTO:
            english_match = self._lookup_term(self._english, normalized)

            if english_match is not None:
                return english_match

            lookup = self._all_languages
        else:
            lookup = self._by_language.get(language.code)

        if lookup is None:
            raise ParseVerseRefError(
                code="unsupported_language",
                details=f"unsupported language code: {language.code}",
            )

        matched = self._lookup_term(lookup, normalized)
        if matched is not None:
            return matched

        if language == BibleLanguageEnum.AUTO:
            try:
                return BibleBookEnum.from_str(compact)
            except ValueError as e:
                raise ParseVerseRefError(
                    code="unknown_book",
                    details=f"book token {book_text!r} did not match known books",
                ) from e

        raise ParseVerseRefError(
            code="unknown_book",
            details=f"book token {book_text!r} is unknown for language {language.code}",
        )

    @staticmethod
    def _build_english_lookup() -> Dict[str, BibleBookEnum]:
        """Build a lookup table containing canonical and short English book names.

        Returns:
            dict[str, BibleBookEnum]: Case-folded English lookup table.
        """
        lookup = {book.full_name.casefold(): book for book in BibleBookEnum}
        for book in BibleBookEnum:
            lookup[book.as_str().casefold()] = book
        return lookup

    @staticmethod
    def _register_terms(
        table: Dict[str, BibleBookEnum],
        source: Dict[BibleBookEnum, Iterable[str]],
        *,
        prefer_existing: bool = False,
        collisions: Dict[str, set[BibleBookEnum]] | None = None,
    ) -> None:
        """Insert all terms from ``source`` into ``table`` as case-insensitive keys.

        Args:
            table: Destination lookup table to mutate.
            source: Book-term mappings to register.
            prefer_existing: Keep existing term mapping if already present.
            collisions: Optional destination map for ambiguous term bookkeeping.
        """
        for book, terms in source.items():
            for term in terms:
                normalized = term.casefold()
                existing = table.get(normalized)
                if existing is not None and existing != book and collisions is not None:
                    collisions.setdefault(normalized, {existing}).add(book)
                if existing is None or not prefer_existing:
                    table[normalized] = book

    @classmethod
    def _register_terms_by_language(
        cls,
        table: Dict[str, BibleBookEnum],
        source: Dict[str, Dict[BibleBookEnum, Iterable[str]]],
        *,
        prefer_existing: bool = False,
        collisions: Dict[str, set[BibleBookEnum]] | None = None,
    ) -> None:
        """Merge all language term maps into a single lookup table.

        Args:
            table: Destination lookup table to mutate.
            source: Per-language term tables.
            prefer_existing: Keep existing term mapping if already present.
            collisions: Optional destination map for ambiguous term bookkeeping.
        """
        ordered_language_codes = tuple(
            code for code in cls.AUTO_LANGUAGE_PRECEDENCE if code in source
        )
        unordered_language_codes = tuple(
            code for code in source if code not in ordered_language_codes
        )
        for language_code in (*ordered_language_codes, *unordered_language_codes):
            books_for_language = source[language_code]
            cls._register_terms(
                table,
                books_for_language,
                prefer_existing=prefer_existing,
                collisions=collisions,
            )

    @staticmethod
    def _lookup_term(
        lookup: Dict[str, BibleBookEnum],
        normalized: str,
    ) -> BibleBookEnum | None:
        """Look up a term directly, then with punctuation/space-insensitive fallbacks.

        Args:
            lookup: Normalized lookup table.
            normalized: Normalized term key.

        Returns:
            BibleBookEnum | None: Matching book enum or ``None``.
        """
        direct = lookup.get(normalized)
        if direct is not None:
            return direct

        without_periods = normalized.replace(".", "")
        no_period_match = lookup.get(without_periods)
        if no_period_match is not None:
            return no_period_match

        return lookup.get(without_periods.replace(" ", ""))


class BaseReference(ABC):
    """Shared parsing utilities for concrete verse reference value objects.

    Class Attributes:
        _PATTERN (re.Pattern[str]): Regex for the concrete parser.
        _BOOK_LOOKUP (_BookTermLookup): Shared localized book lookup helper.
    """

    _PATTERN: re.Pattern[str]

    BOOK_LOOKUP = _BookTermLookup(
        names_by_language=BOOK_NAMES_BY_LANGUAGE,
        abbreviations_by_language=BOOK_ABBREVIATIONS_BY_LANGUAGE,
    )

    @classmethod
    def from_str(
        cls: type[ReferenceT],
        ref: str,
        language: BibleLanguageEnum | str | None = BibleLanguageEnum.AUTO,
    ) -> ReferenceT:
        """Parse a Bible reference string into the concrete reference type.

        Args:
            ref: Bible reference text to parse.
            language: Language enum/code/``None`` controlling book parsing.

        Returns:
            ReferenceT: Parsed reference object matching ``cls``.

        Raises:
            ParseVerseRefError: If the input is empty or invalid.
            ValueError: If ``language`` cannot be normalized.
        """
        if not isinstance(ref, str):
            raise ParseVerseRefError(
                code="invalid_reference_type",
                details=f"reference must be a string, got {type(ref).__name__}",
            )
        if not ref:
            raise ParseVerseRefError(
                code="empty_reference",
                details="reference string is empty",
            )

        match = cls._PATTERN.match(ref)
        if match is None:
            raise ParseVerseRefError(
                code="pattern_mismatch",
                details=f"reference {ref!r} does not match expected format",
            )

        parsed_language = cls.BOOK_LOOKUP.normalize_language(language)
        return cls._from_match(match, parsed_language)

    @staticmethod
    def _parse_positive_int(value: str | None) -> int:
        """Parse ``value`` as a strictly positive integer.

        Args:
            value: Numeric string from regex capture groups.

        Returns:
            int: Parsed positive integer.

        Raises:
            ParseVerseRefError: If a value is missing, non-numeric, or non-positive.
        """
        if value is None:
            raise ParseVerseRefError(
                code="missing_numeric_token",
                details="missing numeric component in parsed reference",
            )

        try:
            parsed = int(value)
        except ValueError as e:
            raise ParseVerseRefError(
                code="invalid_numeric_token",
                details=f"numeric token {value!r} is not an integer",
            ) from e

        if parsed <= 0:
            raise ParseVerseRefError(
                code="non_positive_numeric_token",
                details=f"numeric token {value!r} must be greater than zero",
            )
        return parsed

    @classmethod
    @abstractmethod
    def _from_match(
        cls: type[ReferenceT],
        match: re.Match[str],
        language: BibleLanguageEnum,
    ) -> ReferenceT:
        """Build a concrete reference object from a validated regex match.

        Args:
            match: Valid regex match object.
            language: Normalized language enum for book parsing.

        Returns:
            ReferenceT: Parsed concrete reference object matching ``cls``.

        Raises:
            ParseVerseRefError: If captured values are invalid.
            NotImplementedError: In this abstract base implementation.
        """
        raise NotImplementedError


@dataclass(frozen=True, slots=True)
class VerseRef(BaseReference):
    """A single verse reference, e.g. ``John 3:16``.

    Attributes:
        book (BibleBookEnum): Parsed book enum.
        chapter (int): Parsed chapter number.
        verse (int): Parsed verse number.
    """

    book: BibleBookEnum
    chapter: int
    verse: int

    _PATTERN = _VERSE_REF_PATTERN

    def __str__(self) -> str:
        """Serialize the verse reference in canonical ``Book C:V`` format.

        Returns:
            str: Canonical verse reference string.
        """
        return f"{self.book.full_name} {self.chapter}:{self.verse}"

    @classmethod
    def _from_match(cls, match: re.Match[str], language: BibleLanguageEnum) -> "VerseRef":
        """Construct ``VerseRef`` from a regex match produced by ``_PATTERN``.

        Args:
            match: Regex match from the verse pattern.
            language: Normalized language enum for book parsing.

        Returns:
            VerseRef: Parsed single-verse reference.

        Raises:
            ParseVerseRefError: If captured groups are invalid.
        """
        chapter = cls._parse_positive_int(match.group("chapter"))
        verse = cls._parse_positive_int(match.group("verse"))
        book = cls.BOOK_LOOKUP.parse_book_name(match.group("book"), language)
        return cls(book=book, chapter=chapter, verse=verse)


@dataclass(frozen=True, slots=True)
class VerseRangeRef(BaseReference):
    """A verse range reference, e.g. ``John 3:16-18`` or ``John 3:16-4:2``.

    Attributes:
        start (VerseRef): Start verse of the range.
        end (VerseRef): End verse of the range.
    """

    start: VerseRef
    end: VerseRef

    _PATTERN = _VERSE_RANGE_REF_PATTERN

    def __str__(self) -> str:
        """Serialize the range using the shortest unambiguous textual form.

        Returns:
            str: Canonical verse range string.
        """
        if self.start.book == self.end.book:
            book_name = self.start.book.full_name
            if self.start.chapter == self.end.chapter:
                return (
                    f"{book_name} {self.start.chapter}:{self.start.verse}"
                    f"-{self.end.verse}"
                )
            return (
                f"{book_name} {self.start.chapter}:{self.start.verse}"
                f"-{self.end.chapter}:{self.end.verse}"
            )
        return (
            f"{self.start.book.full_name} {self.start.chapter}:{self.start.verse}"
            f"-{self.end.book.full_name} {self.end.chapter}:{self.end.verse}"
        )

    @classmethod
    def _from_match(
        cls,
        match: re.Match[str],
        language: BibleLanguageEnum,
    ) -> "VerseRangeRef":
        """Construct ``VerseRangeRef`` from a regex match produced by ``_PATTERN``.

        Args:
            match: Regex match from the range pattern.
            language: Normalized language enum for book parsing.

        Returns:
            VerseRangeRef: Parsed verse range reference.

        Raises:
            ParseVerseRefError: If captured groups are invalid.
        """
        start_chapter = cls._parse_positive_int(match.group("start_chapter"))
        start_verse = cls._parse_positive_int(match.group("start_verse"))
        end_verse = cls._parse_positive_int(match.group("end_verse"))

        end_chapter_match = match.group("end_chapter")
        end_chapter = (
            cls._parse_positive_int(end_chapter_match)
            if end_chapter_match is not None
            else start_chapter
        )

        start_book = cls.BOOK_LOOKUP.parse_book_name(match.group("start_book"), language)
        end_book_match = match.group("end_book")
        end_book = (
            cls.BOOK_LOOKUP.parse_book_name(end_book_match, language)
            if end_book_match
            else start_book
        )

        if end_book == start_book and (end_chapter, end_verse) <= (
            start_chapter,
            start_verse,
        ):
            raise ParseVerseRefError(
                code="same_book_range_not_ascending",
                details="end reference must come after start reference for same-book ranges",
            )

        return cls(
            start=VerseRef(book=start_book, chapter=start_chapter, verse=start_verse),
            end=VerseRef(book=end_book, chapter=end_chapter, verse=end_verse),
        )


AUTO_LANGUAGE_PRECEDENCE: tuple[str, ...] = _BookTermLookup.AUTO_LANGUAGE_PRECEDENCE
AUTO_LANGUAGE_COLLISIONS: Dict[str, tuple[BibleBookEnum, ...]] = BaseReference.BOOK_LOOKUP.auto_collisions


Reference = VerseRef | VerseRangeRef


def parse_reference(
    ref: str,
    language: BibleLanguageEnum | str | None = BibleLanguageEnum.AUTO,
) -> Reference:
    """Parse ``ref`` into either a ``VerseRef`` or ``VerseRangeRef``.

    The function first attempts single-verse parsing. If the input does not
    match the single-verse shape, it falls back to range parsing.

    Args:
        ref: Bible reference text to parse.
        language: Language enum/code/``None`` controlling book parsing.

    Returns:
        Reference: Parsed ``VerseRef`` or ``VerseRangeRef``.

    Raises:
        ParseVerseRefError: If both parsing strategies fail.
        ValueError: If ``language`` cannot be normalized.
    """
    try:
        return VerseRef.from_str(ref, language=language)
    except ParseVerseRefError as verse_error:
        if verse_error.code != "pattern_mismatch":
            raise
    return VerseRangeRef.from_str(ref, language=language)


