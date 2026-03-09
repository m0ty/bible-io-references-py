import pytest
from bible_io_references.references import VerseRef, VerseRangeRef
from bible_io_references.language_enums import BibleLanguageEnum
from bible_io_references.bible_book_enums import BibleBookEnum
from bible_io_references.languages import russian

LANGUAGE = BibleLanguageEnum.RUSSIAN


@pytest.mark.parametrize(
    "reference, expected",
    [
        ("Иоанна 3:16", (BibleBookEnum.John, 3, 16)),
        ("Ин. 3:16", (BibleBookEnum.John, 3, 16)),
    ],
)
def test_parse_russian_reference(reference, expected):
    ref = VerseRef.from_str(reference, language=LANGUAGE)

    assert (ref.book, ref.chapter, ref.verse) == expected


@pytest.mark.parametrize(
    "reference, expected",
    [
        (
            "Иоанна 3:16-17",
            (
                (BibleBookEnum.John, 3, 16),
                (BibleBookEnum.John, 3, 17),
            ),
        ),
        (
            "Ин. 3:16–17",
            (
                (BibleBookEnum.John, 3, 16),
                (BibleBookEnum.John, 3, 17),
            ),
        ),
        (
            "Иоанна 3:16-4:1",
            (
                (BibleBookEnum.John, 3, 16),
                (BibleBookEnum.John, 4, 1),
            ),
        ),
        (
            "Иоанна 3.16-4.1",
            (
                (BibleBookEnum.John, 3, 16),
                (BibleBookEnum.John, 4, 1),
            ),
        ),
    ],
)
def test_parse_russian_verse_range(reference, expected):
    ref = VerseRangeRef.from_str(reference, language=LANGUAGE)

    assert (ref.start.book, ref.start.chapter, ref.start.verse) == expected[0]
    assert (ref.end.book, ref.end.chapter, ref.end.verse) == expected[1]


@pytest.mark.parametrize("expected_book", list(BibleBookEnum))
def test_parse_russian_book_names(expected_book):
    names = russian.BOOK_NAMES.get(expected_book)

    assert names, f"Missing BOOK_NAMES entry for {expected_book.name}"

    ref = VerseRef.from_str(f"{names[0]} 1:1", language=LANGUAGE)

    assert (ref.book, ref.chapter, ref.verse) == (expected_book, 1, 1)


@pytest.mark.parametrize("expected_book", list(BibleBookEnum))
def test_parse_russian_book_abbreviations(expected_book):
    abbreviations = russian.BOOK_ABBREVIATIONS.get(expected_book)

    assert abbreviations, f"Missing BOOK_ABBREVIATIONS entry for {expected_book.name}"

    for abbreviation in abbreviations:
        ref = VerseRef.from_str(f"{abbreviation} 1:1", language=LANGUAGE)

        assert (ref.book, ref.chapter, ref.verse) == (expected_book, 1, 1)
