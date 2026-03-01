from typing import Dict, Iterable

from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ("Kejadian",),
    BibleBookEnum.Matthew: ("Matius",),
    BibleBookEnum.John: ("Yohanes",),
    BibleBookEnum.Revelation: ("Wahyu",),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Matthew: ("mat",),
    BibleBookEnum.John: ("yoh",),
    BibleBookEnum.Revelation: ("why",),
}
