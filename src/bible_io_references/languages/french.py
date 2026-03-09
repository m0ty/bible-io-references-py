from typing import Dict, Iterable
from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ("Genèse", "Genese", "Livre de la Genèse", "Livre de la Genese"),
    BibleBookEnum.Exodus: ("Exode", "Livre de l'Exode", "Livre de l Exode"),
    BibleBookEnum.Leviticus: ("Lévitique", "Levitique", "Livre du Lévitique", "Livre du Levitique"),
    BibleBookEnum.Numbers: ("Nombres", "Livre des Nombres"),
    BibleBookEnum.Deuteronomy: ("Deutéronome", "Deuteronome", "Livre du Deutéronome", "Livre du Deuteronome"),

    BibleBookEnum.Joshua: ("Josué", "Josue", "Livre de Josué", "Livre de Josue"),
    BibleBookEnum.Judges: ("Juges", "Livre des Juges"),
    BibleBookEnum.Ruth: ("Ruth", "Livre de Ruth"),

    BibleBookEnum.FirstSamuel: ("1 Samuel", "I Samuel", "Premier livre de Samuel", "1er Samuel"),
    BibleBookEnum.SecondSamuel: ("2 Samuel", "II Samuel", "Deuxième livre de Samuel", "Deuxieme livre de Samuel", "2e Samuel"),

    BibleBookEnum.FirstKings: ("1 Rois", "I Rois", "Premier livre des Rois", "1er Rois"),
    BibleBookEnum.SecondKings: ("2 Rois", "II Rois", "Deuxième livre des Rois", "Deuxieme livre des Rois", "2e Rois"),

    BibleBookEnum.FirstChronicles: ("1 Chroniques", "I Chroniques", "Premier livre des Chroniques", "1er Chroniques"),
    BibleBookEnum.SecondChronicles: ("2 Chroniques", "II Chroniques", "Deuxième livre des Chroniques", "Deuxieme livre des Chroniques", "2e Chroniques"),

    # Key correction: Esdras is the common French book name
    BibleBookEnum.Ezra: ("Esdras", "Livre d'Esdras", "Livre d’Esdras", "Ezra"),

    BibleBookEnum.Nehemiah: ("Néhémie", "Nehemie", "Livre de Néhémie", "Livre de Nehemie"),
    BibleBookEnum.Esther: ("Esther", "Livre d'Esther", "Livre d’Esther"),
    BibleBookEnum.Job: ("Job", "Livre de Job"),
    BibleBookEnum.Psalms: ("Psaumes", "Psaume", "Livre des Psaumes", "Psautier"),
    BibleBookEnum.Proverbs: ("Proverbes", "Livre des Proverbes"),

    BibleBookEnum.Ecclesiastes: (
        "Ecclésiaste", "Ecclesiaste", "L'Ecclésiaste", "L'Ecclesiaste",
        "Qohéleth", "Qoheleth", "Qohélet", "Qohelet"
    ),

    BibleBookEnum.SongOfSolomon: ("Cantique des cantiques", "Cantique des Cantiques", "Cantique", "Chant de Salomon"),

    # Include both Ésaïe and Isaïe variants seen across traditions
    BibleBookEnum.Isaiah: ("Ésaïe", "Esaie", "Isaïe", "Isaie", "Livre d'Isaïe", "Livre d’Isaïe"),
    BibleBookEnum.Jeremiah: ("Jérémie", "Jeremie", "Livre de Jérémie", "Livre de Jeremie"),
    BibleBookEnum.Lamentations: (
        "Lamentations", "Lamentations de Jérémie", "Lamentations de Jeremie",
        "Livre des lamentations de Jérémie", "Livre des lamentations de Jeremie"
    ),
    BibleBookEnum.Ezekiel: ("Ézéchiel", "Ezechiel", "Ezekiel", "Livre d'Ezekiel", "Livre d’Ézéchiel", "Livre d'Ezéchiel"),
    BibleBookEnum.Daniel: ("Daniel", "Livre de Daniel"),

    # Key correction: Osée is standard French
    BibleBookEnum.Hosea: ("Osée", "Osee", "Livre d'Osée", "Livre d Osee", "Hoshéa", "Hoshea", "Hosee"),
    BibleBookEnum.Joel: ("Joël", "Joel", "Livre de Joël", "Livre de Joel"),
    BibleBookEnum.Amos: ("Amos", "Livre d'Amos", "Livre d’Amos"),
    BibleBookEnum.Obadiah: ("Abdias", "Livre d'Abdias", "Livre d’Abdias"),
    BibleBookEnum.Jonah: ("Jonas", "Livre de Jonas"),
    BibleBookEnum.Micah: ("Michée", "Michee", "Livre de Michée", "Livre de Michee"),
    BibleBookEnum.Nahum: ("Nahum", "Nahoum", "Livre de Nahum", "Livre de Nahoum"),
    BibleBookEnum.Habakkuk: ("Habacuc", "Habaquc", "Habakuk", "Habakkuk", "Livre d'Habaquc", "Livre d'Habacuc"),
    BibleBookEnum.Zephaniah: ("Sophonie", "Livre de Sophonie"),
    BibleBookEnum.Haggai: ("Aggée", "Aggee", "Livre d'Aggée", "Livre d Aggee"),
    BibleBookEnum.Zechariah: ("Zacharie", "Livre de Zacharie"),
    BibleBookEnum.Malachi: ("Malachie", "Livre de Malachie"),

    BibleBookEnum.Matthew: ("Matthieu", "Évangile selon Matthieu", "Evangile selon Matthieu", "Évangile de Jésus-Christ selon saint Matthieu", "Evangile de Jesus-Christ selon saint Matthieu"),
    BibleBookEnum.Mark: ("Marc", "Évangile selon Marc", "Evangile selon Marc", "Évangile de Jésus-Christ selon saint Marc", "Evangile de Jesus-Christ selon saint Marc"),
    BibleBookEnum.Luke: ("Luc", "Évangile selon Luc", "Evangile selon Luc", "Évangile de Jésus-Christ selon saint Luc", "Evangile de Jesus-Christ selon saint Luc"),
    BibleBookEnum.John: ("Jean", "Évangile selon Jean", "Evangile selon Jean", "Évangile de Jésus-Christ selon saint Jean", "Evangile de Jesus-Christ selon saint Jean"),

    BibleBookEnum.Acts: ("Actes", "Actes des Apôtres", "Actes des Apotres", "Livre des Actes des Apôtres", "Livre des Actes des Apotres"),
    BibleBookEnum.Romans: ("Romains", "Lettre aux Romains", "Épître aux Romains", "Epitre aux Romains"),

    BibleBookEnum.FirstCorinthians: ("1 Corinthiens", "I Corinthiens", "Première lettre aux Corinthiens", "Premiere lettre aux Corinthiens", "1re lettre aux Corinthiens", "1ère lettre aux Corinthiens"),
    BibleBookEnum.SecondCorinthians: ("2 Corinthiens", "II Corinthiens", "Deuxième lettre aux Corinthiens", "Deuxieme lettre aux Corinthiens", "2e lettre aux Corinthiens"),

    BibleBookEnum.Galatians: ("Galates", "Lettre aux Galates"),
    BibleBookEnum.Ephesians: ("Éphésiens", "Ephesiens"),
    BibleBookEnum.Philippians: ("Philippiens",),
    BibleBookEnum.Colossians: ("Colossiens",),

    BibleBookEnum.FirstThessalonians: ("1 Thessaloniciens", "I Thessaloniciens", "Première lettre aux Thessaloniciens", "Premiere lettre aux Thessaloniciens"),
    BibleBookEnum.SecondThessalonians: ("2 Thessaloniciens", "II Thessaloniciens", "Deuxième lettre aux Thessaloniciens", "Deuxieme lettre aux Thessaloniciens"),

    BibleBookEnum.FirstTimothy: ("1 Timothée", "1 Timothee", "I Timothée", "Première lettre à Timothée", "Premiere lettre a Timothee"),
    BibleBookEnum.SecondTimothy: ("2 Timothée", "2 Timothee", "II Timothée", "Deuxième lettre à Timothée", "Deuxieme lettre a Timothee"),

    # Key correction: French is “Tite”
    BibleBookEnum.Titus: ("Tite", "Titus", "Lettre à Tite", "Lettre a Tite"),

    # Key correction: accent is common in French
    BibleBookEnum.Philemon: ("Philémon", "Philemon", "Lettre à Philémon", "Lettre a Philemon"),

    BibleBookEnum.Hebrews: ("Hébreux", "Hebreux", "Lettre aux Hébreux", "Lettre aux Hebreux"),
    BibleBookEnum.James: ("Jacques", "Lettre de Jacques"),
    BibleBookEnum.FirstPeter: ("1 Pierre", "I Pierre", "Première lettre de Pierre", "Premiere lettre de Pierre"),
    BibleBookEnum.SecondPeter: ("2 Pierre", "II Pierre", "Deuxième lettre de Pierre", "Deuxieme lettre de Pierre"),
    BibleBookEnum.FirstJohn: ("1 Jean", "I Jean", "Première lettre de Jean", "Premiere lettre de Jean"),
    BibleBookEnum.SecondJohn: ("2 Jean", "II Jean", "Deuxième lettre de Jean", "Deuxieme lettre de Jean"),
    BibleBookEnum.ThirdJohn: ("3 Jean", "III Jean", "Troisième lettre de Jean", "Troisieme lettre de Jean"),
    BibleBookEnum.Jude: ("Jude", "Lettre de Jude"),
    BibleBookEnum.Revelation: ("Apocalypse", "Livre de l'Apocalypse", "Apocalypse de Jean", "Révélation", "Revelation"),

    # Deuterocanon / Apocrypha (French naming varies; include common Catholic + TOB-style)
    BibleBookEnum.Tobit: ("Tobie", "Tobit", "Livre de Tobie", "Livre de Tobit"),
    BibleBookEnum.Judith: ("Judith", "Livre de Judith"),
    BibleBookEnum.Wisdom: ("Sagesse", "Livre de la Sagesse", "Sagesse de Salomon"),

    # Key correction: Sirach -> Siracide / Ben Sira
    BibleBookEnum.Sirach: ("Siracide", "Ecclésiastique", "Ecclesiastique", "Ben Sira le Sage", "Livre de Ben Sira le Sage"),

    BibleBookEnum.Baruch: ("Baruch", "Livre de Baruch"),

    # AELF calls these “Martyrs d’Israël”; most Bibles call them “Maccabées”
    BibleBookEnum.FirstMaccabees: ("1 Maccabées", "1 Maccabees", "Premier Livre des Martyrs d'Israël", "Premier livre des Martyrs d'Israël"),
    BibleBookEnum.SecondMaccabees: ("2 Maccabées", "2 Maccabees", "Deuxième Livre des Martyrs d'Israël", "Deuxieme Livre des Martyrs d'Israël"),
    BibleBookEnum.ThirdMaccabees: ("3 Maccabées", "3 Maccabees"),
    BibleBookEnum.FourthMaccabees: ("4 Maccabées", "4 Maccabees"),

    # Greek Esther and Greek Daniel materials are commonly labeled this way in French platforms
    BibleBookEnum.EstherAdditions: ("Esther grec", "Esther (grec)", "Esther grecque", "Additions à Esther", "Additions a Esther"),

    # Greek Daniel “morceaux” are titled in French as prayer/canticle and stories
    BibleBookEnum.DanielSongOfThree: (
        "Prière d'Azarya", "Prière d'Azaria", "Priere d'Azarya", "Priere d'Azaria",
        "Cantique des trois jeunes gens", "Cantique des trois enfants",
        "Cantique des trois amis de Daniel", "Le cantique des trois amis de Daniel"
    ),
    BibleBookEnum.DanielSusanna: ("Suzanne", "Susanne", "Suzanne et les vieillards", "Histoire de Suzanne"),
    BibleBookEnum.DanielBelAndTheDragon: ("Bel et le Dragon", "Bel et le grand serpent", "Daniel et les prêtres de Bel", "Bel et le serpent"),

    # Esdras numbering differs by tradition; TOB/BJ tables often label these 3–4 Esdras
    BibleBookEnum.FirstEsdras: ("1 Esdras", "Premier Esdras", "3 Esdras", "Troisième Esdras", "3 Esd", "3Esd", "1Esd"),
    BibleBookEnum.SecondEsdras: ("2 Esdras", "Deuxième Esdras", "4 Esdras", "Quatrième Esdras", "4 Esd", "4Esd", "2Esd"),

    BibleBookEnum.PrayerOfManasseh: ("Prière de Manassé", "Priere de Manasse", "Prière de Manassé", "Priere de Manasse"),
    BibleBookEnum.Psalm151: ("Psaume 151", "psaume 151"),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    # Pentateuch
    BibleBookEnum.Genesis: ("Gn", "gn", "Gn.", "gn.", "Gen", "gen"),
    BibleBookEnum.Exodus: ("Ex", "ex", "Ex.", "ex."),
    BibleBookEnum.Leviticus: ("Lv", "lv", "Lv.", "lv."),
    BibleBookEnum.Numbers: ("Nb", "nb", "Nb.", "nb."),
    BibleBookEnum.Deuteronomy: ("Dt", "dt", "Dt.", "dt."),

    # Historical
    BibleBookEnum.Joshua: ("Jos", "jos", "Jos.", "jos."),
    BibleBookEnum.Judges: ("Jg", "jg", "Jg.", "jg.", "Jug", "jug"),
    BibleBookEnum.Ruth: ("Rt", "rt", "Ru", "ru"),
    BibleBookEnum.FirstSamuel: ("1 S", "1S", "1s", "1 Sam", "1Sam", "1sam"),
    BibleBookEnum.SecondSamuel: ("2 S", "2S", "2s", "2 Sam", "2Sam", "2sam"),
    BibleBookEnum.FirstKings: ("1 R", "1R", "1r", "1 Rois", "1Rois", "1rois"),
    BibleBookEnum.SecondKings: ("2 R", "2R", "2r", "2 Rois", "2Rois", "2rois"),
    BibleBookEnum.FirstChronicles: ("1 Ch", "1Ch", "1ch", "1 Chr", "1Chr", "1chr"),
    BibleBookEnum.SecondChronicles: ("2 Ch", "2Ch", "2ch", "2 Chr", "2Chr", "2chr"),
    BibleBookEnum.Ezra: ("Esd", "esd", "Ezr", "ezr"),  # Esdras is the dominant French abbreviation; Ezr occurs in some tables
    BibleBookEnum.Nehemiah: ("Ne", "ne", "Neh", "neh"),
    BibleBookEnum.Esther: ("Est", "est", "Est.", "est."),

    # Wisdom
    BibleBookEnum.Job: ("Jb", "jb"),
    BibleBookEnum.Psalms: ("Ps", "ps", "Psa", "psa"),
    BibleBookEnum.Proverbs: ("Pr", "pr", "Prov", "prov"),
    BibleBookEnum.Ecclesiastes: ("Qo", "qo", "Ec", "ec"),
    BibleBookEnum.SongOfSolomon: ("Ct", "ct", "Cant", "cant"),

    # Prophets
    BibleBookEnum.Isaiah: ("Is", "is", "Es", "es"),  # Is is common in Catholic/liturgical lists; Es appears in some TOB/BJ tables
    BibleBookEnum.Jeremiah: ("Jr", "jr"),
    BibleBookEnum.Lamentations: ("Lm", "lm"),
    BibleBookEnum.Ezekiel: ("Ez", "ez", "Éz", "éz"),
    BibleBookEnum.Daniel: ("Dn", "dn"),
    BibleBookEnum.Hosea: ("Os", "os", "Ho", "ho"),
    BibleBookEnum.Joel: ("Jl", "jl"),
    BibleBookEnum.Amos: ("Am", "am"),
    BibleBookEnum.Obadiah: ("Ab", "ab", "Ob", "ob"),
    BibleBookEnum.Jonah: ("Jon", "jon", "Yon", "yon"),
    BibleBookEnum.Micah: ("Mi", "mi"),
    BibleBookEnum.Nahum: ("Na", "na"),
    BibleBookEnum.Habakkuk: ("Ha", "ha", "Hab", "hab"),
    BibleBookEnum.Zephaniah: ("So", "so", "Soph", "soph"),
    BibleBookEnum.Haggai: ("Ag", "ag"),
    BibleBookEnum.Zechariah: ("Za", "za", "Zac", "zac"),
    BibleBookEnum.Malachi: ("Ml", "ml"),

    # Gospels & Acts
    BibleBookEnum.Matthew: ("Mt", "mt"),
    BibleBookEnum.Mark: ("Mc", "mc"),
    BibleBookEnum.Luke: ("Lc", "lc"),
    BibleBookEnum.John: ("Jn", "jn"),
    BibleBookEnum.Acts: ("Ac", "ac"),

    # Epistles
    BibleBookEnum.Romans: ("Rm", "rm", "Rom", "rom"),
    BibleBookEnum.FirstCorinthians: ("1 Co", "1Co", "1co", "1 Cor", "1Cor", "1cor"),
    BibleBookEnum.SecondCorinthians: ("2 Co", "2Co", "2co", "2 Cor", "2Cor", "2cor"),
    BibleBookEnum.Galatians: ("Ga", "ga"),
    BibleBookEnum.Ephesians: ("Ep", "ep", "Ép", "ép"),
    BibleBookEnum.Philippians: ("Ph", "ph"),
    BibleBookEnum.Colossians: ("Col", "col"),
    BibleBookEnum.FirstThessalonians: ("1 Th", "1Th", "1th"),
    BibleBookEnum.SecondThessalonians: ("2 Th", "2Th", "2th"),
    BibleBookEnum.FirstTimothy: ("1 Tm", "1Tm", "1tm"),
    BibleBookEnum.SecondTimothy: ("2 Tm", "2Tm", "2tm"),
    BibleBookEnum.Titus: ("Tt", "tt"),
    BibleBookEnum.Philemon: ("Phm", "phm"),
    BibleBookEnum.Hebrews: ("He", "he", "Hé", "hé"),
    BibleBookEnum.James: ("Jc", "jc", "Jac", "jac"),
    BibleBookEnum.FirstPeter: ("1 P", "1P", "1p"),
    BibleBookEnum.SecondPeter: ("2 P", "2P", "2p"),
    BibleBookEnum.FirstJohn: ("1 Jn", "1Jn", "1jn"),
    BibleBookEnum.SecondJohn: ("2 Jn", "2Jn", "2jn"),
    BibleBookEnum.ThirdJohn: ("3 Jn", "3Jn", "3jn"),
    BibleBookEnum.Jude: ("Jude", "jude", "Jd", "jd"),

    # Revelation
    BibleBookEnum.Revelation: ("Ap", "ap", "Apo", "apo", "Apoc", "apoc", "Ré", "ré", "Re", "re"),

    # Deuterocanon / Apocrypha (French church tables + tooling IDs)
    BibleBookEnum.Tobit: ("Tb", "tb", "Tob", "tob", "TOB"),
    BibleBookEnum.Judith: ("Jdt", "jdt", "JDT"),
    BibleBookEnum.Wisdom: ("Sg", "sg", "WIS", "Wis", "wis"),
    BibleBookEnum.Sirach: ("Si", "si", "SIR", "Sir", "sir"),
    BibleBookEnum.Baruch: ("Ba", "ba", "BAR", "Bar", "bar"),

    BibleBookEnum.FirstMaccabees: ("1 M", "1M", "1m", "1 Mac", "1Mac", "1MA", "1Macc", "1macc"),
    BibleBookEnum.SecondMaccabees: ("2 M", "2M", "2m", "2 Mac", "2Mac", "2MA", "2Macc", "2macc"),
    BibleBookEnum.ThirdMaccabees: ("3 M", "3M", "3m", "3MA", "3Macc", "3macc"),
    BibleBookEnum.FourthMaccabees: ("4 M", "4M", "4m", "4MA", "4Macc", "4macc"),

    BibleBookEnum.EstherAdditions: ("Est gr", "Estgr", "est gr", "estgr", "ESG", "EsthGr", "esthgr"),
    BibleBookEnum.DanielSongOfThree: ("Dn gr", "Dn gr 3", "dn gr", "dn gr 3", "S3Y", "PrAzar", "prazar"),
    BibleBookEnum.DanielSusanna: ("Sus", "sus", "SUS"),
    BibleBookEnum.DanielBelAndTheDragon: ("Bel", "bel", "BEL"),

    BibleBookEnum.FirstEsdras: ("1Esd", "1esd", "1ES", "3 Esd", "3Esd", "3 esd", "3esd"),
    BibleBookEnum.SecondEsdras: ("2Esd", "2esd", "2ES", "4 Esd", "4Esd", "4 esd", "4esd"),

    BibleBookEnum.PrayerOfManasseh: ("Mn", "mn", "MAN", "PrMan", "prman"),
    BibleBookEnum.Psalm151: ("Ps151", "ps151", "Ps 151", "ps 151", "AddPs", "addps", "PS2"),
}
