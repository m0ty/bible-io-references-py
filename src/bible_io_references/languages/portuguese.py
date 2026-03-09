from typing import Dict, Iterable
from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ("Gênesis", "Génesis", "Genesis"),
    BibleBookEnum.Exodus: ("Êxodo", "Exodo"),
    BibleBookEnum.Leviticus: ("Levítico", "Levitico"),
    BibleBookEnum.Numbers: ("Números", "Numeros"),
    BibleBookEnum.Deuteronomy: ("Deuteronômio", "Deuteronómio", "Deuteronomio"),

    BibleBookEnum.Joshua: ("Josué", "Josue"),
    BibleBookEnum.Judges: ("Juízes", "Juizes"),
    BibleBookEnum.Ruth: ("Rute",),

    BibleBookEnum.FirstSamuel: ("1 Samuel", "1º Samuel", "I Samuel", "Primeiro Samuel"),
    BibleBookEnum.SecondSamuel: ("2 Samuel", "2º Samuel", "II Samuel", "Segundo Samuel"),

    BibleBookEnum.FirstKings: ("1 Reis", "1º Reis", "I Reis", "Primeiro Reis"),
    BibleBookEnum.SecondKings: ("2 Reis", "2º Reis", "II Reis", "Segundo Reis"),

    BibleBookEnum.FirstChronicles: ("1 Crônicas", "1 Cronicas", "1º Crônicas", "I Crônicas"),
    BibleBookEnum.SecondChronicles: ("2 Crônicas", "2 Cronicas", "2º Crônicas", "II Crônicas"),

    # Portuguese standard is Esdras; keep Ezra as permissive alias
    BibleBookEnum.Ezra: ("Esdras", "Ezra"),
    BibleBookEnum.Nehemiah: ("Neemias",),
    BibleBookEnum.Esther: ("Ester", "Esther"),
    BibleBookEnum.Job: ("Jó", "Job"),
    BibleBookEnum.Psalms: ("Salmos",),
    BibleBookEnum.Proverbs: ("Provérbios", "Proverbios"),
    BibleBookEnum.Ecclesiastes: ("Eclesiastes", "Coélet", "Coelet"),
    BibleBookEnum.SongOfSolomon: (
        "Cânticos", "Canticos",
        "Cântico dos Cânticos", "Cantico dos Canticos",
        "Cantares", "Cantares de Salomão", "Cantares de Salomao"
    ),

    BibleBookEnum.Isaiah: ("Isaías", "Isaias"),
    BibleBookEnum.Jeremiah: ("Jeremias",),
    BibleBookEnum.Lamentations: ("Lamentações", "Lamentacoes"),
    BibleBookEnum.Ezekiel: ("Ezequiel",),
    BibleBookEnum.Daniel: ("Daniel",),

    # Portuguese standard is Oséias/Oseias
    BibleBookEnum.Hosea: ("Oséias", "Oseias", "Oséias", "Oseias"),
    BibleBookEnum.Joel: ("Joel",),
    BibleBookEnum.Amos: ("Amós", "Amos"),
    BibleBookEnum.Obadiah: ("Obadias", "Abdias"),
    BibleBookEnum.Jonah: ("Jonas",),
    BibleBookEnum.Micah: ("Miquéias", "Miqueias"),
    BibleBookEnum.Nahum: ("Naum",),
    BibleBookEnum.Habakkuk: ("Habacuque", "Habacuc"),
    BibleBookEnum.Zephaniah: ("Sofonias",),
    BibleBookEnum.Haggai: ("Ageu",),
    BibleBookEnum.Zechariah: ("Zacarias",),
    BibleBookEnum.Malachi: ("Malaquias",),

    BibleBookEnum.Matthew: ("Mateus",),
    BibleBookEnum.Mark: ("Marcos",),
    BibleBookEnum.Luke: ("Lucas",),
    BibleBookEnum.John: ("João", "Joao"),
    BibleBookEnum.Acts: ("Atos", "Atos dos Apóstolos", "Atos dos Apostolos"),
    BibleBookEnum.Romans: ("Romanos",),
    BibleBookEnum.FirstCorinthians: ("1 Coríntios", "1 Corintios"),
    BibleBookEnum.SecondCorinthians: ("2 Coríntios", "2 Corintios"),
    BibleBookEnum.Galatians: ("Gálatas", "Galatas"),
    BibleBookEnum.Ephesians: ("Efésios", "Efesios"),
    BibleBookEnum.Philippians: ("Filipenses",),
    BibleBookEnum.Colossians: ("Colossenses",),
    BibleBookEnum.FirstThessalonians: ("1 Tessalonicenses", "1º Tessalonicenses"),
    BibleBookEnum.SecondThessalonians: ("2 Tessalonicenses", "2º Tessalonicenses"),
    BibleBookEnum.FirstTimothy: ("1 Timóteo", "1 Timoteo"),
    BibleBookEnum.SecondTimothy: ("2 Timóteo", "2 Timoteo"),
    BibleBookEnum.Titus: ("Tito",),
    BibleBookEnum.Philemon: ("Filemom", "Filemon", "Filêmon", "Filemón"),
    BibleBookEnum.Hebrews: ("Hebreus",),
    BibleBookEnum.James: ("Tiago",),
    BibleBookEnum.FirstPeter: ("1 Pedro", "1º Pedro"),
    BibleBookEnum.SecondPeter: ("2 Pedro", "2º Pedro"),
    BibleBookEnum.FirstJohn: ("1 João", "1 Joao", "1º João", "1º Joao"),
    BibleBookEnum.SecondJohn: ("2 João", "2 Joao", "2º João", "2º Joao"),
    BibleBookEnum.ThirdJohn: ("3 João", "3 Joao", "3º João", "3º Joao"),
    BibleBookEnum.Jude: ("Judas",),
    BibleBookEnum.Revelation: ("Apocalipse", "Apocalipse de João", "Apocalipse de Joao"),

    # Deuterocanon / Apocrypha (Portuguese Catholic usage)
    BibleBookEnum.Tobit: ("Tobias",),
    BibleBookEnum.Judith: ("Judite",),
    BibleBookEnum.Wisdom: ("Sabedoria", "Sabedoria de Salomão", "Sabedoria de Salomao"),
    BibleBookEnum.Sirach: ("Eclesiástico", "Eclesiastico", "Sirácida", "Siracida", "Ben Sira"),
    BibleBookEnum.Baruch: ("Baruc", "Baruque"),
    BibleBookEnum.FirstMaccabees: ("1 Macabeus", "1º Macabeus"),
    BibleBookEnum.SecondMaccabees: ("2 Macabeus", "2º Macabeus"),

    # Additions / extras (more variable; keep explicit Portuguese labels + common descriptors)
    BibleBookEnum.EstherAdditions: ("Ester (grego)", "Ester Grego", "Ester Gr"),
    BibleBookEnum.DanielSongOfThree: ("Oração de Azarias", "Oracao de Azarias", "Cântico dos Três Jovens", "Cantico dos Tres Jovens"),
    BibleBookEnum.DanielSusanna: ("Susana", "Suzana"),
    BibleBookEnum.DanielBelAndTheDragon: ("Bel e o Dragão", "Bel e o Dragao"),

    BibleBookEnum.FirstEsdras: ("1 Esdras", "Primeiro Esdras"),
    BibleBookEnum.SecondEsdras: ("2 Esdras", "Segundo Esdras"),
    BibleBookEnum.PrayerOfManasseh: ("Oração de Manassés", "Oracao de Manasses"),
    BibleBookEnum.Psalm151: ("Salmo 151", "Salmos Adicionais"),
    BibleBookEnum.ThirdMaccabees: ("3 Macabeus", "Terceiro Macabeus"),
    BibleBookEnum.FourthMaccabees: ("4 Macabeus", "Quarto Macabeus"),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    # Pentateuch
    BibleBookEnum.Genesis: ("Gn", "GN", "Gen", "GEN"),
    BibleBookEnum.Exodus: ("Ex", "Êx", "EX", "EXO", "Exod"),
    BibleBookEnum.Leviticus: ("Lv", "LV", "LEV", "Lev"),
    BibleBookEnum.Numbers: ("Nm", "NM", "NUM", "Num"),
    BibleBookEnum.Deuteronomy: ("Dt", "DT", "DEU", "Deut"),

    # OT history
    BibleBookEnum.Joshua: ("Js", "JS", "JOS", "Jos"),
    BibleBookEnum.Judges: ("Jz", "JZ", "JDG", "Jz"),
    BibleBookEnum.Ruth: ("Rt", "RT", "RUT", "Rute"),

    BibleBookEnum.FirstSamuel: ("1Sm", "1 Sm", "1SM", "1SA", "1Sam"),
    BibleBookEnum.SecondSamuel: ("2Sm", "2 Sm", "2SM", "2SA", "2Sam"),
    BibleBookEnum.FirstKings: ("1Rs", "1 Rs", "1RS", "1KI", "1Kgs"),
    BibleBookEnum.SecondKings: ("2Rs", "2 Rs", "2RS", "2KI", "2Kgs"),
    BibleBookEnum.FirstChronicles: ("1Cr", "1 Cr", "1CR", "1CH", "1Chr"),
    BibleBookEnum.SecondChronicles: ("2Cr", "2 Cr", "2CR", "2CH", "2Chr"),

    # Ezra/Esther/Job: common Portuguese abbreviations are Esd/Est/Jó; also allow Jb for Job (pt-PT Catholic)
    BibleBookEnum.Ezra: ("Esd", "Ed", "EZR", "Ezr"),
    BibleBookEnum.Nehemiah: ("Ne", "NE", "NEH", "Neh"),
    BibleBookEnum.Esther: ("Est", "Et", "EST", "Esth"),
    BibleBookEnum.Job: ("Jó", "Jb", "JOB", "Job"),

    # Wisdom
    BibleBookEnum.Psalms: ("Sl", "SL", "Ps", "PSA", "Psa"),
    BibleBookEnum.Proverbs: ("Pr", "Pv", "PR", "PRO", "Prov"),
    BibleBookEnum.Ecclesiastes: ("Ecl", "Ec", "Co", "ECC", "Eccl"),
    BibleBookEnum.SongOfSolomon: ("Ct", "CT", "Cant", "SNG", "Song"),

    # Prophets
    BibleBookEnum.Isaiah: ("Is", "IS", "ISA", "Isa"),
    BibleBookEnum.Jeremiah: ("Jr", "JR", "JER", "Jer"),
    BibleBookEnum.Lamentations: ("Lm", "LM", "LAM", "Lam"),
    BibleBookEnum.Ezekiel: ("Ez", "EZ", "EZK", "Ezek"),
    BibleBookEnum.Daniel: ("Dn", "DN", "DAN", "Dan"),
    BibleBookEnum.Hosea: ("Os", "OS", "HOS", "Hos"),
    BibleBookEnum.Joel: ("Jl", "JL", "JOL", "Joel"),
    BibleBookEnum.Amos: ("Am", "AM", "AMO", "Amos"),
    BibleBookEnum.Obadiah: ("Ab", "Abd", "OB", "OBA", "Obad"),
    BibleBookEnum.Jonah: ("Jn", "JON", "Jon"),
    BibleBookEnum.Micah: ("Mq", "MQ", "MIC", "Mic"),
    BibleBookEnum.Nahum: ("Na", "NA", "NAM", "Nah"),
    BibleBookEnum.Habakkuk: ("Hab", "Hc", "HAB", "Hab"),
    BibleBookEnum.Zephaniah: ("Sf", "SF", "ZEP", "Zeph"),
    BibleBookEnum.Haggai: ("Ag", "AG", "HAG", "Hag"),
    BibleBookEnum.Zechariah: ("Zc", "ZC", "ZEC", "Zech"),
    BibleBookEnum.Malachi: ("Ml", "ML", "MAL", "Mal"),

    # Gospels & Acts
    BibleBookEnum.Matthew: ("Mt", "MT", "MAT", "Matt"),
    BibleBookEnum.Mark: ("Mc", "MC", "MRK", "Mark"),
    BibleBookEnum.Luke: ("Lc", "LC", "LUK", "Luke"),
    BibleBookEnum.John: ("Jo", "JO", "JHN", "John"),

    BibleBookEnum.Acts: ("At", "AT", "ACT", "Acts"),
    BibleBookEnum.Romans: ("Rm", "RM", "ROM", "Rom"),
    BibleBookEnum.FirstCorinthians: ("1Cor", "1 Cor", "1Co", "1CO", "1Cor"),
    BibleBookEnum.SecondCorinthians: ("2Cor", "2 Cor", "2Co", "2CO", "2Cor"),
    BibleBookEnum.Galatians: ("Gl", "GL", "GAL", "Gal"),
    BibleBookEnum.Ephesians: ("Ef", "EF", "EPH", "Eph"),
    BibleBookEnum.Philippians: ("Fl", "Flp", "FL", "PHP", "Phil"),
    BibleBookEnum.Colossians: ("Cl", "CL", "COL", "Col"),
    BibleBookEnum.FirstThessalonians: ("1Ts", "1 Ts", "1TH", "1Thess"),
    BibleBookEnum.SecondThessalonians: ("2Ts", "2 Ts", "2TH", "2Thess"),
    BibleBookEnum.FirstTimothy: ("1Tm", "1 Tm", "1TI", "1Tim"),
    BibleBookEnum.SecondTimothy: ("2Tm", "2 Tm", "2TI", "2Tim"),
    BibleBookEnum.Titus: ("Tt", "TT", "TIT", "Tit"),
    BibleBookEnum.Philemon: ("Fm", "Flm", "PHM", "Phlm"),
    BibleBookEnum.Hebrews: ("Hb", "Heb", "HEB", "Heb"),
    BibleBookEnum.James: ("Tg", "TG", "JAS", "Jas"),
    BibleBookEnum.FirstPeter: ("1Pd", "1 Pd", "1PE", "1Pet"),
    BibleBookEnum.SecondPeter: ("2Pd", "2 Pd", "2PE", "2Pet"),
    BibleBookEnum.FirstJohn: ("1Jo", "1 Jo", "1JN", "1John"),
    BibleBookEnum.SecondJohn: ("2Jo", "2 Jo", "2JN", "2John"),
    BibleBookEnum.ThirdJohn: ("3Jo", "3 Jo", "3JN", "3John"),
    BibleBookEnum.Jude: ("Jd", "JD", "JUD", "Jude"),
    BibleBookEnum.Revelation: ("Ap", "Apo", "Apoc", "REV", "Rev"),

    # Deuterocanon (Portuguese Catholic conventions + tooling)
    BibleBookEnum.Tobit: ("Tb", "TB", "TOB", "Tob"),
    BibleBookEnum.Judith: ("Jt", "Jdt", "JDT", "Jdt"),
    BibleBookEnum.Wisdom: ("Sb", "SB", "WIS", "Wis"),
    BibleBookEnum.Sirach: ("Eclo", "Sir", "SIR", "Sir"),
    BibleBookEnum.Baruch: ("Br", "BR", "BAR", "Bar"),
    BibleBookEnum.FirstMaccabees: ("1Mc", "1Mac", "1 Mac", "1MA", "1Macc"),
    BibleBookEnum.SecondMaccabees: ("2Mc", "2Mac", "2 Mac", "2MA", "2Macc"),

    # Additions / extras (prefer stable IDs + attested Portuguese labels)
    BibleBookEnum.EstherAdditions: ("Est Gr", "Ester Gr", "ESG", "EsthGr"),
    BibleBookEnum.DanielSongOfThree: ("PrAzar", "S3Y"),
    BibleBookEnum.DanielSusanna: ("Sus", "SUS"),
    BibleBookEnum.DanielBelAndTheDragon: ("Bel", "BEL"),

    BibleBookEnum.FirstEsdras: ("1Esd", "1ES"),
    BibleBookEnum.SecondEsdras: ("2Esd", "2ES"),
    BibleBookEnum.PrayerOfManasseh: ("PrMan", "MAN"),
    BibleBookEnum.Psalm151: ("Sl Adc", "AddPs", "PS2", "Ps151"),
    BibleBookEnum.ThirdMaccabees: ("3Mac", "3Macc", "3MA"),
    BibleBookEnum.FourthMaccabees: ("4Mac", "4Macc", "4MA"),
}
