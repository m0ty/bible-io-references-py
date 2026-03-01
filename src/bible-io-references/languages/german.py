from typing import Dict, Iterable

from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ("1. Mose", "Genesis"),
    BibleBookEnum.Matthew: ("Matthäus", "Matthaus"),
    BibleBookEnum.John: ("Johannes",),
    BibleBookEnum.Revelation: ("Offenbarung",),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Matthew: ("mt",),
    BibleBookEnum.John: ("joh",),
    BibleBookEnum.Revelation: ("offb",),
}
