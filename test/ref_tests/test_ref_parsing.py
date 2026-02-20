import importlib

import pytest

references = importlib.import_module("bible-io-references.references")
books = importlib.import_module("bible-io-references.bible_book_enums")


@pytest.mark.parametrize(
    "reference, expected",
    [
        ("John 3:16", (books.BibleBookEnum.John, 3, 16)),
        ("jo 1:1", (books.BibleBookEnum.John, 1, 1)),
    ],
)
def test_parse_reference(reference, expected):
    ref = references.VerseRef.from_str(reference)

    assert (ref.book, ref.chapter, ref.verse) == expected


@pytest.mark.parametrize("reference", ["NotABook 3:16"])
def test_parse_invalid_reference_raises_parse_error(reference):
    with pytest.raises(references.ParseVerseRefError):
        references.VerseRef.from_str(reference)


@pytest.mark.parametrize(
    "reference, expected",
    [
        (
            "John 3:16-17",
            (
                (books.BibleBookEnum.John, 3, 16),
                (books.BibleBookEnum.John, 3, 17),
            ),
        ),
        (
            "John 3:16–17",
            (
                (books.BibleBookEnum.John, 3, 16),
                (books.BibleBookEnum.John, 3, 17),
            ),
        ),
        (
            "John 3:16-4:1",
            (
                (books.BibleBookEnum.John, 3, 16),
                (books.BibleBookEnum.John, 4, 1),
            ),
        ),
        (
            "John 3:16-Acts 1:2",
            (
                (books.BibleBookEnum.John, 3, 16),
                (books.BibleBookEnum.Acts, 1, 2),
            ),
        ),
    ],
)
def test_parse_verse_range(reference, expected):
    ref = references.VerseRangeRef.from_str(reference)

    assert (ref.start.book, ref.start.chapter, ref.start.verse) == expected[0]
    assert (ref.end.book, ref.end.chapter, ref.end.verse) == expected[1]


@pytest.mark.parametrize("reference", ["John 3:16", "John 3:16-0", "NotABook 3:16-17"])
def test_parse_invalid_verse_range_raises_parse_error(reference):
    with pytest.raises(references.ParseVerseRefError):
        references.VerseRangeRef.from_str(reference)
