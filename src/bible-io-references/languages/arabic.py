from typing import Dict, Iterable

from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ("التكوين",),
    BibleBookEnum.Matthew: ("متى",),
    BibleBookEnum.John: ("يوحنا",),
    BibleBookEnum.Revelation: ("الرؤيا",),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Matthew: ("مت",),
    BibleBookEnum.John: ("يو",),
    BibleBookEnum.Revelation: ("رؤ",),
}
