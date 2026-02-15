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
