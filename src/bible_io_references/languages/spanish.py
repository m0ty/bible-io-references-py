from typing import Dict, Iterable
from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ("Génesis", "Genesis"),
    BibleBookEnum.Exodus: ("Éxodo", "Exodo"),
    BibleBookEnum.Leviticus: ("Levítico", "Levitico"),
    BibleBookEnum.Numbers: ("Números", "Numeros"),
    BibleBookEnum.Deuteronomy: ("Deuteronomio",),

    BibleBookEnum.Joshua: ("Josué", "Josue"),
    BibleBookEnum.Judges: ("Jueces",),
    BibleBookEnum.Ruth: ("Rut",),

    BibleBookEnum.FirstSamuel: ("1 Samuel", "1º Samuel", "1° Samuel", "I Samuel"),
    BibleBookEnum.SecondSamuel: ("2 Samuel", "2º Samuel", "2° Samuel", "II Samuel"),
    BibleBookEnum.FirstKings: ("1 Reyes", "1º Reyes", "1° Reyes", "I Reyes"),
    BibleBookEnum.SecondKings: ("2 Reyes", "2º Reyes", "2° Reyes", "II Reyes"),

    BibleBookEnum.FirstChronicles: ("1 Crónicas", "1 Cronicas", "1º Crónicas", "1° Crónicas", "I Crónicas"),
    BibleBookEnum.SecondChronicles: ("2 Crónicas", "2 Cronicas", "2º Crónicas", "2° Crónicas", "II Crónicas"),

    # CEE uses Esdrás; many users type Esdras
    BibleBookEnum.Ezra: ("Esdrás", "Esdras", "Ezra"),
    BibleBookEnum.Nehemiah: ("Nehemías", "Nehemias"),
    # CEE uses Ester
    BibleBookEnum.Esther: ("Ester", "Esther"),

    BibleBookEnum.Job: ("Job",),
    BibleBookEnum.Psalms: ("Salmos", "Salmo"),
    BibleBookEnum.Proverbs: ("Proverbios",),
    BibleBookEnum.Ecclesiastes: ("Eclesiastés", "Eclesiastes", "Qohelet", "Qoélet", "Coelet"),
    BibleBookEnum.SongOfSolomon: (
        "Cantar de los cantares", "Cantar de los Cantares",
        "Cantares", "Cantar"
    ),

    BibleBookEnum.Isaiah: ("Isaías", "Isaias"),
    BibleBookEnum.Jeremiah: ("Jeremías", "Jeremias"),
    BibleBookEnum.Lamentations: ("Lamentaciones",),
    BibleBookEnum.Ezekiel: ("Ezequiel",),
    BibleBookEnum.Daniel: ("Daniel",),

    # CEE uses Oseas/Amós/Jonás/Abdías/Miqueas/Habacuc/Sofonías/Ageo etc.
    BibleBookEnum.Hosea: ("Oseas", "Hosea"),
    BibleBookEnum.Joel: ("Joel",),
    BibleBookEnum.Amos: ("Amós", "Amos"),
    BibleBookEnum.Obadiah: ("Abdías", "Abdias"),
    BibleBookEnum.Jonah: ("Jonás", "Jonas"),
    BibleBookEnum.Micah: ("Miqueas",),
    # CEE uses Nahún; many editions use Nahúm
    BibleBookEnum.Nahum: ("Nahún", "Nahun", "Nahúm", "Nahum"),
    BibleBookEnum.Habakkuk: ("Habacuc",),
    BibleBookEnum.Zephaniah: ("Sofonías", "Sofonias"),
    BibleBookEnum.Haggai: ("Ageo", "Hageo"),
    BibleBookEnum.Zechariah: ("Zacarías", "Zacarias"),
    BibleBookEnum.Malachi: ("Malaquías", "Malaquias"),

    BibleBookEnum.Matthew: ("Mateo",),
    BibleBookEnum.Mark: ("Marcos",),
    BibleBookEnum.Luke: ("Lucas",),
    BibleBookEnum.John: ("Juan",),

    BibleBookEnum.Acts: ("Hechos", "Hechos de los apóstoles", "Hechos de los Apóstoles"),
    BibleBookEnum.Romans: ("Romanos",),

    BibleBookEnum.FirstCorinthians: ("1 Corintios", "1º Corintios", "1° Corintios", "I Corintios"),
    BibleBookEnum.SecondCorinthians: ("2 Corintios", "2º Corintios", "2° Corintios", "II Corintios"),

    BibleBookEnum.Galatians: ("Gálatas", "Galatas"),
    BibleBookEnum.Ephesians: ("Efesios",),
    BibleBookEnum.Philippians: ("Filipenses",),
    BibleBookEnum.Colossians: ("Colosenses",),

    BibleBookEnum.FirstThessalonians: ("1 Tesalonicenses", "1º Tesalonicenses", "1° Tesalonicenses"),
    BibleBookEnum.SecondThessalonians: ("2 Tesalonicenses", "2º Tesalonicenses", "2° Tesalonicenses"),

    BibleBookEnum.FirstTimothy: ("1 Timoteo", "1º Timoteo", "1° Timoteo"),
    BibleBookEnum.SecondTimothy: ("2 Timoteo", "2º Timoteo", "2° Timoteo"),

    BibleBookEnum.Titus: ("Tito",),
    BibleBookEnum.Philemon: ("Filemón", "Filemon"),
    BibleBookEnum.Hebrews: ("Hebreos",),
    BibleBookEnum.James: ("Santiago", "Jacobo"),
    BibleBookEnum.FirstPeter: ("1 Pedro", "1º Pedro", "1° Pedro"),
    BibleBookEnum.SecondPeter: ("2 Pedro", "2º Pedro", "2° Pedro"),
    BibleBookEnum.FirstJohn: ("1 Juan", "1º Juan", "1° Juan"),
    BibleBookEnum.SecondJohn: ("2 Juan", "2º Juan", "2° Juan"),
    BibleBookEnum.ThirdJohn: ("3 Juan", "3º Juan", "3° Juan"),
    BibleBookEnum.Jude: ("Judas",),
    BibleBookEnum.Revelation: ("Apocalipsis", "Apocalipsis de Juan"),

    # Deuterocanon: CEE uses Tobías/Judit/Sabiduría/Eclesiástico/Baruc/1–2 Macabeos
    BibleBookEnum.Tobit: ("Tobías", "Tobias", "Tobit"),
    BibleBookEnum.Judith: ("Judit", "Judith"),
    BibleBookEnum.Wisdom: ("Sabiduría", "Sabiduria", "Sabiduría de Salomón", "Sabiduria de Salomon"),
    BibleBookEnum.Sirach: ("Eclesiástico", "Eclesiastico", "Sirácida", "Siracida"),
    BibleBookEnum.Baruch: ("Baruc", "Baruch"),
    BibleBookEnum.FirstMaccabees: ("1 Macabeos", "1º Macabeos", "1° Macabeos"),
    BibleBookEnum.SecondMaccabees: ("2 Macabeos", "2º Macabeos", "2° Macabeos"),
    BibleBookEnum.ThirdMaccabees: ("3 Macabeos", "3º Macabeos", "3° Macabeos"),
    BibleBookEnum.FourthMaccabees: ("4 Macabeos", "4º Macabeos", "4° Macabeos"),

    # Additions/extras (names vary; keep descriptive Spanish)
    BibleBookEnum.EstherAdditions: ("Ester (griego)", "Ester (Griego)", "Ester griego"),
    BibleBookEnum.DanielSongOfThree: (
        "Oración de Azarías", "Oracion de Azarias",
        "Cántico de los tres jóvenes", "Cantico de los tres jovenes",
        "Oración de Azarías y el Cántico de los tres jóvenes",
        "Oracion de Azarias y el Cantico de los tres jovenes",
    ),
    BibleBookEnum.DanielSusanna: ("Susana",),
    BibleBookEnum.DanielBelAndTheDragon: ("Bel y el dragón", "Bel y el dragon", "Bel y la serpiente"),

    BibleBookEnum.FirstEsdras: ("1 Esdras",),
    BibleBookEnum.SecondEsdras: ("2 Esdras",),

    BibleBookEnum.PrayerOfManasseh: ("Oración de Manasés", "Oracion de Manases"),
    BibleBookEnum.Psalm151: ("Salmo 151",),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    # OT / Canon común
    BibleBookEnum.Genesis: ("Gn", "gn", "Gén", "gen", "GEN"),
    BibleBookEnum.Exodus: ("Ex", "ex", "Éx", "Exod", "EXO"),
    BibleBookEnum.Leviticus: ("Lv", "lv", "Lev", "LEV"),
    BibleBookEnum.Numbers: ("Nm", "nm", "Núm", "Num", "NUM"),
    BibleBookEnum.Deuteronomy: ("Dt", "dt", "Deut", "DEU"),

    BibleBookEnum.Joshua: ("Jos", "jos", "JOS"),
    BibleBookEnum.Judges: ("Jue", "jue", "Jc", "jc", "JDG"),
    BibleBookEnum.Ruth: ("Rt", "rt", "Rut", "rut", "RUT"),

    # Spaced + unspaced numeric forms
    BibleBookEnum.FirstSamuel: ("1S", "1 S", "1Sam", "1 Sam", "1Sm", "1 Sm", "1SA"),
    BibleBookEnum.SecondSamuel: ("2S", "2 S", "2Sam", "2 Sam", "2Sm", "2 Sm", "2SA"),

    BibleBookEnum.FirstKings: ("1R", "1 R", "1Re", "1 Re", "1Rey", "1 Rey", "1KI", "1Kgs"),
    BibleBookEnum.SecondKings: ("2R", "2 R", "2Re", "2 Re", "2Rey", "2 Rey", "2KI", "2Kgs"),

    BibleBookEnum.FirstChronicles: ("1Cr", "1 Cr", "1Cro", "1 Cro", "1CH", "1Chr"),
    BibleBookEnum.SecondChronicles: ("2Cr", "2 Cr", "2Cro", "2 Cro", "2CH", "2Chr"),

    # Spanish canonical Ezra is Esdras → Esd is safest (avoid 'Es' collision)
    BibleBookEnum.Ezra: ("Esd", "esd", "EZR", "Ezr"),
    BibleBookEnum.Nehemiah: ("Neh", "neh", "Ne", "ne", "NEH"),
    BibleBookEnum.Esther: ("Est", "est", "EST"),

    BibleBookEnum.Job: ("Job", "job", "Jb", "jb", "JOB"),
    BibleBookEnum.Psalms: ("Sal", "sal", "Sl", "sl", "PSA", "Ps"),
    BibleBookEnum.Proverbs: ("Pr", "pr", "Prov", "prov", "PRO"),
    # Ecclesiastes: BIBLIJA.net: Ec/Qo ; many also use Ecl — keep but rely on longest-match (Eclo for Sirach)
    BibleBookEnum.Ecclesiastes: ("Ec", "ec", "Qo", "qo", "Ecl", "ecl", "ECC", "Eccl"),
    BibleBookEnum.SongOfSolomon: ("Cnt", "cnt", "Ct", "ct", "Cant", "cant", "SNG", "Song"),

    BibleBookEnum.Isaiah: ("Is", "is", "ISA", "Isa"),
    BibleBookEnum.Jeremiah: ("Jer", "jer", "Jr", "jr", "JER"),
    BibleBookEnum.Lamentations: ("Lm", "lm", "LAM", "Lam"),
    # Ezequiel commonly abbreviated Ez in Spanish tables; avoid using Ezr for Ezra
    BibleBookEnum.Ezekiel: ("Ez", "ez", "Ezeq", "ezeq", "EZK", "Ezek"),
    BibleBookEnum.Daniel: ("Dn", "dn", "Dan", "dan", "DAN"),

    # Minor Prophets (Spanish)
    BibleBookEnum.Hosea: ("Os", "os", "HOS", "Hos"),
    BibleBookEnum.Joel: ("Jl", "jl", "JOL", "Joel"),
    BibleBookEnum.Amos: ("Am", "am", "AMO", "Amos"),
    BibleBookEnum.Obadiah: ("Abd", "abd", "Ab", "ab", "OBA", "Obad"),
    # Key disambiguation: Jonah is Jon; John gospel is Jn
    BibleBookEnum.Jonah: ("Jon", "jon", "JON", "Jonah"),
    BibleBookEnum.Micah: ("Miq", "miq", "Mi", "mi", "MIC", "Mic"),
    BibleBookEnum.Nahum: ("Nah", "nah", "Na", "na", "NAM", "Nahum"),
    BibleBookEnum.Habakkuk: ("Hab", "hab", "Ha", "ha", "HAB", "Hab"),
    BibleBookEnum.Zephaniah: ("Sof", "sof", "ZEP", "Zeph"),
    BibleBookEnum.Haggai: ("Hag", "hag", "Ag", "ag", "HAG", "Hag"),
    BibleBookEnum.Zechariah: ("Zac", "zac", "Za", "za", "ZEC", "Zech"),
    BibleBookEnum.Malachi: ("Mal", "mal", "Ml", "ml", "MAL", "Mal"),

    # NT
    BibleBookEnum.Matthew: ("Mt", "mt", "Mat", "mat", "MAT", "Matt"),
    BibleBookEnum.Mark: ("Mc", "mc", "MRK", "Mark"),
    BibleBookEnum.Luke: ("Lc", "lc", "LUK", "Luke"),
    # Juan: accept both "Jn" and full token "Juan" (some lists do)
    BibleBookEnum.John: ("Jn", "jn", "Juan", "juan", "JHN", "John"),
    # Acts: Spanish commonly uses Hch; some lists also accept Hech
    BibleBookEnum.Acts: ("Hch", "hch", "Hech", "hech", "ACT", "Acts"),

    BibleBookEnum.Romans: ("Rm", "rm", "Ro", "ro", "Rom", "rom", "ROM"),
    BibleBookEnum.FirstCorinthians: ("1Co", "1 Co", "1Cor", "1 Cor", "1CO", "1Cor"),
    BibleBookEnum.SecondCorinthians: ("2Co", "2 Co", "2Cor", "2 Cor", "2CO", "2Cor"),
    BibleBookEnum.Galatians: ("Gl", "gl", "Ga", "ga", "Gál", "gál", "GAL"),
    BibleBookEnum.Ephesians: ("Ef", "ef", "Efes", "efes", "EPH"),
    BibleBookEnum.Philippians: ("Flp", "flp", "Fil", "fil", "PHP", "Phil"),
    BibleBookEnum.Colossians: ("Col", "col", "COL"),
    BibleBookEnum.FirstThessalonians: ("1Ts", "1 Ts", "1Tes", "1 Tes", "1TH", "1Thess"),
    BibleBookEnum.SecondThessalonians: ("2Ts", "2 Ts", "2Tes", "2 Tes", "2TH", "2Thess"),
    BibleBookEnum.FirstTimothy: ("1Ti", "1 Ti", "1Tm", "1 Tm", "1Tim", "1 Tim", "1TI", "1Tim"),
    BibleBookEnum.SecondTimothy: ("2Ti", "2 Ti", "2Tm", "2 Tm", "2Tim", "2 Tim", "2TI", "2Tim"),
    BibleBookEnum.Titus: ("Tit", "tit", "Tt", "tt", "TIT"),
    BibleBookEnum.Philemon: ("Flm", "flm", "Filem", "filem", "PHM", "Phlm"),
    BibleBookEnum.Hebrews: ("Heb", "heb", "Hb", "hb", "HEB"),
    # Santiago: Stg/St are common; also accept Sant/Stgo from some publishers
    BibleBookEnum.James: ("Stg", "stg", "St", "st", "Sant", "sant", "Stgo", "stgo", "JAS", "Jas"),
    BibleBookEnum.FirstPeter: ("1P", "1 P", "1Pe", "1 Pe", "1PE", "1Pet"),
    BibleBookEnum.SecondPeter: ("2P", "2 P", "2Pe", "2 Pe", "2PE", "2Pet"),
    BibleBookEnum.FirstJohn: ("1Jn", "1 Jn", "1JN", "1John"),
    BibleBookEnum.SecondJohn: ("2Jn", "2 Jn", "2JN", "2John"),
    BibleBookEnum.ThirdJohn: ("3Jn", "3 Jn", "3JN", "3John"),
    # Judas: avoid "Ju" ambiguity; prefer Jud/Jds
    BibleBookEnum.Jude: ("Jud", "jud", "Jds", "jds", "JUD", "Jude"),
    BibleBookEnum.Revelation: ("Ap", "ap", "Apoc", "apoc", "REV", "Rev"),

    # Deuterocanon / Apocrypha (Spanish)
    BibleBookEnum.Tobit: ("Tb", "tb", "Tob", "tob", "TOB"),
    BibleBookEnum.Judith: ("Jdt", "jdt", "JDT"),
    BibleBookEnum.Wisdom: ("Sab", "sab", "Sb", "sb", "WIS", "Wis"),
    BibleBookEnum.Sirach: ("Eclo", "eclo", "Si", "si", "Sir", "sir", "SIR"),
    BibleBookEnum.Baruch: ("Bar", "bar", "Ba", "ba", "BAR"),

    BibleBookEnum.FirstMaccabees: ("1Mac", "1 Mac", "1M", "1 M", "1MA", "1Macc"),
    BibleBookEnum.SecondMaccabees: ("2Mac", "2 Mac", "2M", "2 M", "2MA", "2Macc"),

    # 3–4 Maccabees are not in the CEE list; abbreviations vary → keep Spanish + USFM/OSIS IDs
    BibleBookEnum.ThirdMaccabees: ("3Mac", "3 Mac", "3MA", "3Macc"),
    BibleBookEnum.FourthMaccabees: ("4Mac", "4 Mac", "4MA", "4Macc"),

    # Greek Esther (BIBLIJA.net uses EstDC; USFM: ESG; OSIS: EsthGr/AddEsth)
    BibleBookEnum.EstherAdditions: ("EstDC", "estdc", "ESG", "EsthGr", "AddEsth"),

    # Daniel additions: rely on stable IDs + explicit Spanish section names
    BibleBookEnum.DanielSongOfThree: ("S3Y", "PrAzar"),
    BibleBookEnum.DanielSusanna: ("Sus", "sus", "SUS"),
    BibleBookEnum.DanielBelAndTheDragon: ("Bel", "bel", "BEL"),

    # Esdras apocrypha numbering varies by tradition; BIBLIJA.net uses 3 Esr / 4 Esr
    # Keep USFM/OSIS IDs as the authoritative anchors.
    BibleBookEnum.FirstEsdras: ("1ES", "1Esd", "1Esdras", "1 Esd", "3Esr", "3 Esr"),
    BibleBookEnum.SecondEsdras: ("2ES", "2Esd", "2Esdras", "2 Esd", "4Esr", "4 Esr"),

    BibleBookEnum.PrayerOfManasseh: ("Man", "man", "MAN", "PrMan"),
    # Psalm 151: BIBLIJA.net uses Sal151; USFM: PS2; OSIS: AddPs
    BibleBookEnum.Psalm151: ("Sal151", "sal151", "PS2", "AddPs"),
}
