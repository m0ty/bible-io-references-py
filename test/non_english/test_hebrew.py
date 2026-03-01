import importlib

import pytest

references = importlib.import_module("bible-io-references.references")
books = importlib.import_module("bible-io-references.bible_book_enums")
hebrew = importlib.import_module("bible-io-references.languages.hebrew")


@pytest.mark.parametrize(
    "reference, expected",
    [
        ("יוחנן 3:16", (books.BibleBookEnum.John, 3, 16)),
        ("יוח 3:16", (books.BibleBookEnum.John, 3, 16)),
    ],
)
def test_parse_hebrew_reference(reference, expected):
    ref = references.VerseRef.from_str(reference)

    assert (ref.book, ref.chapter, ref.verse) == expected


@pytest.mark.parametrize(
    "reference, expected",
    [
        (
            "יוחנן 3:16-17",
            (
                (books.BibleBookEnum.John, 3, 16),
                (books.BibleBookEnum.John, 3, 17),
            ),
        ),
        (
            "יוח 3:16–17",
            (
                (books.BibleBookEnum.John, 3, 16),
                (books.BibleBookEnum.John, 3, 17),
            ),
        ),
        (
            "יוחנן 3:16-4:1",
            (
                (books.BibleBookEnum.John, 3, 16),
                (books.BibleBookEnum.John, 4, 1),
            ),
        ),
        (
            "יוחנן 3.16-4.1",
            (
                (books.BibleBookEnum.John, 3, 16),
                (books.BibleBookEnum.John, 4, 1),
            ),
        ),
    ],
)
def test_parse_hebrew_verse_range(reference, expected):
    ref = references.VerseRangeRef.from_str(reference)

    assert (ref.start.book, ref.start.chapter, ref.start.verse) == expected[0]
    assert (ref.end.book, ref.end.chapter, ref.end.verse) == expected[1]


@pytest.mark.parametrize(
    "reference, expected_book",
    [(f"{names[0]} 1:1", book) for book, names in hebrew.BOOK_NAMES.items()],
)
def test_parse_hebrew_book_names(reference, expected_book):
    ref = references.VerseRef.from_str(reference)

    assert (ref.book, ref.chapter, ref.verse) == (expected_book, 1, 1)


@pytest.mark.parametrize(
    "reference, expected_book",
    [(f"{abbr} 1:1", book) for book, abbreviations in hebrew.BOOK_ABBREVIATIONS.items() for abbr in abbreviations],
)
def test_parse_hebrew_book_abbreviations(reference, expected_book):
    ref = references.VerseRef.from_str(reference)

    assert (ref.book, ref.chapter, ref.verse) == (expected_book, 1, 1)
