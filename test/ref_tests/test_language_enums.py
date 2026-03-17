import pytest

from src.bible_io_references import BibleBookEnum, BibleLanguageEnum, VerseRef
from src.bible_io_references.references import ParseVerseRefError


def test_language_enum_uses_human_readable_string_values():
    assert BibleLanguageEnum.SPANISH.value == "Spanish"
    assert str(BibleLanguageEnum.SPANISH) == "Spanish"
    assert BibleLanguageEnum.SPANISH.code == "es"
    assert BibleLanguageEnum.SPANISH.identifier_prefix == "spa"


@pytest.mark.parametrize(
    ("raw_value", "expected"),
    [
        ("Auto", BibleLanguageEnum.AUTO),
        ("all", BibleLanguageEnum.AUTO),
        ("Arabic", BibleLanguageEnum.ARABIC),
        ("arb", BibleLanguageEnum.ARABIC),
        ("arb-svd-1865", BibleLanguageEnum.ARABIC),
        ("English", BibleLanguageEnum.ENGLISH),
        ("eng", BibleLanguageEnum.ENGLISH),
        ("eng-kjv-1769", BibleLanguageEnum.ENGLISH),
        ("Spanish", BibleLanguageEnum.SPANISH),
        ("es", BibleLanguageEnum.SPANISH),
        ("spa", BibleLanguageEnum.SPANISH),
        ("spa-rva-1602", BibleLanguageEnum.SPANISH),
        ("Tagalog", BibleLanguageEnum.TAGALOG),
        ("fil", BibleLanguageEnum.TAGALOG),
        ("Vietnamese", BibleLanguageEnum.VIETNAMESE),
    ],
)
def test_language_enum_from_str_accepts_names_codes_and_bible_io_json_identifiers(
    raw_value: str,
    expected: BibleLanguageEnum,
):
    assert BibleLanguageEnum.from_str(raw_value) == expected


def test_parse_reference_accepts_language_display_name():
    ref = VerseRef.from_str("Juan 3:16", language="Spanish")

    assert ref.book == BibleBookEnum.John


def test_parse_reference_accepts_explicit_english_language():
    ref = VerseRef.from_str("John 3:16", language="English")

    assert ref.book == BibleBookEnum.John


def test_parse_reference_rejects_enum_languages_without_localized_term_tables():
    with pytest.raises(ParseVerseRefError) as exc_info:
        VerseRef.from_str("John 3:16", language="Vietnamese")

    assert exc_info.value.code == "unsupported_language"
