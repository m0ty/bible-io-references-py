from typing import Dict, Iterable

from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ("창세기",),
    BibleBookEnum.Matthew: ("마태복음",),
    BibleBookEnum.John: ("요한복음",),
    BibleBookEnum.Revelation: ("요한계시록",),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Matthew: ("마",),
    BibleBookEnum.John: ("요",),
    BibleBookEnum.Revelation: ("계",),
}
