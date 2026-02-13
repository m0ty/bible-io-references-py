from typing import Dict, Iterable

from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ("Génesis", "Genesis"),
    BibleBookEnum.Exodus: ("Éxodo", "Exodo"),
    BibleBookEnum.Leviticus: ("Levítico", "Levitico"),
    BibleBookEnum.Numbers: ("Números", "Numeros"),
    BibleBookEnum.Deuteronomy: ("Deuteronomio",),
    BibleBookEnum.Psalms: ("Salmos",),
    BibleBookEnum.Proverbs: ("Proverbios",),
    BibleBookEnum.Isaiah: ("Isaías", "Isaias"),
    BibleBookEnum.Matthew: ("Mateo",),
    BibleBookEnum.Mark: ("Marcos",),
    BibleBookEnum.Luke: ("Lucas",),
    BibleBookEnum.John: ("Juan",),
    BibleBookEnum.Acts: ("Hechos",),
    BibleBookEnum.Romans: ("Romanos",),
    BibleBookEnum.FirstCorinthians: ("1 Corintios",),
    BibleBookEnum.SecondCorinthians: ("2 Corintios",),
    BibleBookEnum.Galatians: ("Gálatas", "Galatas"),
    BibleBookEnum.Ephesians: ("Efesios",),
    BibleBookEnum.Philippians: ("Filipenses",),
    BibleBookEnum.Colossians: ("Colosenses",),
    BibleBookEnum.FirstThessalonians: ("1 Tesalonicenses",),
    BibleBookEnum.SecondThessalonians: ("2 Tesalonicenses",),
    BibleBookEnum.FirstTimothy: ("1 Timoteo",),
    BibleBookEnum.SecondTimothy: ("2 Timoteo",),
    BibleBookEnum.Titus: ("Tito",),
    BibleBookEnum.Philemon: ("Filemón", "Filemon"),
    BibleBookEnum.Hebrews: ("Hebreos",),
    BibleBookEnum.James: ("Santiago",),
    BibleBookEnum.FirstPeter: ("1 Pedro",),
    BibleBookEnum.SecondPeter: ("2 Pedro",),
    BibleBookEnum.FirstJohn: ("1 Juan",),
    BibleBookEnum.SecondJohn: ("2 Juan",),
    BibleBookEnum.ThirdJohn: ("3 Juan",),
    BibleBookEnum.Jude: ("Judas",),
    BibleBookEnum.Revelation: ("Apocalipsis",),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Matthew: ("mat",),
    BibleBookEnum.Luke: ("luc",),
    BibleBookEnum.John: ("juan",),
    BibleBookEnum.Revelation: ("apoc",),
}
