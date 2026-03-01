from typing import Dict, Iterable

from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ("创世记", "創世記"),
    BibleBookEnum.Matthew: ("马太福音", "馬太福音"),
    BibleBookEnum.John: ("约翰福音", "約翰福音"),
    BibleBookEnum.Revelation: ("启示录", "啟示錄"),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Matthew: ("太",),
    BibleBookEnum.John: ("约", "約"),
    BibleBookEnum.Revelation: ("启", "啟"),
}
