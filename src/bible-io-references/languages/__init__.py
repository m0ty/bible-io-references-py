from typing import Dict, Iterable

from ..bible_book_enums import BibleBookEnum
from . import es, he, pt, ru

BOOK_NAMES_BY_LANGUAGE: Dict[str, Dict[BibleBookEnum, Iterable[str]]] = {
    "ru": ru.BOOK_NAMES,
    "he": he.BOOK_NAMES,
    "es": es.BOOK_NAMES,
    "pt": pt.BOOK_NAMES,
}

BOOK_ABBREVIATIONS_BY_LANGUAGE: Dict[str, Dict[BibleBookEnum, Iterable[str]]] = {
    "ru": ru.BOOK_ABBREVIATIONS,
    "he": he.BOOK_ABBREVIATIONS,
    "es": es.BOOK_ABBREVIATIONS,
    "pt": pt.BOOK_ABBREVIATIONS,
}
