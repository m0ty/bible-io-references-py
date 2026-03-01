from typing import Dict, Iterable

from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ("Gênesis",),
    BibleBookEnum.Exodus: ("Êxodo",),
    BibleBookEnum.Leviticus: ("Levítico",),
    BibleBookEnum.Numbers: ("Números",),
    BibleBookEnum.Deuteronomy: ("Deuteronômio",),
    BibleBookEnum.Proverbs: ("Provérbios",),
    BibleBookEnum.Matthew: ("Mateus",),
    BibleBookEnum.John: ("João", "Joao"),
    BibleBookEnum.Acts: ("Atos",),
    BibleBookEnum.FirstCorinthians: ("1 Coríntios",),
    BibleBookEnum.SecondCorinthians: ("2 Coríntios",),
    BibleBookEnum.Ephesians: ("Efésios",),
    BibleBookEnum.Colossians: ("Colossenses",),
    BibleBookEnum.FirstTimothy: ("1 Timóteo",),
    BibleBookEnum.SecondTimothy: ("2 Timóteo",),
    BibleBookEnum.Philemon: ("Filemom",),
    BibleBookEnum.Hebrews: ("Hebreus",),
    BibleBookEnum.James: ("Tiago",),
    BibleBookEnum.FirstJohn: ("1 João", "1 Joao"),
    BibleBookEnum.SecondJohn: ("2 João", "2 Joao"),
    BibleBookEnum.ThirdJohn: ("3 João", "3 Joao"),
    BibleBookEnum.Revelation: ("Apocalipse",),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.John: ("joao",),
    BibleBookEnum.Revelation: ("apoc",),
}
