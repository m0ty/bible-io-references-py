from typing import Dict, Iterable

from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ("Genesis",),
    BibleBookEnum.Matthew: ("Mateo",),
    BibleBookEnum.John: ("Juan",),
    BibleBookEnum.Revelation: ("Pahayag",),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Matthew: ("mat",),
    BibleBookEnum.John: ("juan",),
    BibleBookEnum.Revelation: ("pah",),
}
