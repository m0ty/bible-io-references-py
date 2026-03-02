import re
from typing import Dict, Iterable

from .bible_book_enums import BibleBookEnum
from .language_enums import BibleLanguageEnum
from .languages import BOOK_ABBREVIATIONS_BY_LANGUAGE, BOOK_NAMES_BY_LANGUAGE

_BOOK_NAMES_BY_LANGUAGE = BOOK_NAMES_BY_LANGUAGE
_BOOK_ABBREVIATIONS_BY_LANGUAGE = BOOK_ABBREVIATIONS_BY_LANGUAGE


class ParseVerseRefError(ValueError):
    """Error raised when parsing a verse reference string fails."""

    def __str__(self) -> str:
        return "invalid verse reference"


_VERSE_REF_PATTERN = re.compile(
    r"^\s*(?P<book>.+?)\s+(?P<chapter>\d+)\s*[:.]\s*(?P<verse>\d+)\s*$"
)

_VERSE_RANGE_REF_PATTERN = re.compile(
    r"^\s*(?P<start_book>.+?)\s+(?P<start_chapter>\d+)\s*[:.]\s*(?P<start_verse>\d+)\s*"
    r"[-–—]\s*(?:(?P<end_book>.+?)\s+)?(?:(?P<end_chapter>\d+)\s*[:.]\s*)?"
    r"(?P<end_verse>\d+)\s*$"
)

def _register_book_terms(
    table: Dict[str, BibleBookEnum],
    source: Dict[BibleBookEnum, Iterable[str]],
) -> None:
    for book, terms in source.items():
        for term in terms:
            table[term.casefold()] = book


def _register_book_terms_by_language(
    table: Dict[str, BibleBookEnum],
    source: Dict[str, Dict[BibleBookEnum, Iterable[str]]],
) -> None:
    for books_for_language in source.values():
        _register_book_terms(table, books_for_language)


# Centralized lookup table used by parsing logic.
_BOOK_NAME_TO_ENUM: Dict[str, BibleBookEnum] = {
    book.full_name.casefold(): book for book in BibleBookEnum
}
_register_book_terms_by_language(_BOOK_NAME_TO_ENUM, _BOOK_NAMES_BY_LANGUAGE)
_register_book_terms_by_language(_BOOK_NAME_TO_ENUM, _BOOK_ABBREVIATIONS_BY_LANGUAGE)

_LANGUAGE_CODES = set(_BOOK_NAMES_BY_LANGUAGE) | set(_BOOK_ABBREVIATIONS_BY_LANGUAGE)
_BOOK_NAME_TO_ENUM_BY_LANGUAGE: Dict[str, Dict[str, BibleBookEnum]] = {}
for code in _LANGUAGE_CODES:
    table: Dict[str, BibleBookEnum] = {}
    names = _BOOK_NAMES_BY_LANGUAGE.get(code)
    if names is not None:
        _register_book_terms(table, names)
    abbreviations = _BOOK_ABBREVIATIONS_BY_LANGUAGE.get(code)
    if abbreviations is not None:
        _register_book_terms(table, abbreviations)
    _BOOK_NAME_TO_ENUM_BY_LANGUAGE[code] = table


class VerseRef:
    def __init__(self, book_enum: BibleBookEnum, chapter: int, verse: int):
        self.book = book_enum
        self.chapter = chapter
        self.verse = verse

    def __str__(self) -> str:
        return f"{self.book.full_name} {self.chapter}:{self.verse}"

    @classmethod
    def from_str(
        cls,
        ref: str,
        language: BibleLanguageEnum | str | None = BibleLanguageEnum.AUTO,
    ) -> "VerseRef":
        """Parse a verse reference string like ``John 3:16`` into a VerseRef.

        If ``language`` is ``AUTO`` (default), the parser searches all languages.
        Otherwise, it only matches terms for the specified language.
        """
        if not isinstance(ref, str) or not ref:
            raise ParseVerseRefError()

        match = _VERSE_REF_PATTERN.match(ref)
        if not match:
            raise ParseVerseRefError()

        try:
            chapter = int(match.group("chapter"))
            verse = int(match.group("verse"))
        except ValueError as e:
            raise ParseVerseRefError() from e

        if chapter <= 0 or verse <= 0:
            raise ParseVerseRefError()

        book = _parse_book_name(match.group("book"), _normalize_language(language))
        return cls(book_enum=book, chapter=chapter, verse=verse)


def _normalize_language(language: BibleLanguageEnum | str | None) -> BibleLanguageEnum:
    if language is None:
        return BibleLanguageEnum.AUTO
    if isinstance(language, BibleLanguageEnum):
        return language
    if isinstance(language, str):
        return BibleLanguageEnum.from_str(language)
    raise ValueError("language must be a BibleLanguageEnum or string")


def _parse_book_name(book_text: str, language: BibleLanguageEnum) -> BibleBookEnum:
    normalized = " ".join(book_text.split()).casefold()
    if not normalized:
        raise ParseVerseRefError()

    if language == BibleLanguageEnum.AUTO:
        lookup = _BOOK_NAME_TO_ENUM
        allow_enum_fallback = True
    else:
        lookup = _BOOK_NAME_TO_ENUM_BY_LANGUAGE.get(language.code)
        allow_enum_fallback = False

    if lookup is None:
        raise ParseVerseRefError()

    direct = lookup.get(normalized)
    if direct is not None:
        return direct

    normalized_without_period = normalized.replace(".", "")
    without_period = lookup.get(normalized_without_period)
    if without_period is not None:
        return without_period

    compact = normalized_without_period.replace(" ", "")
    compact_match = lookup.get(compact)
    if compact_match is not None:
        return compact_match

    if allow_enum_fallback:
        try:
            return BibleBookEnum.from_str(compact)
        except ValueError as e:
            raise ParseVerseRefError() from e
    raise ParseVerseRefError()


class VerseRangeRef:
    def __init__(self, start: VerseRef, end: VerseRef):
        self.start = start
        self.end = end

    def __str__(self) -> str:
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
    def from_str(
        cls,
        ref: str,
        language: BibleLanguageEnum | str | None = BibleLanguageEnum.AUTO,
    ) -> "VerseRangeRef":
        """Parse a verse range like ``John 3:16-17`` into a VerseRangeRef.

        If ``language`` is ``AUTO`` (default), the parser searches all languages.
        Otherwise, it only matches terms for the specified language.
        """
        if not isinstance(ref, str) or not ref:
            raise ParseVerseRefError()

        match = _VERSE_RANGE_REF_PATTERN.match(ref)
        if not match:
            raise ParseVerseRefError()

        try:
            start_chapter = int(match.group("start_chapter"))
            start_verse = int(match.group("start_verse"))
            end_verse = int(match.group("end_verse"))
            end_chapter_match = match.group("end_chapter")
            end_chapter = (
                int(end_chapter_match)
                if end_chapter_match is not None
                else start_chapter
            )
        except ValueError as e:
            raise ParseVerseRefError() from e

        if min(start_chapter, start_verse, end_chapter, end_verse) <= 0:
            raise ParseVerseRefError()

        parsed_language = _normalize_language(language)
        start_book = _parse_book_name(match.group("start_book"), parsed_language)
        end_book_match = match.group("end_book")
        end_book = (
            _parse_book_name(end_book_match, parsed_language)
            if end_book_match
            else start_book
        )

        return cls(
            start=VerseRef(book_enum=start_book, chapter=start_chapter, verse=start_verse),
            end=VerseRef(book_enum=end_book, chapter=end_chapter, verse=end_verse),
        )
