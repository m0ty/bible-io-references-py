import importlib

references = importlib.import_module("bible-io-references.references")
books = importlib.import_module("bible-io-references.bible_book_enums")


def test_parse_spanish_reference():
    ref = references.VerseRef.from_str("Juan 3:16")

    assert ref.book == books.BibleBookEnum.John
    assert ref.chapter == 3
    assert ref.verse == 16


def test_parse_spanish_abbreviated_reference():
    ref = references.VerseRef.from_str("Mat. 5:9")

    assert ref.book == books.BibleBookEnum.Matthew
    assert ref.chapter == 5
    assert ref.verse == 9
