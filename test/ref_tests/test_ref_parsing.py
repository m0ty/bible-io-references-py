from dataclasses import FrozenInstanceError

import pytest

from src.bible_io_references.bible_book_enums import BibleBookEnum
from src.bible_io_references.references import (
    AUTO_LANGUAGE_COLLISIONS,
    AUTO_LANGUAGE_PRECEDENCE,
    ParseVerseRefError,
    VerseRangeRef,
    VerseRef,
)


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


def test_auto_language_collision_metadata_exposes_ambiguous_terms():
    assert AUTO_LANGUAGE_PRECEDENCE == (
        "ar",
        "zh",
        "fr",
        "de",
        "he",
        "hi",
        "id",
        "ko",
        "pt",
        "ru",
        "es",
        "tl",
    )

    assert "jn" in AUTO_LANGUAGE_COLLISIONS
    assert "jud" in AUTO_LANGUAGE_COLLISIONS

    jn_books = {book.name for book in AUTO_LANGUAGE_COLLISIONS["jn"]}
    assert jn_books == {"John", "Jonah"}


@pytest.mark.parametrize("reference", ["NotABook 3:16"])
def test_parse_invalid_reference_raises_parse_error(reference):
    with pytest.raises(ParseVerseRefError):
        VerseRef.from_str(reference)


@pytest.mark.parametrize("reference", ["John 0:1", "John 1:0", "John -1:1", "John 1:-1"])
def test_parse_non_positive_single_verse_components_raise_parse_error(reference):
    with pytest.raises(ParseVerseRefError):
        VerseRef.from_str(reference)


def test_parse_error_includes_machine_readable_diagnostics():
    with pytest.raises(ParseVerseRefError) as exc_info:
        VerseRef.from_str("NotABook 3:16")

    exc = exc_info.value
    assert str(exc) == "invalid verse reference"
    assert exc.code == "unknown_book"
    assert exc.details is not None
    assert exc.to_dict()["code"] == "unknown_book"


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
            "John 3:16\u201317",
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


@pytest.mark.parametrize(
    "reference",
    ["John 0:1-2", "John 1:0-2", "John 1:1-0", "John -1:1-2", "John 1:-1-2"],
)
def test_parse_non_positive_verse_range_components_raise_parse_error(reference):
    with pytest.raises(ParseVerseRefError):
        VerseRangeRef.from_str(reference)


@pytest.mark.parametrize("reference", ["John 3:17-16", "John 3:16-3:16", "John 3:16-John 3:16"])
def test_same_book_range_requires_end_after_start(reference):
    with pytest.raises(ParseVerseRefError) as exc_info:
        VerseRangeRef.from_str(reference)

    assert exc_info.value.code == "same_book_range_not_ascending"


def test_references_are_immutable_value_objects():
    ref = VerseRef.from_str("John 3:16")
    rng = VerseRangeRef.from_str("John 3:16-17")

    with pytest.raises(FrozenInstanceError):
        ref.chapter = 4

    with pytest.raises(FrozenInstanceError):
        rng.end = ref


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
