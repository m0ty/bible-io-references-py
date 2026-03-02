from typing import Dict, Iterable
from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ("1. Mose", "1 Mose", "Erstes Buch Mose", "Genesis"),
    BibleBookEnum.Exodus: ("2. Mose", "2 Mose", "Zweites Buch Mose", "Exodus"),
    BibleBookEnum.Leviticus: ("3. Mose", "3 Mose", "Drittes Buch Mose", "Levitikus"),
    BibleBookEnum.Numbers: ("4. Mose", "4 Mose", "Viertes Buch Mose", "Numeri"),
    BibleBookEnum.Deuteronomy: ("5. Mose", "5 Mose", "Fünftes Buch Mose", "Deuteronomium"),

    BibleBookEnum.Joshua: ("Josua",),
    BibleBookEnum.Judges: ("Richter", "Buch der Richter"),
    BibleBookEnum.Ruth: ("Rut", "Ruth"),

    BibleBookEnum.FirstSamuel: ("1. Samuel", "1 Samuel", "Erstes Buch Samuel"),
    BibleBookEnum.SecondSamuel: ("2. Samuel", "2 Samuel", "Zweites Buch Samuel"),

    BibleBookEnum.FirstKings: ("1. Könige", "1 Könige", "1 Koenige", "Erstes Buch der Könige", "Erstes Buch der Koenige"),
    BibleBookEnum.SecondKings: ("2. Könige", "2 Könige", "2 Koenige", "Zweites Buch der Könige", "Zweites Buch der Koenige"),

    BibleBookEnum.FirstChronicles: ("1. Chronik", "1 Chronik", "Erstes Buch der Chronik"),
    BibleBookEnum.SecondChronicles: ("2. Chronik", "2 Chronik", "Zweites Buch der Chronik"),

    BibleBookEnum.Ezra: ("Esra", "Ezra"),
    BibleBookEnum.Nehemiah: ("Nehemia", "Nehemiah"),
    BibleBookEnum.Esther: ("Ester", "Esther"),

    BibleBookEnum.Job: ("Hiob", "Ijob", "Job"),
    BibleBookEnum.Psalms: ("Psalmen", "Psalm", "Psalter"),
    BibleBookEnum.Proverbs: ("Sprüche", "Sprueche", "Sprichwörter", "Sprichwoerter"),
    BibleBookEnum.Ecclesiastes: ("Prediger", "Kohelet", "Kohélet", "Qohelet"),
    BibleBookEnum.SongOfSolomon: ("Hohelied", "Hohes Lied", "Hoheslied", "Hohelied Salomos"),

    BibleBookEnum.Isaiah: ("Jesaja",),
    BibleBookEnum.Jeremiah: ("Jeremia",),
    BibleBookEnum.Lamentations: ("Klagelieder", "Klagelieder Jeremias"),
    BibleBookEnum.Ezekiel: ("Hesekiel", "Ezechiel"),
    BibleBookEnum.Daniel: ("Daniel",),

    BibleBookEnum.Hosea: ("Hosea",),
    BibleBookEnum.Joel: ("Joel", "Joël"),
    BibleBookEnum.Amos: ("Amos",),
    BibleBookEnum.Obadiah: ("Obadja",),
    BibleBookEnum.Jonah: ("Jona",),
    BibleBookEnum.Micah: ("Micha",),
    BibleBookEnum.Nahum: ("Nahum",),
    BibleBookEnum.Habakkuk: ("Habakuk", "Habakkuk"),
    BibleBookEnum.Zephaniah: ("Zefanja",),
    BibleBookEnum.Haggai: ("Haggai",),
    BibleBookEnum.Zechariah: ("Sacharja",),
    BibleBookEnum.Malachi: ("Maleachi",),

    BibleBookEnum.Matthew: ("Matthäus", "Matthaeus", "Matthaus", "Evangelium nach Matthäus", "Evangelium nach Matthaeus"),
    BibleBookEnum.Mark: ("Markus", "Evangelium nach Markus"),
    BibleBookEnum.Luke: ("Lukas", "Evangelium nach Lukas"),
    BibleBookEnum.John: ("Johannes", "Evangelium nach Johannes"),

    BibleBookEnum.Acts: ("Apostelgeschichte", "Apostelgeschichte des Lukas"),
    BibleBookEnum.Romans: ("Römer", "Roemer", "Brief an die Römer", "Brief an die Roemer"),

    BibleBookEnum.FirstCorinthians: ("1. Korinther", "1 Korinther", "Erster Korintherbrief"),
    BibleBookEnum.SecondCorinthians: ("2. Korinther", "2 Korinther", "Zweiter Korintherbrief"),

    BibleBookEnum.Galatians: ("Galater", "Galaterbrief"),
    BibleBookEnum.Ephesians: ("Epheser", "Epheserbrief"),
    BibleBookEnum.Philippians: ("Philipper", "Philipperbrief"),
    BibleBookEnum.Colossians: ("Kolosser", "Kolosserbrief"),

    BibleBookEnum.FirstThessalonians: ("1. Thessalonicher", "1 Thessalonicher", "Erster Thessalonicherbrief"),
    BibleBookEnum.SecondThessalonians: ("2. Thessalonicher", "2 Thessalonicher", "Zweiter Thessalonicherbrief"),

    BibleBookEnum.FirstTimothy: ("1. Timotheus", "1 Timotheus", "Erster Timotheusbrief"),
    BibleBookEnum.SecondTimothy: ("2. Timotheus", "2 Timotheus", "Zweiter Timotheusbrief"),

    BibleBookEnum.Titus: ("Titus", "Titusbrief"),
    BibleBookEnum.Philemon: ("Philemon", "Philemonbrief"),
    BibleBookEnum.Hebrews: ("Hebräer", "Hebraeer", "Hebräerbrief", "Hebraëerbrief"),
    BibleBookEnum.James: ("Jakobus", "Jakobusbrief"),
    BibleBookEnum.FirstPeter: ("1. Petrus", "1 Petrus", "Erster Petrusbrief"),
    BibleBookEnum.SecondPeter: ("2. Petrus", "2 Petrus", "Zweiter Petrusbrief"),
    BibleBookEnum.FirstJohn: ("1. Johannes", "1 Johannes", "Erster Johannesbrief"),
    BibleBookEnum.SecondJohn: ("2. Johannes", "2 Johannes", "Zweiter Johannesbrief"),
    BibleBookEnum.ThirdJohn: ("3. Johannes", "3 Johannes", "Dritter Johannesbrief"),
    BibleBookEnum.Jude: ("Judas", "Judasbrief"),
    BibleBookEnum.Revelation: ("Offenbarung", "Offenbarung des Johannes", "Apokalypse"),

    # Deuterocanon / Additions often found in German editions & portals
    BibleBookEnum.Tobit: ("Tobit", "Tobias", "Buch Tobit", "Buch Tobias"),
    BibleBookEnum.Judith: ("Judit", "Judith"),
    BibleBookEnum.Wisdom: ("Weisheit", "Weisheit Salomos", "Buch der Weisheit"),
    BibleBookEnum.Sirach: ("Sirach", "Jesus Sirach", "Buch Jesus Sirach"),
    BibleBookEnum.Baruch: ("Baruch",),

    BibleBookEnum.FirstMaccabees: ("1. Makkabäer", "1 Makkabäer", "1 Makkabaeer"),
    BibleBookEnum.SecondMaccabees: ("2. Makkabäer", "2 Makkabäer", "2 Makkabaeer"),
    BibleBookEnum.ThirdMaccabees: ("3. Makkabäer", "3 Makkabäer", "3 Makkabaeer"),
    BibleBookEnum.FourthMaccabees: ("4. Makkabäer", "4 Makkabäer", "4 Makkabaeer"),

    BibleBookEnum.EstherAdditions: ("Stücke zu Ester", "Stücke zum Buch Ester", "Zusätze zu Ester", "Esther (griechisch)", "Ester (griechisch)"),
    BibleBookEnum.DanielSongOfThree: ("Das Gebet Asarjas im Feuerofen", "Der Gesang der drei Männer im Feuerofen", "Gesang der drei Männer im Feuerofen"),
    BibleBookEnum.DanielSusanna: ("Susanna", "Susanna und Daniel", "Geschichte von Susanna und Daniel"),
    BibleBookEnum.DanielBelAndTheDragon: ("Bel und Drache", "Bel und der Drache"),

    # Names vary strongly in German traditions; include both neutral + explanatory variants
    BibleBookEnum.FirstEsdras: ("1 Esdras", "1. Esdras", "Esra (griechische Ergänzung)", "3. Esra", "3 Esra"),
    BibleBookEnum.SecondEsdras: ("2 Esdras", "2. Esdras", "Esra (lateinische Ergänzung)", "4. Esra", "4 Esra"),

    BibleBookEnum.PrayerOfManasseh: ("Gebet des Manasse", "Gebet Manasses", "Gebet Manesses"),
    BibleBookEnum.Psalm151: ("Psalm 151",),
}

