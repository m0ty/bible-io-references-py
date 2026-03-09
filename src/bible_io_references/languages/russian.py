from typing import Dict, Iterable
from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    # Torah / Pentateuch
    BibleBookEnum.Genesis: ("Бытие", "Книга Бытия"),
    BibleBookEnum.Exodus: ("Исход", "Книга Исход"),
    BibleBookEnum.Leviticus: ("Левит", "Книга Левит"),
    BibleBookEnum.Numbers: ("Числа", "Книга Чисел"),
    BibleBookEnum.Deuteronomy: ("Второзаконие",),

    # Historical
    BibleBookEnum.Joshua: ("Иисус Навин", "Книга Иисуса Навина"),
    BibleBookEnum.Judges: ("Судьи", "Книга Судей", "Книга Судей Израилевых"),
    BibleBookEnum.Ruth: ("Руфь", "Книга Руфи"),

    # Russian/Synodal practice also uses 1–4 Царств for Samuel+Kings
    BibleBookEnum.FirstSamuel: ("1 Самуила", "1-я книга Самуила", "1 Царств", "Первая книга Царств"),
    BibleBookEnum.SecondSamuel: ("2 Самуила", "2-я книга Самуила", "2 Царств", "Вторая книга Царств"),
    BibleBookEnum.FirstKings: ("1 Царей", "3 Царств", "Третья книга Царств"),
    BibleBookEnum.SecondKings: ("2 Царей", "4 Царств", "Четвертая книга Царств", "Четвёртая книга Царств"),

    BibleBookEnum.FirstChronicles: (
        "1 Паралипоменон", "Первая книга Паралипоменон",
        "1 Хроник", "Первая книга Хроник"
    ),
    BibleBookEnum.SecondChronicles: (
        "2 Паралипоменон", "Вторая книга Паралипоменон",
        "2 Хроник", "Вторая книга Хроник"
    ),

    # Ezra/Nehemiah/Esdras numbering in Russian Orthodox/Synodal tables:
    # canonical Ezra = 1 Ездры; apocryphal = 2 Ездры, 3 Ездры. citeturn1view0turn1view1turn2view0
    BibleBookEnum.Ezra: ("Ездра", "Книга Ездры", "1 Ездры", "Первая книга Ездры"),
    BibleBookEnum.Nehemiah: ("Неемия", "Книга Неемии"),
    BibleBookEnum.Esther: ("Есфирь", "Эсфирь", "Книга Есфири"),
    BibleBookEnum.Job: ("Иов", "Книга Иова"),

    # Wisdom/Poetry
    BibleBookEnum.Psalms: ("Псалтирь", "Псалмы"),
    BibleBookEnum.Proverbs: ("Притчи", "Притчи Соломона", "Книга Притчей"),
    BibleBookEnum.Ecclesiastes: ("Екклесиаст", "Проповедник"),
    BibleBookEnum.SongOfSolomon: ("Песнь Песней", "Песнь песней", "Песня песней"),

    # Prophets
    BibleBookEnum.Isaiah: ("Исаия", "Книга пророка Исаии"),
    BibleBookEnum.Jeremiah: ("Иеремия", "Книга пророка Иеремии"),
    BibleBookEnum.Lamentations: ("Плач Иеремии", "Плач"),
    BibleBookEnum.Ezekiel: ("Иезекииль", "Книга пророка Иезекииля"),
    BibleBookEnum.Daniel: ("Даниил", "Книга пророка Даниила"),

    BibleBookEnum.Hosea: ("Осия", "Книга пророка Осии"),
    BibleBookEnum.Joel: ("Иоиль", "Книга пророка Иоиля"),
    BibleBookEnum.Amos: ("Амос", "Книга пророка Амоса"),
    BibleBookEnum.Obadiah: ("Авдий", "Книга пророка Авдия"),
    BibleBookEnum.Jonah: ("Иона", "Книга пророка Ионы"),
    BibleBookEnum.Micah: ("Михей", "Книга пророка Михея"),
    BibleBookEnum.Nahum: ("Наум", "Книга пророка Наума"),
    BibleBookEnum.Habakkuk: ("Аввакум", "Книга пророка Аввакума"),
    BibleBookEnum.Zephaniah: ("Софония", "Книга пророка Софонии"),
    BibleBookEnum.Haggai: ("Аггей", "Книга пророка Аггея"),
    BibleBookEnum.Zechariah: ("Захария", "Книга пророка Захарии"),
    BibleBookEnum.Malachi: ("Малахия", "Книга пророка Малахии"),

    # Gospels & Acts
    BibleBookEnum.Matthew: ("Матфея", "Евангелие от Матфея", "От Матфея"),
    BibleBookEnum.Mark: ("Марка", "Евангелие от Марка", "От Марка"),
    BibleBookEnum.Luke: ("Луки", "Евангелие от Луки", "От Луки"),
    BibleBookEnum.John: ("Иоанна", "Евангелие от Иоанна", "От Иоанна"),
    BibleBookEnum.Acts: ("Деяния", "Деяния Апостолов", "Деяния святых Апостолов"),

    # Epistles
    BibleBookEnum.Romans: ("Римлянам", "Послание к Римлянам"),
    BibleBookEnum.FirstCorinthians: ("1 Коринфянам", "Первое послание к Коринфянам"),
    BibleBookEnum.SecondCorinthians: ("2 Коринфянам", "Второе послание к Коринфянам"),
    BibleBookEnum.Galatians: ("Галатам", "Послание к Галатам"),
    BibleBookEnum.Ephesians: ("Ефесянам", "Послание к Ефесянам"),
    BibleBookEnum.Philippians: ("Филиппийцам", "Послание к Филиппийцам"),
    BibleBookEnum.Colossians: ("Колоссянам", "Послание к Колоссянам"),
    BibleBookEnum.FirstThessalonians: ("1 Фессалоникийцам", "1 Солунянам"),
    BibleBookEnum.SecondThessalonians: ("2 Фессалоникийцам", "2 Солунянам"),
    BibleBookEnum.FirstTimothy: ("1 Тимофею", "Первое послание к Тимофею"),
    BibleBookEnum.SecondTimothy: ("2 Тимофею", "Второе послание к Тимофею"),
    BibleBookEnum.Titus: ("Титу", "Послание к Титу"),
    BibleBookEnum.Philemon: ("Филимону", "Послание к Филимону"),
    BibleBookEnum.Hebrews: ("Евреям", "Послание к Евреям"),

    BibleBookEnum.James: ("Иакова", "Послание Иакова"),
    BibleBookEnum.FirstPeter: ("1 Петра", "Первое послание Петра"),
    BibleBookEnum.SecondPeter: ("2 Петра", "Второе послание Петра"),
    BibleBookEnum.FirstJohn: ("1 Иоанна", "Первое послание Иоанна"),
    BibleBookEnum.SecondJohn: ("2 Иоанна", "Второе послание Иоанна"),
    BibleBookEnum.ThirdJohn: ("3 Иоанна", "Третье послание Иоанна"),
    BibleBookEnum.Jude: ("Иуды", "Послание Иуды"),

    BibleBookEnum.Revelation: ("Откровение", "Откровение Иоанна Богослова", "Апокалипсис"),

    # Deuterocanon / Apocrypha (common Russian names)
    BibleBookEnum.Tobit: ("Товит", "Книга Товита"),
    BibleBookEnum.Judith: ("Иудифь", "Книга Иудифи"),
    BibleBookEnum.Wisdom: ("Премудрость Соломона", "Книга Премудрости Соломона"),
    BibleBookEnum.Sirach: ("Премудрость Иисуса, сына Сирахова", "Сирах", "Книга Сираха"),
    BibleBookEnum.Baruch: ("Варух", "Книга Варуха"),
    BibleBookEnum.FirstMaccabees: ("1 Маккавейская", "Первая книга Маккавейская"),
    BibleBookEnum.SecondMaccabees: ("2 Маккавейская", "Вторая книга Маккавейская"),
    BibleBookEnum.ThirdMaccabees: ("3 Маккавейская", "Третья книга Маккавейская"),
    BibleBookEnum.FourthMaccabees: ("4 Маккавейская", "Четвертая книга Маккавейская", "Четвёртая книга Маккавейская"),

    # Additions / extras (highly variant; keep explicit Russian titles)
    BibleBookEnum.EstherAdditions: ("Есфирь (греческая)", "Есфирь (добавления)", "Есфирь (LXX)"),
    BibleBookEnum.DanielSongOfThree: ("Песнь трёх отроков", "Песнь трех отроков", "Молитва Азарии и песнь трёх отроков"),
    BibleBookEnum.DanielSusanna: ("Сусанна", "Даниил (Сусанна)"),
    BibleBookEnum.DanielBelAndTheDragon: ("Вил и дракон", "Бел и дракон", "Даниил (Вил и дракон)"),

    # Apocryphal Esdras in Russian Orthodox/Synodal naming
    BibleBookEnum.FirstEsdras: ("2 Ездры", "Вторая книга Ездры"),
    BibleBookEnum.SecondEsdras: ("3 Ездры", "Третья книга Ездры"),

    BibleBookEnum.PrayerOfManasseh: ("Молитва Манассии", "Молитва Манассии, царя Иудейского"),
    BibleBookEnum.Psalm151: ("Псалом 151", "Псалтирь (Псалом 151)"),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    # Pentateuch (Russian)
    BibleBookEnum.Genesis: ("быт", "бт"),
    BibleBookEnum.Exodus: ("исх", "ид"),
    BibleBookEnum.Leviticus: ("лев", "лв"),
    BibleBookEnum.Numbers: ("чис", "чс", "числ"),
    BibleBookEnum.Deuteronomy: ("вт", "втор"),

    # History
    BibleBookEnum.Joshua: ("нв", "нав", "иснав", "иош"),
    BibleBookEnum.Judges: ("сд", "суд", "судей"),
    BibleBookEnum.Ruth: ("рф", "руф", "руфь"),

    # Samuel + Kings: support both “Сам” and “Цар/Царств” citation systems
    BibleBookEnum.FirstSamuel: ("1цар", "1ц", "1сам", "iсам"),
    BibleBookEnum.SecondSamuel: ("2цар", "2ц", "2сам", "iiсам"),
    BibleBookEnum.FirstKings: ("3цар", "3ц", "1царей", "1цр"),
    BibleBookEnum.SecondKings: ("4цар", "4ц", "2царей", "2цр"),

    BibleBookEnum.FirstChronicles: ("1пар", "1пар.", "1par"),
    BibleBookEnum.SecondChronicles: ("2пар", "2пар.", "2par"),

    # Ezra/Nehemiah/Esther
    BibleBookEnum.Ezra: ("1езд", "езд"),
    BibleBookEnum.Nehemiah: ("неем", "нм"),
    BibleBookEnum.Esther: ("есф", "ес"),

    BibleBookEnum.Job: ("иов",),

    # Wisdom/Poetry
    BibleBookEnum.Psalms: ("пс", "псал"),
    BibleBookEnum.Proverbs: ("пр", "прит", "притч"),
    BibleBookEnum.Ecclesiastes: ("ек", "еккл"),
    BibleBookEnum.SongOfSolomon: ("пес", "песн"),

    # Major prophets
    BibleBookEnum.Isaiah: ("ис", "исаи"),
    BibleBookEnum.Jeremiah: ("иер",),
    BibleBookEnum.Lamentations: ("пл", "плач"),
    BibleBookEnum.Ezekiel: ("иез",),
    BibleBookEnum.Daniel: ("дан",),

    # Minor prophets
    BibleBookEnum.Hosea: ("ос",),
    BibleBookEnum.Joel: ("иол", "иоил"),
    BibleBookEnum.Amos: ("ам",),
    BibleBookEnum.Obadiah: ("авд",),
    BibleBookEnum.Jonah: ("ион",),
    BibleBookEnum.Micah: ("мих",),
    BibleBookEnum.Nahum: ("наум",),
    BibleBookEnum.Habakkuk: ("авв",),
    BibleBookEnum.Zephaniah: ("соф",),
    BibleBookEnum.Haggai: ("агг", "аг"),
    BibleBookEnum.Zechariah: ("зах",),
    BibleBookEnum.Malachi: ("мал",),

    # Gospels & Acts
    BibleBookEnum.Matthew: ("мф", "мат", "матф"),
    BibleBookEnum.Mark: ("мк", "мр"),
    BibleBookEnum.Luke: ("лк", "лук"),
    BibleBookEnum.John: ("ин", "иоан", "инн"),
    BibleBookEnum.Acts: ("де", "деян"),

    # Epistles
    BibleBookEnum.Romans: ("рим",),
    BibleBookEnum.FirstCorinthians: ("1кор", "1кор.", "1 кор"),
    BibleBookEnum.SecondCorinthians: ("2кор", "2кор.", "2 кор"),
    BibleBookEnum.Galatians: ("гал", "галл"),
    BibleBookEnum.Ephesians: ("еф",),
    BibleBookEnum.Philippians: ("флп",),
    BibleBookEnum.Colossians: ("кол",),
    BibleBookEnum.FirstThessalonians: ("1фес", "1сол"),
    BibleBookEnum.SecondThessalonians: ("2фес", "2сол"),
    BibleBookEnum.FirstTimothy: ("1тим",),
    BibleBookEnum.SecondTimothy: ("2тим",),
    BibleBookEnum.Titus: ("тит",),
    BibleBookEnum.Philemon: ("флм",),
    BibleBookEnum.Hebrews: ("евр",),
    BibleBookEnum.James: ("иак", "ик"),
    BibleBookEnum.FirstPeter: ("1пет",),
    BibleBookEnum.SecondPeter: ("2пет",),
    BibleBookEnum.FirstJohn: ("1ин",),
    BibleBookEnum.SecondJohn: ("2ин",),
    BibleBookEnum.ThirdJohn: ("3ин",),
    BibleBookEnum.Jude: ("иуд",),

    BibleBookEnum.Revelation: ("от", "откр", "апок"),

    # Deuterocanon / Apocrypha (Russian)
    BibleBookEnum.Tobit: ("тов",),
    BibleBookEnum.Judith: ("иудиф",),
    BibleBookEnum.Wisdom: ("прем",),
    BibleBookEnum.Sirach: ("сир",),
    BibleBookEnum.Baruch: ("вар",),

    BibleBookEnum.FirstMaccabees: ("1мак",),
    BibleBookEnum.SecondMaccabees: ("2мак",),
    BibleBookEnum.ThirdMaccabees: ("3мак",),
    BibleBookEnum.FourthMaccabees: ("4мак",),

    # Additions / extras
    # Russian short forms are not as standardized; prefer explicit tokens + stable IDs in your parser.
    BibleBookEnum.EstherAdditions: ("есф(гр)", "ESG", "EsthGr"),
    BibleBookEnum.DanielSongOfThree: ("песньтрехотроков", "S3Y", "PrAzar"),
    BibleBookEnum.DanielSusanna: ("сусанна", "SUS", "Sus"),
    BibleBookEnum.DanielBelAndTheDragon: ("вил", "бел", "BEL", "Bel"),

    # Apocryphal Esdras numbering (Russian Orthodox/Synodal)
    BibleBookEnum.FirstEsdras: ("2езд", "2 ез", "1ES", "1Esd"),
    BibleBookEnum.SecondEsdras: ("3езд", "3 ез", "2ES", "2Esd"),

    BibleBookEnum.PrayerOfManasseh: ("молитваман", "MAN", "PrMan"),
    BibleBookEnum.Psalm151: ("пс151", "PS2", "AddPs"),
}
