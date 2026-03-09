import pytest

from src.bible_io_references import (
    BibleBookEnum,
    BibleLanguageEnum,
    ParseVerseRefError,
    Reference,
    VerseRangeRef,
    VerseRef,
    parse_reference,
)


def test_public_api_re_exports_language_and_book_enums():
    assert BibleBookEnum.John.full_name == "John"
    assert BibleLanguageEnum.SPANISH.code == "es"


def test_parse_reference_returns_verse_ref_for_single_verse_input():
    parsed: Reference = parse_reference("John 3:16")

    assert isinstance(parsed, VerseRef)
    assert (parsed.book, parsed.chapter, parsed.verse) == (
        BibleBookEnum.John,
        3,
        16,
    )


def test_parse_reference_returns_verse_range_ref_for_range_input():
    parsed: Reference = parse_reference("John 3:16-17")

    assert isinstance(parsed, VerseRangeRef)
    assert (parsed.start.book, parsed.start.chapter, parsed.start.verse) == (
        BibleBookEnum.John,
        3,
        16,
    )
    assert (parsed.end.book, parsed.end.chapter, parsed.end.verse) == (
        BibleBookEnum.John,
        3,
        17,
    )


def test_parse_reference_accepts_language_enum_and_string_codes():
    parsed_by_enum = parse_reference("Juan 3:16", language=BibleLanguageEnum.SPANISH)
    parsed_by_code = parse_reference("Juan 3:16", language="es")

    assert isinstance(parsed_by_enum, VerseRef)
    assert isinstance(parsed_by_code, VerseRef)
    assert parsed_by_enum.book == BibleBookEnum.John
    assert parsed_by_code.book == BibleBookEnum.John


def test_parse_reference_raises_range_order_error_for_non_ascending_same_book_range():
    with pytest.raises(ParseVerseRefError) as exc_info:
        parse_reference("John 3:17-16")

    assert exc_info.value.code == "same_book_range_not_ascending"