from typing import Dict, Iterable
from ..bible_book_enums import BibleBookEnum

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    # Pentateuch (German practice: Gen/Ex/Lev/Num/Dtn; also common 1Mo/2Mo… forms)
    BibleBookEnum.Genesis: ("Gen", "gen", "GEN", "1Mo", "1 Mo", "1.Mo", "1 Mose", "1. Mose"),
    BibleBookEnum.Exodus: ("Ex", "ex", "EXO", "2Mo", "2 Mo", "2.Mo", "2 Mose", "2. Mose"),
    BibleBookEnum.Leviticus: ("Lev", "lev", "LEV", "3Mo", "3 Mo", "3.Mo", "3 Mose", "3. Mose"),
    BibleBookEnum.Numbers: ("Num", "num", "NUM", "4Mo", "4 Mo", "4.Mo", "4 Mose", "4. Mose"),
    BibleBookEnum.Deuteronomy: ("Dtn", "dtn", "DEU", "5Mo", "5 Mo", "5.Mo", "5 Mose", "5. Mose"),

    BibleBookEnum.Joshua: ("Jos", "jos", "JOS"),
    BibleBookEnum.Judges: ("Ri", "ri", "JDG"),
    BibleBookEnum.Ruth: ("Rut", "rut", "RUT", "Rt", "rt"),

    BibleBookEnum.FirstSamuel: ("1Sam", "1 Sam", "1. Sam", "1SA"),
    BibleBookEnum.SecondSamuel: ("2Sam", "2 Sam", "2. Sam", "2SA"),

    BibleBookEnum.FirstKings: ("1Kön", "1 Kön", "1Koen", "1 Koen", "1KI"),
    BibleBookEnum.SecondKings: ("2Kön", "2 Kön", "2Koen", "2 Koen", "2KI"),

    BibleBookEnum.FirstChronicles: ("1Chr", "1 Chr", "1CH"),
    BibleBookEnum.SecondChronicles: ("2Chr", "2 Chr", "2CH"),

    BibleBookEnum.Ezra: ("Esra", "esra", "EZR", "Esr", "esr"),
    BibleBookEnum.Nehemiah: ("Neh", "neh", "NEH"),
    BibleBookEnum.Esther: ("Est", "est", "EST"),

    BibleBookEnum.Job: ("Hi", "hi", "Hiob", "Ijob", "JOB"),
    BibleBookEnum.Psalms: ("Ps", "ps", "PSA"),
    BibleBookEnum.Proverbs: ("Spr", "spr", "PRO"),
    BibleBookEnum.Ecclesiastes: ("Pred", "pred", "Koh", "koh", "ECC"),
    BibleBookEnum.SongOfSolomon: ("Hld", "hld", "SNG", "Hhld", "hhld"),

    BibleBookEnum.Isaiah: ("Jes", "jes", "ISA"),
    BibleBookEnum.Jeremiah: ("Jer", "jer", "JER"),
    BibleBookEnum.Lamentations: ("Klgl", "klgl", "LAM", "Klg", "klg"),
    BibleBookEnum.Ezekiel: ("Hes", "hes", "Ez", "ez", "EZK"),
    BibleBookEnum.Daniel: ("Dan", "dan", "DAN"),

    BibleBookEnum.Hosea: ("Hos", "hos", "HOS"),
    BibleBookEnum.Joel: ("Joel", "joel", "Joël", "joël", "JOL"),
    BibleBookEnum.Amos: ("Am", "am", "AMO"),
    BibleBookEnum.Obadiah: ("Obd", "obd", "OBA"),
    BibleBookEnum.Jonah: ("Jona", "jona", "Jon", "jon", "JON"),
    BibleBookEnum.Micah: ("Mi", "mi", "MIC"),
    BibleBookEnum.Nahum: ("Nah", "nah", "NAM"),
    BibleBookEnum.Habakkuk: ("Hab", "hab", "HAB"),
    BibleBookEnum.Zephaniah: ("Zef", "zef", "ZEP"),
    BibleBookEnum.Haggai: ("Hag", "hag", "HAG"),
    BibleBookEnum.Zechariah: ("Sach", "sach", "ZEC"),
    BibleBookEnum.Malachi: ("Mal", "mal", "MAL"),

    # NT
    BibleBookEnum.Matthew: ("Mt", "mt", "MAT"),
    BibleBookEnum.Mark: ("Mk", "mk", "MRK"),
    BibleBookEnum.Luke: ("Lk", "lk", "LUK"),
    BibleBookEnum.John: ("Joh", "joh", "JHN"),

    BibleBookEnum.Acts: ("Apg", "apg", "ACT"),
    BibleBookEnum.Romans: ("Röm", "röm", "Roem", "roem", "ROM"),

    BibleBookEnum.FirstCorinthians: ("1Kor", "1 Kor", "1. Kor", "1CO"),
    BibleBookEnum.SecondCorinthians: ("2Kor", "2 Kor", "2. Kor", "2CO"),
    BibleBookEnum.Galatians: ("Gal", "gal", "GAL"),
    BibleBookEnum.Ephesians: ("Eph", "eph", "EPH"),
    BibleBookEnum.Philippians: ("Phil", "phil", "PHP", "Php", "php"),
    BibleBookEnum.Colossians: ("Kol", "kol", "COL"),

    BibleBookEnum.FirstThessalonians: ("1Thess", "1 Thess", "1. Thess", "1TH"),
    BibleBookEnum.SecondThessalonians: ("2Thess", "2 Thess", "2. Thess", "2TH"),
    BibleBookEnum.FirstTimothy: ("1Tim", "1 Tim", "1. Tim", "1TI"),
    BibleBookEnum.SecondTimothy: ("2Tim", "2 Tim", "2. Tim", "2TI"),
    BibleBookEnum.Titus: ("Tit", "tit", "TIT"),
    BibleBookEnum.Philemon: ("Phlm", "phlm", "PHM"),
    BibleBookEnum.Hebrews: ("Hebr", "hebr", "HEB"),
    BibleBookEnum.James: ("Jak", "jak", "JAS"),
    BibleBookEnum.FirstPeter: ("1Petr", "1 Petr", "1. Petr", "1PE"),
    BibleBookEnum.SecondPeter: ("2Petr", "2 Petr", "2. Petr", "2PE"),
    BibleBookEnum.FirstJohn: ("1Joh", "1 Joh", "1. Joh", "1JN"),
    BibleBookEnum.SecondJohn: ("2Joh", "2 Joh", "2. Joh", "2JN"),
    BibleBookEnum.ThirdJohn: ("3Joh", "3 Joh", "3. Joh", "3JN"),
    BibleBookEnum.Jude: ("Jud", "jud", "JUD"),
    BibleBookEnum.Revelation: ("Offb", "offb", "REV"),

    # Deuterocanon / Additions (German: Tb/Jdt/Weish/Sir/Bar; plus USFM/OSIS IDs)
    BibleBookEnum.Tobit: ("Tob", "tob", "TOB", "Tobit", "Tobias"),
    BibleBookEnum.Judith: ("Jdt", "jdt", "JDT"),
    BibleBookEnum.Wisdom: ("Weish", "weish", "WIS", "Weis", "weis"),
    BibleBookEnum.Sirach: ("Sir", "sir", "SIR"),
    BibleBookEnum.Baruch: ("Bar", "bar", "BAR"),

    BibleBookEnum.FirstMaccabees: ("1Makk", "1 Makk", "1. Makk", "1MA"),
    BibleBookEnum.SecondMaccabees: ("2Makk", "2 Makk", "2. Makk", "2MA"),
    BibleBookEnum.ThirdMaccabees: ("3Makk", "3 Makk", "3. Makk", "3MA", "3Macc", "3macc"),
    BibleBookEnum.FourthMaccabees: ("4Makk", "4 Makk", "4. Makk", "4MA", "4Macc", "4macc"),

    BibleBookEnum.EstherAdditions: ("St zu Est", "StzuEst", "EstZ", "estz", "ESG", "EsthGr", "esthgr"),
    BibleBookEnum.DanielSongOfThree: ("S3Y", "PrAzar", "prazar", "Gesang der drei Männer", "Gebet Asarjas"),
    BibleBookEnum.DanielSusanna: ("Sus", "sus", "SUS", "Susanna"),
    BibleBookEnum.DanielBelAndTheDragon: ("Bel", "bel", "BEL", "Bel und Drache"),

    BibleBookEnum.FirstEsdras: ("1ES", "1Esd", "1esd", "1 Esd", "3Esra", "3 Esra"),
    BibleBookEnum.SecondEsdras: ("2ES", "2Esd", "2esd", "2 Esd", "4Esra", "4 Esra"),

    BibleBookEnum.PrayerOfManasseh: ("Geb.Man", "GebMan", "MAN", "PrMan", "prman"),
    BibleBookEnum.Psalm151: ("Ps151", "ps151", "PS2", "AddPs", "addps"),
}
