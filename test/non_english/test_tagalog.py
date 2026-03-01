import importlib

import pytest

references = importlib.import_module("bible-io-references.references")
books = importlib.import_module("bible-io-references.bible_book_enums")
tagalog = importlib.import_module("bible-io-references.languages.tagalog")


@pytest.mark.parametrize(
    "reference, expected",
    [
        ("Juan 3:16", (books.BibleBookEnum.John, 3, 16)),
        ("Pah 21:4", (books.BibleBookEnum.Revelation, 21, 4)),
    ],
)
def test_parse_tagalog_reference(reference, expected):
    ref = references.VerseRef.from_str(reference)

    assert (ref.book, ref.chapter, ref.verse) == expected


@pytest.mark.parametrize(
    "reference, expected_book",
    [(f"{names[0]} 1:1", book) for book, names in tagalog.BOOK_NAMES.items()],
)
def test_parse_tagalog_book_names(reference, expected_book):
    ref = references.VerseRef.from_str(reference)

    assert (ref.book, ref.chapter, ref.verse) == (expected_book, 1, 1)


@pytest.mark.parametrize(
    "reference, expected_book",
    [
        (f"{abbr} 1:1", book)
        for book, abbreviations in tagalog.BOOK_ABBREVIATIONS.items()
        for abbr in abbreviations
    ],
)
def test_parse_tagalog_book_abbreviations(reference, expected_book):
    ref = references.VerseRef.from_str(reference)

    assert (ref.book, ref.chapter, ref.verse) == (expected_book, 1, 1)
