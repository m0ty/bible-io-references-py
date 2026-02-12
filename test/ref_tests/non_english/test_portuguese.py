import importlib

references = importlib.import_module("bible-io-references.references")
books = importlib.import_module("bible-io-references.bible_book_enums")


def test_parse_portuguese_reference():
    ref = references.VerseRef.from_str("João 3:16")

    assert ref.book == books.BibleBookEnum.John
    assert ref.chapter == 3
    assert ref.verse == 16


def test_parse_portuguese_abbreviated_reference():
    ref = references.VerseRef.from_str("Apoc 21:4")

    assert ref.book == books.BibleBookEnum.Revelation
    assert ref.chapter == 21
    assert ref.verse == 4
