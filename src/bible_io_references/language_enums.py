from enum import Enum


class BibleLanguageEnum(Enum):
    """Supported languages for localized parsing."""

    AUTO = "auto"
    ARABIC = "ar"
    CHINESE = "zh"
    FRENCH = "fr"
    GERMAN = "de"
    HEBREW = "he"
    HINDI = "hi"
    INDONESIAN = "id"
    KOREAN = "ko"
    PORTUGUESE = "pt"
    RUSSIAN = "ru"
    SPANISH = "es"
    TAGALOG = "tl"

    def __str__(self) -> str:
        return self.value

    @property
    def code(self) -> str:
        return self.value

    @classmethod
    def from_str(cls, value: str) -> "BibleLanguageEnum":
        if not isinstance(value, str) or not value.strip():
            raise ValueError("language must be a non-empty string")
        normalized = value.strip().casefold()
        if normalized in {"auto", "global", "all"}:
            return cls.AUTO
        for lang in cls:
            if lang.value == normalized:
                return lang
        for lang in cls:
            if lang.name.casefold() == normalized:
                return lang
        raise ValueError(f"unknown language: {value!r}")
