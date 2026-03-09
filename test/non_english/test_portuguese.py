import pytest
from bible_io_references.references import VerseRef, VerseRangeRef
from bible_io_references.language_enums import BibleLanguageEnum
from bible_io_references.bible_book_enums import BibleBookEnum
from bible_io_references.languages import portuguese

LANGUAGE = BibleLanguageEnum.PORTUGUESE


@pytest.mark.parametrize(
    "reference, expected",
    [
        ("João 3:16", (BibleBookEnum.John, 3, 16)),
        ("Apoc 21:4", (BibleBookEnum.Revelation, 21, 4)),
    ],
)
def test_parse_portuguese_reference(reference, expected):
    ref = VerseRef.from_str(reference, language=LANGUAGE)

    assert (ref.book, ref.chapter, ref.verse) == expected


@pytest.mark.parametrize(
    "reference, expected",
    [
        (
            "João 3:16-17",
            (
                (BibleBookEnum.John, 3, 16),
                (BibleBookEnum.John, 3, 17),
            ),
        ),
        (
            "Apoc 21:4–5",
            (
                (BibleBookEnum.Revelation, 21, 4),
                (BibleBookEnum.Revelation, 21, 5),
            ),
        ),
        (
            "João 3:16-4:1",
            (
                (BibleBookEnum.John, 3, 16),
                (BibleBookEnum.John, 4, 1),
            ),
        ),
        (
            "João 3.16-4.1",
            (
                (BibleBookEnum.John, 3, 16),
                (BibleBookEnum.John, 4, 1),
            ),
        ),
    ],
)
def test_parse_portuguese_verse_range(reference, expected):
    ref = VerseRangeRef.from_str(reference, language=LANGUAGE)

    assert (ref.start.book, ref.start.chapter, ref.start.verse) == expected[0]
    assert (ref.end.book, ref.end.chapter, ref.end.verse) == expected[1]


@pytest.mark.parametrize("expected_book", list(BibleBookEnum))
def test_parse_portuguese_book_names(expected_book):
    names = portuguese.BOOK_NAMES.get(expected_book)

    assert names, f"Missing BOOK_NAMES entry for {expected_book.name}"

    ref = VerseRef.from_str(f"{names[0]} 1:1", language=LANGUAGE)

    assert (ref.book, ref.chapter, ref.verse) == (expected_book, 1, 1)


@pytest.mark.parametrize("expected_book", list(BibleBookEnum))
def test_parse_portuguese_book_abbreviations(expected_book):
    abbreviations = portuguese.BOOK_ABBREVIATIONS.get(expected_book)

    assert abbreviations, f"Missing BOOK_ABBREVIATIONS entry for {expected_book.name}"

    for abbreviation in abbreviations:
        ref = VerseRef.from_str(f"{abbreviation} 1:1", language=LANGUAGE)

        assert (ref.book, ref.chapter, ref.verse) == (expected_book, 1, 1)
