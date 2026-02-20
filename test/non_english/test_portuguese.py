import importlib

import pytest

references = importlib.import_module("bible-io-references.references")
books = importlib.import_module("bible-io-references.bible_book_enums")


@pytest.mark.parametrize(
    "reference, expected",
    [
        ("João 3:16", (books.BibleBookEnum.John, 3, 16)),
        ("Apoc 21:4", (books.BibleBookEnum.Revelation, 21, 4)),
    ],
)
def test_parse_portuguese_reference(reference, expected):
    ref = references.VerseRef.from_str(reference)

    assert (ref.book, ref.chapter, ref.verse) == expected


@pytest.mark.parametrize(
    "reference, expected",
    [
        (
            "João 3:16-17",
            (
                (books.BibleBookEnum.John, 3, 16),
                (books.BibleBookEnum.John, 3, 17),
            ),
        ),
        (
            "Apoc 21:4–5",
            (
                (books.BibleBookEnum.Revelation, 21, 4),
                (books.BibleBookEnum.Revelation, 21, 5),
            ),
        ),
    ],
)
def test_parse_portuguese_verse_range(reference, expected):
    ref = references.VerseRangeRef.from_str(reference)

    assert (ref.start.book, ref.start.chapter, ref.start.verse) == expected[0]
    assert (ref.end.book, ref.end.chapter, ref.end.verse) == expected[1]
