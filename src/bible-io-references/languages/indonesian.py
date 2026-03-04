from typing import Dict, Iterable
from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    # Perjanjian Lama (TB / TB-ecosystem common naming)
    BibleBookEnum.Genesis: ("Kejadian",),
    BibleBookEnum.Exodus: ("Keluaran",),
    BibleBookEnum.Leviticus: ("Imamat",),
    BibleBookEnum.Numbers: ("Bilangan",),
    BibleBookEnum.Deuteronomy: ("Ulangan",),

    BibleBookEnum.Joshua: ("Yosua",),
    BibleBookEnum.Judges: ("Hakim-hakim", "Hakim-Hakim"),
    BibleBookEnum.Ruth: ("Rut",),

    BibleBookEnum.FirstSamuel: ("1 Samuel", "1Samuel"),
    BibleBookEnum.SecondSamuel: ("2 Samuel", "2Samuel"),

    BibleBookEnum.FirstKings: ("1 Raja-raja", "1 Raja-Raja", "1Raja-raja", "1Raja-Raja"),
    BibleBookEnum.SecondKings: ("2 Raja-raja", "2 Raja-Raja", "2Raja-raja", "2Raja-Raja"),

    BibleBookEnum.FirstChronicles: ("1 Tawarikh", "1Tawarikh"),
    BibleBookEnum.SecondChronicles: ("2 Tawarikh", "2Tawarikh"),

    BibleBookEnum.Ezra: ("Ezra",),
    BibleBookEnum.Nehemiah: ("Nehemia",),
    BibleBookEnum.Esther: ("Ester", "Esther"),

    BibleBookEnum.Job: ("Ayub", "Job"),

    BibleBookEnum.Psalms: ("Mazmur",),
    BibleBookEnum.Proverbs: ("Amsal",),
    BibleBookEnum.Ecclesiastes: ("Pengkhotbah", "Pengkotbah"),
    BibleBookEnum.SongOfSolomon: ("Kidung Agung",),

    BibleBookEnum.Isaiah: ("Yesaya",),
    BibleBookEnum.Jeremiah: ("Yeremia",),
    BibleBookEnum.Lamentations: ("Ratapan", "Ratapan Yeremia"),
    BibleBookEnum.Ezekiel: ("Yehezkiel", "Yehezkiel", "Yeheskiel"),
    BibleBookEnum.Daniel: ("Daniel",),

    BibleBookEnum.Hosea: ("Hosea",),
    BibleBookEnum.Joel: ("Yoel", "Yoël", "Joel"),
    BibleBookEnum.Amos: ("Amos",),
    BibleBookEnum.Obadiah: ("Obaja",),
    BibleBookEnum.Jonah: ("Yunus",),
    BibleBookEnum.Micah: ("Mikha", "Mikha"),
    BibleBookEnum.Nahum: ("Nahum",),
    BibleBookEnum.Habakkuk: ("Habakuk",),
    BibleBookEnum.Zephaniah: ("Zefanya",),
    BibleBookEnum.Haggai: ("Hagai", "Haggai"),
    BibleBookEnum.Zechariah: ("Zakharia",),
    BibleBookEnum.Malachi: ("Maleakhi",),

    # Perjanjian Baru (TB / TB-ecosystem common naming)
    BibleBookEnum.Matthew: ("Matius",),
    BibleBookEnum.Mark: ("Markus",),
    BibleBookEnum.Luke: ("Lukas",),
    BibleBookEnum.John: ("Yohanes",),

    BibleBookEnum.Acts: ("Kisah Para Rasul", "Kisah Rasul"),
    BibleBookEnum.Romans: ("Roma",),

    BibleBookEnum.FirstCorinthians: ("1 Korintus", "1Korintus"),
    BibleBookEnum.SecondCorinthians: ("2 Korintus", "2Korintus"),

    BibleBookEnum.Galatians: ("Galatia",),
    BibleBookEnum.Ephesians: ("Efesus",),
    BibleBookEnum.Philippians: ("Filipi",),
    BibleBookEnum.Colossians: ("Kolose",),

    BibleBookEnum.FirstThessalonians: ("1 Tesalonika", "1Tesalonika"),
    BibleBookEnum.SecondThessalonians: ("2 Tesalonika", "2Tesalonika"),

    BibleBookEnum.FirstTimothy: ("1 Timotius", "1Timotius"),
    BibleBookEnum.SecondTimothy: ("2 Timotius", "2Timotius"),

    BibleBookEnum.Titus: ("Titus",),
    BibleBookEnum.Philemon: ("Filemon",),
    BibleBookEnum.Hebrews: ("Ibrani",),
    BibleBookEnum.James: ("Yakobus",),

    BibleBookEnum.FirstPeter: ("1 Petrus", "1Petrus"),
    BibleBookEnum.SecondPeter: ("2 Petrus", "2Petrus"),

    BibleBookEnum.FirstJohn: ("1 Yohanes", "1Yohanes"),
    BibleBookEnum.SecondJohn: ("2 Yohanes", "2Yohanes"),
    BibleBookEnum.ThirdJohn: ("3 Yohanes", "3Yohanes"),

    BibleBookEnum.Jude: ("Yudas",),
    BibleBookEnum.Revelation: ("Wahyu", "Wahyu kepada Yohanes"),

    # Deuterokanonika (Indonesian Catholic naming commonly used in Indonesia)
    BibleBookEnum.Tobit: ("Tobit", "Kitab Tobit"),
    BibleBookEnum.Judith: ("Yudit", "Judith", "Kitab Yudit"),
    BibleBookEnum.Wisdom: ("Kebijaksanaan Salomo", "Kebijaksanaan"),
    BibleBookEnum.Sirach: ("Yesus bin Sirakh", "Yesus Bin Sirakh", "Sirakh", "Kitab Sirakh"),
    BibleBookEnum.Baruch: ("Barukh", "Baruch", "Kitab Barukh"),

    BibleBookEnum.FirstMaccabees: ("1 Makabe", "1Makabe", "1 Makabeus"),
    BibleBookEnum.SecondMaccabees: ("2 Makabe", "2Makabe", "2 Makabeus"),
    BibleBookEnum.ThirdMaccabees: ("3 Makabe", "3Makabe"),
    BibleBookEnum.FourthMaccabees: ("4 Makabe", "4Makabe"),

    BibleBookEnum.EstherAdditions: ("Tambahan Ester", "Tambahan-tambahan pada Kitab Ester", "Ester (Yunani)", "Ester Yunani"),
    BibleBookEnum.DanielSongOfThree: (
        "Doa Azarya dan Lagu Pujian Ketiga Pemuda",
        "Doa Azarya",
        "Lagu Pujian Ketiga Pemuda",
        "Nyanyian Tiga Pemuda"
    ),
    BibleBookEnum.DanielSusanna: ("Susana", "Kisah Susana", "Kisah Susana dan Daniel"),
    BibleBookEnum.DanielBelAndTheDragon: ("Bel dan Naga", "Bel dan Naga Babel", "Dewa Bel dan Naga Babel"),

    BibleBookEnum.FirstEsdras: ("1 Esdras", "3 Esdras"),
    BibleBookEnum.SecondEsdras: ("2 Esdras", "4 Esdras"),

    BibleBookEnum.PrayerOfManasseh: ("Doa Manasye", "Doa Manasseh"),
    BibleBookEnum.Psalm151: ("Mazmur 151",),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    # OT (baseline: Alkitab.mobi/SABDA; plus common alternates like Ul/Ula, 1Sam/1Sa)
    BibleBookEnum.Genesis: ("Kej", "Kej.", "kej"),
    BibleBookEnum.Exodus: ("Kel", "Kel.", "kel"),
    BibleBookEnum.Leviticus: ("Ima", "Ima.", "Im", "Im.", "ima", "im"),
    BibleBookEnum.Numbers: ("Bil", "Bil.", "bil"),
    BibleBookEnum.Deuteronomy: ("Ula", "Ula.", "Ul", "Ul.", "ula", "ul"),

    BibleBookEnum.Joshua: ("Yos", "Yos.", "yos"),
    BibleBookEnum.Judges: ("Hak", "Hak.", "hak"),
    BibleBookEnum.Ruth: ("Rut", "Rut.", "rut"),

    BibleBookEnum.FirstSamuel: ("1Sa", "1Sa.", "1 Sam", "1 Sam.", "1Sam", "1Sam.", "1sa", "1sam"),
    BibleBookEnum.SecondSamuel: ("2Sa", "2Sa.", "2 Sam", "2 Sam.", "2Sam", "2Sam.", "2sa", "2sam"),

    BibleBookEnum.FirstKings: ("1Ra", "1Ra.", "1 Raj", "1 Raj.", "1Raj", "1Raj.", "1ra", "1raj"),
    BibleBookEnum.SecondKings: ("2Ra", "2Ra.", "2 Raj", "2 Raj.", "2Raj", "2Raj.", "2ra", "2raj"),

    BibleBookEnum.FirstChronicles: ("1Ta", "1Ta.", "1 Taw", "1 Taw.", "1Taw", "1Taw.", "1ta", "1taw"),
    BibleBookEnum.SecondChronicles: ("2Ta", "2Ta.", "2 Taw", "2 Taw.", "2Taw", "2Taw.", "2ta", "2taw"),

    BibleBookEnum.Ezra: ("Ezr", "Ezr.", "ezr"),
    BibleBookEnum.Nehemiah: ("Neh", "Neh.", "neh"),
    BibleBookEnum.Esther: ("Est", "Est.", "est"),

    BibleBookEnum.Job: ("Ayb", "Ayb.", "ayb", "Ayu", "Ayu.", "ayu"),
    BibleBookEnum.Psalms: ("Mzm", "Mzm.", "mzm", "Mz", "Mz.", "mz", "Maz", "Maz.", "maz"),
    BibleBookEnum.Proverbs: ("Ams", "Ams.", "ams"),
    BibleBookEnum.Ecclesiastes: ("Pkh", "Pkh.", "pkh", "Pengk", "Pengk.", "pengk"),
    BibleBookEnum.SongOfSolomon: ("Kid", "Kid.", "kid"),

    BibleBookEnum.Isaiah: ("Yes", "Yes.", "yes"),
    BibleBookEnum.Jeremiah: ("Yer", "Yer.", "yer"),
    BibleBookEnum.Lamentations: ("Rat", "Rat.", "rat"),
    BibleBookEnum.Ezekiel: ("Yeh", "Yeh.", "yeh"),
    BibleBookEnum.Daniel: ("Dan", "Dan.", "dan"),

    BibleBookEnum.Hosea: ("Hos", "Hos.", "hos"),
    BibleBookEnum.Joel: ("Yoe", "Yoe.", "yoe", "Yl", "Yl.", "yl"),
    BibleBookEnum.Amos: ("Amo", "Amo.", "amo", "Am", "Am.", "am"),
    BibleBookEnum.Obadiah: ("Oba", "Oba.", "oba", "Ob", "Ob.", "ob"),
    BibleBookEnum.Jonah: ("Yun", "Yun.", "yun"),
    BibleBookEnum.Micah: ("Mik", "Mik.", "mik", "Mi", "Mi.", "mi"),
    BibleBookEnum.Nahum: ("Nah", "Nah.", "nah"),
    BibleBookEnum.Habakkuk: ("Hab", "Hab.", "hab"),
    BibleBookEnum.Zephaniah: ("Zef", "Zef.", "zef"),
    BibleBookEnum.Haggai: ("Hag", "Hag.", "hag"),
    BibleBookEnum.Zechariah: ("Zak", "Zak.", "zak", "Za", "Za.", "za"),
    BibleBookEnum.Malachi: ("Mal", "Mal.", "mal"),

    # NT (baseline: Alkitab.mobi/SABDA; plus common alternates like Rm/Rom, 1Kor/1Ko, Wah/Why)
    BibleBookEnum.Matthew: ("Mat", "Mat.", "mat"),
    BibleBookEnum.Mark: ("Mrk", "Mrk.", "mrk", "Mar", "Mar.", "mar"),
    BibleBookEnum.Luke: ("Luk", "Luk.", "luk"),
    BibleBookEnum.John: ("Yoh", "Yoh.", "yoh"),

    BibleBookEnum.Acts: ("Kis", "Kis.", "kis"),
    BibleBookEnum.Romans: ("Rom", "Rom.", "rom", "Rm", "Rm.", "rm"),

    BibleBookEnum.FirstCorinthians: ("1Ko", "1Ko.", "1 Ko", "1 Ko.", "1Kor", "1Kor.", "1 Kor", "1 Kor.", "1ko", "1kor"),
    BibleBookEnum.SecondCorinthians: ("2Ko", "2Ko.", "2 Ko", "2 Ko.", "2Kor", "2Kor.", "2 Kor", "2 Kor.", "2ko", "2kor"),

    BibleBookEnum.Galatians: ("Gal", "Gal.", "gal"),
    BibleBookEnum.Ephesians: ("Efe", "Efe.", "efe", "Ef", "Ef.", "ef"),
    BibleBookEnum.Philippians: ("Flp", "Flp.", "flp", "Fili", "Fili.", "fili", "Fil", "Fil.", "fil"),
    BibleBookEnum.Colossians: ("Kol", "Kol.", "kol"),

    BibleBookEnum.FirstThessalonians: ("1Te", "1Te.", "1 Te", "1 Te.", "1Tes", "1Tes.", "1 Tes", "1 Tes.", "1te", "1tes"),
    BibleBookEnum.SecondThessalonians: ("2Te", "2Te.", "2 Te", "2 Te.", "2Tes", "2Tes.", "2 Tes", "2 Tes.", "2te", "2tes"),

    BibleBookEnum.FirstTimothy: ("1Ti", "1Ti.", "1 Ti", "1 Ti.", "1Tim", "1Tim.", "1 Tim", "1 Tim.", "1ti", "1tim"),
    BibleBookEnum.SecondTimothy: ("2Ti", "2Ti.", "2 Ti", "2 Ti.", "2Tim", "2Tim.", "2 Tim", "2 Tim.", "2ti", "2tim"),

    BibleBookEnum.Titus: ("Tit", "Tit.", "tit"),
    BibleBookEnum.Philemon: ("Flm", "Flm.", "flm", "File", "File.", "file"),
    BibleBookEnum.Hebrews: ("Ibr", "Ibr.", "ibr"),
    BibleBookEnum.James: ("Yak", "Yak.", "yak"),

    BibleBookEnum.FirstPeter: ("1Pt", "1Pt.", "1 Pt", "1 Pt.", "1Ptr", "1Ptr.", "1 Ptr", "1 Ptr.", "1pt", "1ptr"),
    BibleBookEnum.SecondPeter: ("2Pt", "2Pt.", "2 Pt", "2 Pt.", "2Ptr", "2Ptr.", "2 Ptr", "2 Ptr.", "2pt", "2ptr"),

    BibleBookEnum.FirstJohn: ("1Yo", "1Yo.", "1 Yo", "1 Yo.", "1Yoh", "1Yoh.", "1 Yoh", "1 Yoh.", "1yo", "1yoh"),
    BibleBookEnum.SecondJohn: ("2Yo", "2Yo.", "2 Yo", "2 Yo.", "2Yoh", "2Yoh.", "2 Yoh", "2 Yoh.", "2yo", "2yoh"),
    BibleBookEnum.ThirdJohn: ("3Yo", "3Yo.", "3 Yo", "3 Yo.", "3Yoh", "3Yoh.", "3 Yoh", "3 Yoh.", "3yo", "3yoh"),

    BibleBookEnum.Jude: ("Yud", "Yud.", "yud"),
    BibleBookEnum.Revelation: ("Why", "Why.", "why", "Wah", "Wah.", "wah"),

    # Deuterocanon / additions / orthodox extras (less standardized abbreviations in Indonesian public tables)
    # Strategy: accept common short forms seen in Indonesian usage + stable tooling IDs in case you ingest USFM/OSIS data.
    BibleBookEnum.Tobit: ("Tob", "Tob.", "tob", "TOB"),
    BibleBookEnum.Judith: ("Ydt", "Ydt.", "ydt", "JDT"),
    BibleBookEnum.Wisdom: ("Keb", "Keb.", "keb", "WIS"),
    BibleBookEnum.Sirach: ("Sir", "Sir.", "sir", "SIR"),
    BibleBookEnum.Baruch: ("Bar", "Bar.", "bar", "BAR"),

    BibleBookEnum.FirstMaccabees: ("1Mak", "1Mak.", "1 Mak", "1 Mak.", "1MA"),
    BibleBookEnum.SecondMaccabees: ("2Mak", "2Mak.", "2 Mak", "2 Mak.", "2MA"),
    BibleBookEnum.ThirdMaccabees: ("3Mak", "3Mak.", "3 Mak", "3 Mak.", "3MA"),
    BibleBookEnum.FourthMaccabees: ("4Mak", "4Mak.", "4 Mak", "4 Mak.", "4MA"),

    BibleBookEnum.EstherAdditions: ("TambEster", "Tamb Ester", "Tambahan Ester", "ESG"),
    BibleBookEnum.DanielSongOfThree: ("DoaAzarya", "Doa Azarya", "NyanyianTigaPemuda", "S3Y"),
    BibleBookEnum.DanielSusanna: ("Susana", "SUS"),
    BibleBookEnum.DanielBelAndTheDragon: ("BelNaga", "Bel dan Naga", "BEL"),

    BibleBookEnum.FirstEsdras: ("1Esd", "1Esd.", "1 Esd", "1 Esd.", "1ES"),
    BibleBookEnum.SecondEsdras: ("2Esd", "2Esd.", "2 Esd", "2 Esd.", "2ES"),

    BibleBookEnum.PrayerOfManasseh: ("DoaManasye", "Doa Manasye", "MAN"),
    BibleBookEnum.Psalm151: ("Mazmur151", "Mazmur 151", "Mzm151", "PS2", "AddPs"),
}
