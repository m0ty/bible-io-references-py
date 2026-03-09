from typing import Dict, Iterable
from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ("Genesis",),
    BibleBookEnum.Exodus: ("Exodo",),
    BibleBookEnum.Leviticus: ("Levitico",),
    BibleBookEnum.Numbers: ("Mga Bilang",),
    BibleBookEnum.Deuteronomy: ("Deuteronomio",),

    BibleBookEnum.Joshua: ("Josue",),
    BibleBookEnum.Judges: ("Mga Hukom",),
    BibleBookEnum.Ruth: ("Ruth",),

    # Samuel, Kings, Chronicles with "Mga Hari/Mga Cronica"
    BibleBookEnum.FirstSamuel: ("1 Samuel",),
    BibleBookEnum.SecondSamuel: ("2 Samuel",),
    BibleBookEnum.FirstKings: ("1 Mga Hari",),
    BibleBookEnum.SecondKings: ("2 Mga Hari",),

    BibleBookEnum.FirstChronicles: ("1 Mga Cronica",),
    BibleBookEnum.SecondChronicles: ("2 Mga Cronica",),

    BibleBookEnum.Ezra: ("Ezra",),
    BibleBookEnum.Nehemiah: ("Nehemias",),
    BibleBookEnum.Esther: ("Ester",),
    BibleBookEnum.Job: ("Job",),

    # Psalms, Proverbs, Ecclesiastes, Song of Solomon
    BibleBookEnum.Psalms: ("Mga Awit",),
    BibleBookEnum.Proverbs: ("Mga Kawikaan",),
    BibleBookEnum.Ecclesiastes: ("Ang Mangangaral",),
    BibleBookEnum.SongOfSolomon: ("Awit ni Solomon",),

    BibleBookEnum.Isaiah: ("Isaias",),
    BibleBookEnum.Jeremiah: ("Jeremias",),
    BibleBookEnum.Lamentations: ("Mga Panaghoy",),   # Aklat ng mga Panaghoy
    BibleBookEnum.Ezekiel: ("Ezekiel",),
    BibleBookEnum.Daniel: ("Daniel",),

    BibleBookEnum.Hosea: ("Oseas",),
    BibleBookEnum.Joel: ("Joel",),
    BibleBookEnum.Amos: ("Amos",),
    BibleBookEnum.Obadiah: ("Obadias",),
    BibleBookEnum.Jonah: ("Jonas",),
    BibleBookEnum.Micah: ("Mikas",),
    BibleBookEnum.Nahum: ("Nahum",),
    BibleBookEnum.Habakkuk: ("Habacuc",),
    BibleBookEnum.Zephaniah: ("Zefanias",),
    BibleBookEnum.Haggai: ("Hagai",),
    BibleBookEnum.Zechariah: ("Zacarias",),
    BibleBookEnum.Malachi: ("Malakias",),

    BibleBookEnum.Matthew: ("Mateo",),
    BibleBookEnum.Mark: ("Marcos",),
    BibleBookEnum.Luke: ("Lucas",),
    BibleBookEnum.John: ("Juan",),
    BibleBookEnum.Acts: ("Mga Gawa",),

    # Epistles with "Mga Taga-"
    BibleBookEnum.Romans: ("Mga Taga-Roma",),
    BibleBookEnum.FirstCorinthians: ("1 Mga Taga-Corinto",),
    BibleBookEnum.SecondCorinthians: ("2 Mga Taga-Corinto",),
    BibleBookEnum.Galatians: ("Mga Taga-Galacia",),
    BibleBookEnum.Ephesians: ("Mga Taga-Efeso",),
    BibleBookEnum.Philippians: ("Mga Taga-Filipos",),
    BibleBookEnum.Colossians: ("Mga Taga-Colosas",),
    BibleBookEnum.FirstThessalonians: ("1 Mga Taga-Tesalonica",),
    BibleBookEnum.SecondThessalonians: ("2 Mga Taga-Tesalonica",),

    BibleBookEnum.FirstTimothy: ("1 Timoteo",),
    BibleBookEnum.SecondTimothy: ("2 Timoteo",),
    BibleBookEnum.Titus: ("Tito",),
    BibleBookEnum.Philemon: ("Filemon",),
    BibleBookEnum.Hebrews: ("Mga Hebreo",),

    BibleBookEnum.James: ("Santiago",),
    BibleBookEnum.FirstPeter: ("1 Pedro",),
    BibleBookEnum.SecondPeter: ("2 Pedro",),
    BibleBookEnum.FirstJohn: ("1 Juan",),
    BibleBookEnum.SecondJohn: ("2 Juan",),
    BibleBookEnum.ThirdJohn: ("3 Juan",),
    BibleBookEnum.Jude: ("Judas",),
    BibleBookEnum.Revelation: ("Pahayag",),

    # Deuterocanon / Apocrypha (common Tagalog titles):
    BibleBookEnum.Tobit: ("Tobit",),               # also "Aklat ni Tobias"
    BibleBookEnum.Judith: ("Judit",),             # Spanish/Tagalog form
    BibleBookEnum.Wisdom: ("Karunungan ni Solomon",),
    BibleBookEnum.Sirach: ("Sirach",),            # or "Si Sirac"
    BibleBookEnum.Baruch: ("Baruc",),
    BibleBookEnum.FirstMaccabees: ("1 Macabeo",),
    BibleBookEnum.SecondMaccabees: ("2 Macabeo",),
    BibleBookEnum.ThirdMaccabees: ("3 Macabeo",),
    BibleBookEnum.FourthMaccabees: ("4 Macabeo",),

    # Additions:
    BibleBookEnum.EstherAdditions: ("Ester (Griyego)",),
    BibleBookEnum.DanielSongOfThree: ("Daniel (Awit ng Tatlong Kabataan)",),
    BibleBookEnum.DanielSusanna: ("Daniel (Susana)",),
    BibleBookEnum.DanielBelAndTheDragon: ("Daniel (Bel at ang Dragon)",),

    BibleBookEnum.FirstEsdras: ("1 Esdras",),
    BibleBookEnum.SecondEsdras: ("2 Esdras",),
    BibleBookEnum.PrayerOfManasseh: ("Panalangin ni Manases",),
    BibleBookEnum.Psalm151: ("Awit 151",),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    # Canonical books (using standard USFM-like codes)
    BibleBookEnum.Genesis: ("gn", "Gn", "GEN"),
    BibleBookEnum.Exodus: ("ex", "Exo", "EXO"),
    BibleBookEnum.Leviticus: ("lv", "Lev", "LEV"),
    BibleBookEnum.Numbers: ("nm", "Nm", "NUM"),
    BibleBookEnum.Deuteronomy: ("dt", "Deut", "DEU"),

    BibleBookEnum.Joshua: ("js", "Jos", "JOS"),
    BibleBookEnum.Judges: ("jud", "Jue", "JDG"),
    BibleBookEnum.Ruth: ("rt", "Rut", "RUT"),

    BibleBookEnum.FirstSamuel: ("1sm", "1Sm", "1SA", "1Sam"),
    BibleBookEnum.SecondSamuel: ("2sm", "2Sm", "2SA", "2Sam"),

    BibleBookEnum.FirstKings: ("1kg", "1Kg", "1Kgs", "1KI"),
    BibleBookEnum.SecondKings: ("2kg", "2Kg", "2Kgs", "2KI"),

    BibleBookEnum.FirstChronicles: ("1ch", "1Ch", "1CH"),
    BibleBookEnum.SecondChronicles: ("2ch", "2Ch", "2CH"),

    BibleBookEnum.Ezra: ("ezr", "Ezr", "EZR"),
    BibleBookEnum.Nehemiah: ("neh", "Neh", "NEH"),
    BibleBookEnum.Esther: ("est", "Est", "EST"),
    BibleBookEnum.Job: ("job", "Job"),
    BibleBookEnum.Psalms: ("ps", "Sal", "SAL"),
    BibleBookEnum.Proverbs: ("prv", "Prv", "PRO"),
    BibleBookEnum.Ecclesiastes: ("ec", "Eccl", "ECC"),
    BibleBookEnum.SongOfSolomon: ("song", "Cant", "CNT"),

    BibleBookEnum.Isaiah: ("is", "Isa", "ISA"),
    BibleBookEnum.Jeremiah: ("jr", "Jer", "JER"),
    BibleBookEnum.Lamentations: ("lm", "Lam", "LAM"),
    BibleBookEnum.Ezekiel: ("ez", "Eze", "EZK"),
    BibleBookEnum.Daniel: ("dn", "Dan", "DAN"),

    BibleBookEnum.Hosea: ("hos", "Hos", "HOS"),
    BibleBookEnum.Joel: ("jl", "Joel", "JOL"),
    BibleBookEnum.Amos: ("amo", "Amos", "AMO"),
    BibleBookEnum.Obadiah: ("oba", "Oba", "OBA"),
    BibleBookEnum.Jonah: ("jon", "Jon", "JON"),
    BibleBookEnum.Micah: ("mic", "Mic", "MIC"),
    BibleBookEnum.Nahum: ("nah", "Nah", "NAH"),
    BibleBookEnum.Habakkuk: ("hab", "Hab", "HAB"),
    BibleBookEnum.Zephaniah: ("zep", "Zep", "ZEP"),
    BibleBookEnum.Haggai: ("hag", "Hag", "HAG"),
    BibleBookEnum.Zechariah: ("zec", "Zec", "ZEC"),
    BibleBookEnum.Malachi: ("mal", "Mal", "MAL"),

    BibleBookEnum.Matthew: ("mat", "Mat", "MAT"),
    BibleBookEnum.Mark: ("mrk", "Mrk", "MRK"),
    BibleBookEnum.Luke: ("luk", "Luk", "LUK"),
    BibleBookEnum.John: ("jn", "Jn", "JOH"),
    BibleBookEnum.Acts: ("act", "Acts", "ACT"),

    BibleBookEnum.Romans: ("rm", "Ro", "ROM"),
    BibleBookEnum.FirstCorinthians: ("1co", "1Co", "1CO"),
    BibleBookEnum.SecondCorinthians: ("2co", "2Co", "2CO"),
    BibleBookEnum.Galatians: ("gl", "Gal", "GAL"),
    BibleBookEnum.Ephesians: ("eph", "Eph", "EPH"),
    BibleBookEnum.Philippians: ("php", "Php", "PHP"),
    BibleBookEnum.Colossians: ("col", "Col", "COL"),
    BibleBookEnum.FirstThessalonians: ("1th", "1Ts", "1TH"),
    BibleBookEnum.SecondThessalonians: ("2th", "2Ts", "2TH"),
    BibleBookEnum.FirstTimothy: ("1ti", "1Tm", "1TI"),
    BibleBookEnum.SecondTimothy: ("2ti", "2Tm", "2TI"),
    BibleBookEnum.Titus: ("tit", "Tit"),
    BibleBookEnum.Philemon: ("phm", "Phm"),
    BibleBookEnum.Hebrews: ("heb", "Heb", "HEB"),

    BibleBookEnum.James: ("jas", "Jas", "JAS"),
    BibleBookEnum.FirstPeter: ("1pe", "1Pe", "1PT"),
    BibleBookEnum.SecondPeter: ("2pe", "2Pe", "2PT"),
    BibleBookEnum.FirstJohn: ("1jn", "1Jn", "1JO"),
    BibleBookEnum.SecondJohn: ("2jn", "2Jn", "2JO"),
    BibleBookEnum.ThirdJohn: ("3jn", "3Jn", "3JO"),
    BibleBookEnum.Jude: ("jd", "Jude"),
    BibleBookEnum.Revelation: ("rev", "Ap", "APO", "Pah"),

    # Deuterocanonical / Apocrypha
    BibleBookEnum.Tobit: ("tb", "Tob", "TOB"),
    BibleBookEnum.Judith: ("jdt", "JDT"),
    BibleBookEnum.Wisdom: ("wis", "Sab", "SAB"),
    BibleBookEnum.Sirach: ("sir", "SIR", "Eclo"),
    BibleBookEnum.Baruch: ("bar", "Bar", "BAR"),
    BibleBookEnum.FirstMaccabees: ("1mc", "1Mc", "1MA"),
    BibleBookEnum.SecondMaccabees: ("2mc", "2Mc", "2MA"),
    BibleBookEnum.ThirdMaccabees: ("3mc", "3Mc", "3MA"),
    BibleBookEnum.FourthMaccabees: ("4mc", "4Mc", "4MA"),

    BibleBookEnum.EstherAdditions: ("esg", "ESG", "EsthGr"),
    BibleBookEnum.DanielSongOfThree: ("s3y", "S3Y", "PrAzar"),
    BibleBookEnum.DanielSusanna: ("sus", "SUS"),
    BibleBookEnum.DanielBelAndTheDragon: ("bel", "BEL"),
    BibleBookEnum.FirstEsdras: ("1es", "1Es", "1ES"),
    BibleBookEnum.SecondEsdras: ("2es", "2Es", "2ES"),
    BibleBookEnum.PrayerOfManasseh: ("man", "Man", "MAN"),
    BibleBookEnum.Psalm151: ("ps2", "PS2", "AddPs"),
}
