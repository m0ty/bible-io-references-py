import pytest
from src.bible_io_references.references import VerseRef, VerseRangeRef
from src.bible_io_references.language_enums import BibleLanguageEnum
from src.bible_io_references.bible_book_enums import BibleBookEnum
from src.bible_io_references.languages import spanish

LANGUAGE = BibleLanguageEnum.SPANISH


@pytest.mark.parametrize(
    "reference, expected",
    [
        ("Juan 3:16", (BibleBookEnum.John, 3, 16)),
        ("Mat. 5:9", (BibleBookEnum.Matthew, 5, 9)),
    ],
)
def test_parse_spanish_reference(reference, expected):
    ref = VerseRef.from_str(reference, language=LANGUAGE)

    assert (ref.book, ref.chapter, ref.verse) == expected


@pytest.mark.parametrize(
    "reference, expected",
    [
        (
            "Juan 3:16-17",
            (
                (BibleBookEnum.John, 3, 16),
                (BibleBookEnum.John, 3, 17),
            ),
        ),
        (
            "Mat. 5:9–10",
            (
                (BibleBookEnum.Matthew, 5, 9),
                (BibleBookEnum.Matthew, 5, 10),
            ),
        ),
        (
            "Juan 3:16-4:1",
            (
                (BibleBookEnum.John, 3, 16),
                (BibleBookEnum.John, 4, 1),
            ),
        ),
        (
            "Juan 3.16-4.1",
            (
                (BibleBookEnum.John, 3, 16),
                (BibleBookEnum.John, 4, 1),
            ),
        ),
    ],
)
def test_parse_spanish_verse_range(reference, expected):
    ref = VerseRangeRef.from_str(reference, language=LANGUAGE)

    assert (ref.start.book, ref.start.chapter, ref.start.verse) == expected[0]
    assert (ref.end.book, ref.end.chapter, ref.end.verse) == expected[1]


@pytest.mark.parametrize("expected_book", list(BibleBookEnum))
def test_parse_spanish_book_names(expected_book):
    names = spanish.BOOK_NAMES.get(expected_book)

    assert names, f"Missing BOOK_NAMES entry for {expected_book.name}"

    ref = VerseRef.from_str(f"{names[0]} 1:1", language=LANGUAGE)

    assert (ref.book, ref.chapter, ref.verse) == (expected_book, 1, 1)


@pytest.mark.parametrize("expected_book", list(BibleBookEnum))
def test_parse_spanish_book_abbreviations(expected_book):
    abbreviations = spanish.BOOK_ABBREVIATIONS.get(expected_book)

    assert abbreviations, f"Missing BOOK_ABBREVIATIONS entry for {expected_book.name}"

    for abbreviation in abbreviations:
        ref = VerseRef.from_str(f"{abbreviation} 1:1", language=LANGUAGE)

        assert (ref.book, ref.chapter, ref.verse) == (expected_book, 1, 1)
