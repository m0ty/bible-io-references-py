from enum import Enum


class BibleLanguageEnum(Enum):
    """Supported languages for localized parsing."""

    _code: str
    _identifier_prefix: str
    _aliases: tuple[str, ...]

    def __new__(
        cls,
        display_name: str,
        code: str,
        identifier_prefix: str,
        *aliases: str,
    ) -> "BibleLanguageEnum":
        obj = object.__new__(cls)
        obj._value_ = display_name
        obj._code = code
        obj._identifier_prefix = identifier_prefix
        obj._aliases = tuple(alias.casefold() for alias in aliases)
        return obj

    AUTO = ("Auto", "auto", "auto", "all", "global")
    ARABIC = ("Arabic", "ar", "arb")
    CHINESE = ("Chinese", "zh", "zho")
    ENGLISH = ("English", "en", "eng")
    ESPERANTO = ("Esperanto", "eo", "epo")
    FINNISH = ("Finnish", "fi", "fin")
    FRENCH = ("French", "fr", "fra")
    GERMAN = ("German", "de", "deu")
    GREEK = ("Greek", "el", "ell")
    HEBREW = ("Hebrew", "he", "heb")
    HINDI = ("Hindi", "hi", "hin")
    INDONESIAN = ("Indonesian", "id", "ind")
    KOREAN = ("Korean", "ko", "kor")
    PORTUGUESE = ("Portuguese", "pt", "por")
    ROMANIAN = ("Romanian", "ro", "ron")
    RUSSIAN = ("Russian", "ru", "rus")
    SPANISH = ("Spanish", "es", "spa")
    TAGALOG = ("Tagalog", "tl", "tgl", "fil")
    VIETNAMESE = ("Vietnamese", "vi", "vie")

    def __str__(self) -> str:
        return self.value

    @property
    def code(self) -> str:
        return self._code

    @property
    def identifier_prefix(self) -> str:
        return self._identifier_prefix

    @property
    def aliases(self) -> tuple[str, ...]:
        return (
            self.name.casefold(),
            self.value.casefold(),
            self.code.casefold(),
            self.identifier_prefix.casefold(),
            *self._aliases,
        )

    @classmethod
    def from_str(cls, value: str) -> "BibleLanguageEnum":
        if not isinstance(value, str) or not value.strip():
            raise ValueError("language must be a non-empty string")
        normalized = value.strip().casefold()
        identifier_prefix = normalized.split("-", 1)[0]
        for lang in cls:
            if normalized in lang.aliases or identifier_prefix in lang.aliases:
                return lang
        raise ValueError(f"unknown language: {value!r}")
