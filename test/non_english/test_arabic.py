import importlib

import pytest

references = importlib.import_module("bible-io-references.references")
books = importlib.import_module("bible-io-references.bible_book_enums")
arabic = importlib.import_module("bible-io-references.languages.arabic")
language_enums = importlib.import_module("bible-io-references.language_enums")
LANGUAGE = language_enums.BibleLanguageEnum.ARABIC


@pytest.mark.parametrize(
    "reference, expected",
    [
        ("يوحنا 3:16", (books.BibleBookEnum.John, 3, 16)),
        ("رؤ 21:4", (books.BibleBookEnum.Revelation, 21, 4)),
    ],
)
def test_parse_arabic_reference(reference, expected):
    ref = references.VerseRef.from_str(reference, language=LANGUAGE)

    assert (ref.book, ref.chapter, ref.verse) == expected


@pytest.mark.parametrize("expected_book", list(books.BibleBookEnum))
def test_parse_arabic_book_names(expected_book):
    names = arabic.BOOK_NAMES.get(expected_book)

    assert names, f"Missing BOOK_NAMES entry for {expected_book.name}"

    ref = references.VerseRef.from_str(f"{names[0]} 1:1", language=LANGUAGE)

    assert (ref.book, ref.chapter, ref.verse) == (expected_book, 1, 1)


@pytest.mark.parametrize("expected_book", list(books.BibleBookEnum))
def test_parse_arabic_book_abbreviations(expected_book):
    abbreviations = arabic.BOOK_ABBREVIATIONS.get(expected_book)

    assert abbreviations, f"Missing BOOK_ABBREVIATIONS entry for {expected_book.name}"

    for abbreviation in abbreviations:
        ref = references.VerseRef.from_str(f"{abbreviation} 1:1", language=LANGUAGE)

        assert (ref.book, ref.chapter, ref.verse) == (expected_book, 1, 1)
