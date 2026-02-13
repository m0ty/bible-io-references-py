import re
from typing import Dict, Iterable

from .bible_book_enums import BibleBookEnum
from .languages import BOOK_ABBREVIATIONS_BY_LANGUAGE, BOOK_NAMES_BY_LANGUAGE

_BOOK_NAMES_BY_LANGUAGE = BOOK_NAMES_BY_LANGUAGE
_BOOK_ABBREVIATIONS_BY_LANGUAGE = BOOK_ABBREVIATIONS_BY_LANGUAGE


class ParseVerseRefError(ValueError):
    """Error raised when parsing a verse reference string fails."""

    def __str__(self) -> str:
        return "invalid verse reference"


_VERSE_REF_PATTERN = re.compile(
    r"^\s*(?P<book>.+?)\s+(?P<chapter>\d+)\s*:\s*(?P<verse>\d+)\s*$"
)

def _register_book_terms(
    table: Dict[str, BibleBookEnum],
    source: Dict[str, Dict[BibleBookEnum, Iterable[str]]],
) -> None:
    for books_for_language in source.values():
        for book, terms in books_for_language.items():
            for term in terms:
                table[term.casefold()] = book


# Centralized lookup table used by parsing logic.
_BOOK_NAME_TO_ENUM: Dict[str, BibleBookEnum] = {
    book.full_name.casefold(): book for book in BibleBookEnum
}
_register_book_terms(_BOOK_NAME_TO_ENUM, _BOOK_NAMES_BY_LANGUAGE)
_register_book_terms(_BOOK_NAME_TO_ENUM, _BOOK_ABBREVIATIONS_BY_LANGUAGE)


class VerseRef:
    def __init__(self, book_enum: BibleBookEnum, chapter: int, verse: int):
        self.book = book_enum
        self.chapter = chapter
        self.verse = verse

    def __str__(self) -> str:
        return f"{self.book.full_name} {self.chapter}:{self.verse}"

    @classmethod
    def from_str(cls, ref: str) -> "VerseRef":
        """Parse a verse reference string like ``John 3:16`` into a VerseRef."""
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

        book = _parse_book_name(match.group("book"))
        return cls(book_enum=book, chapter=chapter, verse=verse)


def _parse_book_name(book_text: str) -> BibleBookEnum:
    normalized = " ".join(book_text.split()).casefold()
    if not normalized:
        raise ParseVerseRefError()

    direct = _BOOK_NAME_TO_ENUM.get(normalized)
    if direct is not None:
        return direct

    normalized_without_period = normalized.replace(".", "")
    without_period = _BOOK_NAME_TO_ENUM.get(normalized_without_period)
    if without_period is not None:
        return without_period

    compact = normalized_without_period.replace(" ", "")
    compact_match = _BOOK_NAME_TO_ENUM.get(compact)
    if compact_match is not None:
        return compact_match

    try:
        return BibleBookEnum.from_str(compact)
    except ValueError as e:
        raise ParseVerseRefError() from e


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
