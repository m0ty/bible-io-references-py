from typing import Dict, Iterable

from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ("उत्पत्ति",),
    BibleBookEnum.Matthew: ("मत्ती",),
    BibleBookEnum.John: ("यूहन्ना",),
    BibleBookEnum.Revelation: ("प्रकाशितवाक्य",),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Matthew: ("मत",),
    BibleBookEnum.John: ("यूह",),
    BibleBookEnum.Revelation: ("प्रका",),
}
