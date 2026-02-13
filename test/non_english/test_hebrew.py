import importlib

references = importlib.import_module("bible-io-references.references")
books = importlib.import_module("bible-io-references.bible_book_enums")


def test_parse_hebrew_reference():
    ref = references.VerseRef.from_str("יוחנן 3:16")

    assert ref.book == books.BibleBookEnum.John
    assert ref.chapter == 3
    assert ref.verse == 16


def test_parse_hebrew_abbreviated_reference():
    ref = references.VerseRef.from_str("יוח 3:16")

    assert ref.book == books.BibleBookEnum.John
    assert ref.chapter == 3
    assert ref.verse == 16
