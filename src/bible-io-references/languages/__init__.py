from typing import Dict, Iterable

from ..bible_book_enums import BibleBookEnum
from . import (
    arabic,
    chinese,
    french,
    german,
    hebrew,
    hindi,
    indonesian,
    korean,
    portuguese,
    russian,
    spanish,
    tagalog,
)

BOOK_NAMES_BY_LANGUAGE: Dict[str, Dict[BibleBookEnum, Iterable[str]]] = {
    "ru": russian.BOOK_NAMES,
    "he": hebrew.BOOK_NAMES,
    "es": spanish.BOOK_NAMES,
    "pt": portuguese.BOOK_NAMES,
    "fr": french.BOOK_NAMES,
    "de": german.BOOK_NAMES,
    "zh": chinese.BOOK_NAMES,
    "ko": korean.BOOK_NAMES,
    "tl": tagalog.BOOK_NAMES,
    "id": indonesian.BOOK_NAMES,
    "ar": arabic.BOOK_NAMES,
    "hi": hindi.BOOK_NAMES,
}

BOOK_ABBREVIATIONS_BY_LANGUAGE: Dict[str, Dict[BibleBookEnum, Iterable[str]]] = {
    "ru": russian.BOOK_ABBREVIATIONS,
    "he": hebrew.BOOK_ABBREVIATIONS,
    "es": spanish.BOOK_ABBREVIATIONS,
    "pt": portuguese.BOOK_ABBREVIATIONS,
    "fr": french.BOOK_ABBREVIATIONS,
    "de": german.BOOK_ABBREVIATIONS,
    "zh": chinese.BOOK_ABBREVIATIONS,
    "ko": korean.BOOK_ABBREVIATIONS,
    "tl": tagalog.BOOK_ABBREVIATIONS,
    "id": indonesian.BOOK_ABBREVIATIONS,
    "ar": arabic.BOOK_ABBREVIATIONS,
    "hi": hindi.BOOK_ABBREVIATIONS,
}
