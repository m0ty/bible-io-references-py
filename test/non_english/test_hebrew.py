import importlib

import pytest

references = importlib.import_module("bible-io-references.references")
books = importlib.import_module("bible-io-references.bible_book_enums")


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
