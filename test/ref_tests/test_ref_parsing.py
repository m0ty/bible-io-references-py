import pytest
from bible_io_references.references import VerseRef, VerseRangeRef, ParseVerseRefError
from bible_io_references.bible_book_enums import BibleBookEnum


@pytest.mark.parametrize(
    "reference, expected",
    [
        ("John 3:16", (BibleBookEnum.John, 3, 16)),
        ("John 3.16", (BibleBookEnum.John, 3, 16)),
        ("jo 1:1", (BibleBookEnum.John, 1, 1)),
    ],
)
def test_parse_reference(reference, expected):
    ref = VerseRef.from_str(reference)

    assert (ref.book, ref.chapter, ref.verse) == expected


@pytest.mark.parametrize(
    "reference, expected_book",
    [
        ("jud 1:1", BibleBookEnum.Judges),
        ("so 1:1", BibleBookEnum.SongOfSolomon),
        ("jn 1:1", BibleBookEnum.Jonah),
    ],
)
def test_auto_language_prefers_english_abbreviations_on_collisions(
    reference, expected_book
):
    ref = VerseRef.from_str(reference)

    assert ref.book == expected_book


def test_auto_language_falls_back_to_non_english_terms():
    ref = VerseRef.from_str("Juan 1:1")

    assert ref.book == BibleBookEnum.John


@pytest.mark.parametrize("reference", ["NotABook 3:16"])
def test_parse_invalid_reference_raises_parse_error(reference):
    with pytest.raises(ParseVerseRefError):
        VerseRef.from_str(reference)


@pytest.mark.parametrize(
    "reference, expected",
    [
        (
            "John 3:16-17",
            (
                (BibleBookEnum.John, 3, 16),
                (BibleBookEnum.John, 3, 17),
            ),
        ),
        (
            "John 3:16–17",
            (
                (BibleBookEnum.John, 3, 16),
                (BibleBookEnum.John, 3, 17),
            ),
        ),
        (
            "John 3:16-4:1",
            (
                (BibleBookEnum.John, 3, 16),
                (BibleBookEnum.John, 4, 1),
            ),
        ),
        (
            "John 3.16-4.1",
            (
                (BibleBookEnum.John, 3, 16),
                (BibleBookEnum.John, 4, 1),
            ),
        ),
        (
            "John 3:16-Acts 1:2",
            (
                (BibleBookEnum.John, 3, 16),
                (BibleBookEnum.Acts, 1, 2),
            ),
        ),
    ],
)
def test_parse_verse_range(reference, expected):
    ref = VerseRangeRef.from_str(reference)

    assert (ref.start.book, ref.start.chapter, ref.start.verse) == expected[0]
    assert (ref.end.book, ref.end.chapter, ref.end.verse) == expected[1]


@pytest.mark.parametrize("reference", ["John 3:16", "John 3:16-0", "NotABook 3:16-17"])
def test_parse_invalid_verse_range_raises_parse_error(reference):
    with pytest.raises(ParseVerseRefError):
        VerseRangeRef.from_str(reference)


@pytest.mark.parametrize("book", list(BibleBookEnum))
def test_parse_all_books_with_colon_and_dot_separators(book):
    colon_ref = VerseRef.from_str(f"{book.full_name} 1:1")
    dot_ref = VerseRef.from_str(f"{book.full_name} 1.1")

    assert (colon_ref.book, colon_ref.chapter, colon_ref.verse) == (book, 1, 1)
    assert (dot_ref.book, dot_ref.chapter, dot_ref.verse) == (book, 1, 1)


@pytest.mark.parametrize("book", list(BibleBookEnum))
def test_parse_all_book_abbreviations_with_colon_and_dot_separators(book):
    colon_ref = VerseRef.from_str(f"{book.as_str()} 1:1")
    dot_ref = VerseRef.from_str(f"{book.as_str()} 1.1")

    assert (colon_ref.book, colon_ref.chapter, colon_ref.verse) == (book, 1, 1)
    assert (dot_ref.book, dot_ref.chapter, dot_ref.verse) == (book, 1, 1)
