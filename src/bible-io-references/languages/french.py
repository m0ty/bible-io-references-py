from typing import Dict, Iterable

from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ("Genèse", "Genese"),
    BibleBookEnum.Matthew: ("Matthieu",),
    BibleBookEnum.John: ("Jean",),
    BibleBookEnum.Revelation: ("Apocalypse",),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Matthew: ("mat",),
    BibleBookEnum.John: ("jean",),
    BibleBookEnum.Revelation: ("ap", "apo"),
}
