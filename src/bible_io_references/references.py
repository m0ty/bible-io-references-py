import re
from abc import ABC, abstractmethod
from typing import Dict, Iterable, Self

from .bible_book_enums import BibleBookEnum
from .language_enums import BibleLanguageEnum
from .languages import BOOK_ABBREVIATIONS_BY_LANGUAGE, BOOK_NAMES_BY_LANGUAGE


class ParseVerseRefError(ValueError):
    """Raised when a verse reference string cannot be parsed."""

    def __str__(self) -> str:
        return "invalid verse reference"


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
        self._register_terms_by_language(self._all_languages, names_by_language)
        self._register_terms_by_language(self._all_languages, abbreviations_by_language)

        self._by_language: Dict[str, Dict[str, BibleBookEnum]] = {}
        language_codes = set(names_by_language) | set(abbreviations_by_language)
        
        for code in language_codes:
            table: Dict[str, BibleBookEnum] = {}
            names = names_by_language.get(code)
            if names is not None:
                self._register_terms(table, names)
            abbreviations = abbreviations_by_language.get(code)
            if abbreviations is not None:
                self._register_terms(table, abbreviations)
            self._by_language[code] = table

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
        raise ValueError("language must be a BibleLanguageEnum or string")

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
            raise ParseVerseRefError()

        compact = normalized.replace(".", "").replace(" ", "")
        if language == BibleLanguageEnum.AUTO:
            english_match = self._lookup_term(self._english, normalized)
            if english_match is not None:
                return english_match
            lookup = self._all_languages
        else:
            lookup = self._by_language.get(language.code)

        if lookup is None:
            raise ParseVerseRefError()

        matched = self._lookup_term(lookup, normalized)
        if matched is not None:
            return matched

        if language == BibleLanguageEnum.AUTO:
            try:
                return BibleBookEnum.from_str(compact)
            except ValueError as e:
                raise ParseVerseRefError() from e
        raise ParseVerseRefError()

    @staticmethod
    def _build_english_lookup() -> Dict[str, BibleBookEnum]:
        """Build a lookup table containing canonical and short English book names.

        Returns:
            dict[str, BibleBookEnum]: Casefolded English lookup table.
        """
        lookup = {book.full_name.casefold(): book for book in BibleBookEnum}
        for book in BibleBookEnum:
            lookup[book.as_str().casefold()] = book
        return lookup

    @staticmethod
    def _register_terms(
        table: Dict[str, BibleBookEnum],
        source: Dict[BibleBookEnum, Iterable[str]],
    ) -> None:
        """Insert all terms from ``source`` into ``table`` as case-insensitive keys.

        Args:
            table: Destination lookup table to mutate.
            source: Book-term mappings to register.
        """
        for book, terms in source.items():
            for term in terms:
                table[term.casefold()] = book

    @classmethod
    def _register_terms_by_language(
        cls,
        table: Dict[str, BibleBookEnum],
        source: Dict[str, Dict[BibleBookEnum, Iterable[str]]],
    ) -> None:
        """Merge all language term maps into a single lookup table.

        Args:
            table: Destination lookup table to mutate.
            source: Per-language term tables.
        """
        for books_for_language in source.values():
            cls._register_terms(table, books_for_language)

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





class _BaseReference(ABC):
    """Shared parsing utilities for concrete verse reference value objects.

    Class Attributes:
        _PATTERN (re.Pattern[str]): Regex for the concrete parser.
        _BOOK_LOOKUP (_BookTermLookup): Shared localized book lookup helper.
    """

    _PATTERN: re.Pattern[str]

    _BOOK_LOOKUP = _BookTermLookup(
        names_by_language=BOOK_NAMES_BY_LANGUAGE,
        abbreviations_by_language=BOOK_ABBREVIATIONS_BY_LANGUAGE,
    )


    @classmethod
    def from_str(
        cls,
        ref: str,
        language: BibleLanguageEnum | str | None = BibleLanguageEnum.AUTO,
    ) -> Self:
        """Parse a Bible reference string into the concrete reference type.

        Args:
            ref: Bible reference text to parse.
            language: Language enum/code/``None`` controlling book parsing.

        Returns:
            Self: Parsed reference object.

        Raises:
            ParseVerseRefError: If the input is empty or invalid.
            ValueError: If ``language`` cannot be normalized.
        """
        if not isinstance(ref, str) or not ref:
            raise ParseVerseRefError()

        match = cls._PATTERN.match(ref)
        if match is None:
            raise ParseVerseRefError()

        parsed_language = cls._BOOK_LOOKUP.normalize_language(language)
        return cls._from_match(match, parsed_language)

    @staticmethod
    def _parse_positive_int(value: str | None) -> int:
        """Parse ``value`` as a strictly positive integer.

        Args:
            value: Numeric string from regex capture groups.

        Returns:
            int: Parsed positive integer.

        Raises:
            ParseVerseRefError: If value is missing, non-numeric, or non-positive.
        """
        if value is None:
            raise ParseVerseRefError()

        try:
            parsed = int(value)
        except ValueError as e:
            raise ParseVerseRefError() from e

        if parsed <= 0:
            raise ParseVerseRefError()
        return parsed

    @classmethod
    @abstractmethod
    def _from_match(cls, match: re.Match[str], language: BibleLanguageEnum) -> Self:
        """Build a concrete reference object from a validated regex match.

        Args:
            match: Valid regex match object.
            language: Normalized language enum for book parsing.

        Returns:
            Self: Parsed concrete reference object.

        Raises:
            ParseVerseRefError: If captured values are invalid.
            NotImplementedError: In this abstract base implementation.
        """
        raise NotImplementedError


class VerseRef(_BaseReference):
    """A single verse reference, e.g. ``John 3:16``.

    Attributes:
        book (BibleBookEnum): Parsed book enum.
        chapter (int): Parsed chapter number.
        verse (int): Parsed verse number.
    """

    _PATTERN = _VERSE_REF_PATTERN

    def __init__(self, book_enum: BibleBookEnum, chapter: int, verse: int):
        """Create a single-verse reference from parsed components.

        Args:
            book_enum: Parsed book enum.
            chapter: Chapter number.
            verse: Verse number.
        """
        self.book = book_enum
        self.chapter = chapter
        self.verse = verse

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
        book = cls._BOOK_LOOKUP.parse_book_name(match.group("book"), language)
        return cls(book_enum=book, chapter=chapter, verse=verse)


class VerseRangeRef(_BaseReference):
    """A verse range reference, e.g. ``John 3:16-18`` or ``John 3:16-4:2``.

    Attributes:
        start (VerseRef): Start verse of the range.
        end (VerseRef): End verse of the range.
    """

    _PATTERN = _VERSE_RANGE_REF_PATTERN

    def __init__(self, start: VerseRef, end: VerseRef):
        """Create a range reference with explicit start and end verse refs.

        Args:
            start: Start verse reference.
            end: End verse reference.
        """
        self.start = start
        self.end = end

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

        start_book = cls._BOOK_LOOKUP.parse_book_name(match.group("start_book"), language)
        end_book_match = match.group("end_book")
        end_book = (
            cls._BOOK_LOOKUP.parse_book_name(end_book_match, language)
            if end_book_match
            else start_book
        )

        return cls(
            start=VerseRef(book_enum=start_book, chapter=start_chapter, verse=start_verse),
            end=VerseRef(book_enum=end_book, chapter=end_chapter, verse=end_verse),
        )
