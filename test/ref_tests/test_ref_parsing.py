import importlib

references = importlib.import_module("bible-io-references.references")
books = importlib.import_module("bible-io-references.bible_book_enums")


def test_parse_standard_reference():
    ref = references.VerseRef.from_str("John 3:16")

    assert ref.book == books.BibleBookEnum.John
    assert ref.chapter == 3
    assert ref.verse == 16


def test_parse_with_book_abbreviation():
    ref = references.VerseRef.from_str("jo 1:1")

    assert ref.book == books.BibleBookEnum.John
    assert ref.chapter == 1
    assert ref.verse == 1


def test_parse_invalid_reference_raises_parse_error():
    try:
        references.VerseRef.from_str("NotABook 3:16")
    except references.ParseVerseRefError:
        pass
    else:
        raise AssertionError("expected ParseVerseRefError")
