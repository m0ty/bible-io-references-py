import pytest
from src.bible_io_references.references import VerseRef
from src.bible_io_references.language_enums import BibleLanguageEnum
from src.bible_io_references.bible_book_enums import BibleBookEnum
from src.bible_io_references.languages import french

LANGUAGE = BibleLanguageEnum.FRENCH


@pytest.mark.parametrize(
    "reference, expected",
    [
        ("Jean 3:16", (BibleBookEnum.John, 3, 16)),
        ("Ap. 21:4", (BibleBookEnum.Revelation, 21, 4)),
    ],
)
def test_parse_french_reference(reference, expected):
    ref = VerseRef.from_str(reference, language=LANGUAGE)

    assert (ref.book, ref.chapter, ref.verse) == expected


@pytest.mark.parametrize("expected_book", list(BibleBookEnum))
def test_parse_french_book_names(expected_book):
    names = french.BOOK_NAMES.get(expected_book)

    assert names, f"Missing BOOK_NAMES entry for {expected_book.name}"

    ref = VerseRef.from_str(f"{names[0]} 1:1", language=LANGUAGE)

    assert (ref.book, ref.chapter, ref.verse) == (expected_book, 1, 1)


@pytest.mark.parametrize("expected_book", list(BibleBookEnum))
def test_parse_french_book_abbreviations(expected_book):
    abbreviations = french.BOOK_ABBREVIATIONS.get(expected_book)

    assert abbreviations, f"Missing BOOK_ABBREVIATIONS entry for {expected_book.name}"

    for abbreviation in abbreviations:
        ref = VerseRef.from_str(f"{abbreviation} 1:1", language=LANGUAGE)

        assert (ref.book, ref.chapter, ref.verse) == (expected_book, 1, 1)
