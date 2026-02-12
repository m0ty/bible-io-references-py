import re
from typing import Dict, Iterable

from .bible_book_enums import BibleBookEnum


class ParseVerseRefError(ValueError):
    """Error raised when parsing a verse reference string fails."""

    def __str__(self) -> str:
        return "invalid verse reference"


_VERSE_REF_PATTERN = re.compile(
    r"^\s*(?P<book>.+?)\s+(?P<chapter>\d+)\s*:\s*(?P<verse>\d+)\s*$"
)

# Localized full book names grouped by language.
_BOOK_NAMES_BY_LANGUAGE: Dict[str, Dict[BibleBookEnum, Iterable[str]]] = {
    "ru": {
        BibleBookEnum.Genesis: ("Бытие",),
        BibleBookEnum.Exodus: ("Исход",),
        BibleBookEnum.Leviticus: ("Левит",),
        BibleBookEnum.Numbers: ("Числа",),
        BibleBookEnum.Deuteronomy: ("Второзаконие",),
        BibleBookEnum.Joshua: ("Иисус Навин",),
        BibleBookEnum.Judges: ("Судьи",),
        BibleBookEnum.Ruth: ("Руфь",),
        BibleBookEnum.FirstSamuel: ("1 Самуила",),
        BibleBookEnum.SecondSamuel: ("2 Самуила",),
        BibleBookEnum.FirstKings: ("1 Царей",),
        BibleBookEnum.SecondKings: ("2 Царей",),
        BibleBookEnum.FirstChronicles: ("1 Паралипоменон",),
        BibleBookEnum.SecondChronicles: ("2 Паралипоменон",),
        BibleBookEnum.Ezra: ("Ездра",),
        BibleBookEnum.Nehemiah: ("Неемия",),
        BibleBookEnum.Esther: ("Есфирь",),
        BibleBookEnum.Job: ("Иов",),
        BibleBookEnum.Psalms: ("Псалтирь",),
        BibleBookEnum.Proverbs: ("Притчи",),
        BibleBookEnum.Ecclesiastes: ("Екклесиаст",),
        BibleBookEnum.SongOfSolomon: ("Песнь Песней",),
        BibleBookEnum.Isaiah: ("Исаия",),
        BibleBookEnum.Jeremiah: ("Иеремия",),
        BibleBookEnum.Lamentations: ("Плач Иеремии",),
        BibleBookEnum.Ezekiel: ("Иезекииль",),
        BibleBookEnum.Daniel: ("Даниил",),
        BibleBookEnum.Hosea: ("Осия",),
        BibleBookEnum.Joel: ("Иоиль",),
        BibleBookEnum.Amos: ("Амос",),
        BibleBookEnum.Obadiah: ("Авдий",),
        BibleBookEnum.Jonah: ("Иона",),
        BibleBookEnum.Micah: ("Михей",),
        BibleBookEnum.Nahum: ("Наум",),
        BibleBookEnum.Habakkuk: ("Аввакум",),
        BibleBookEnum.Zephaniah: ("Софония",),
        BibleBookEnum.Haggai: ("Аггей",),
        BibleBookEnum.Zechariah: ("Захария",),
        BibleBookEnum.Malachi: ("Малахия",),
        BibleBookEnum.Matthew: ("Матфея",),
        BibleBookEnum.Mark: ("Марка",),
        BibleBookEnum.Luke: ("Луки",),
        BibleBookEnum.John: ("Иоанна",),
        BibleBookEnum.Acts: ("Деяния",),
        BibleBookEnum.Romans: ("Римлянам",),
        BibleBookEnum.FirstCorinthians: ("1 Коринфянам",),
        BibleBookEnum.SecondCorinthians: ("2 Коринфянам",),
        BibleBookEnum.Galatians: ("Галатам",),
        BibleBookEnum.Ephesians: ("Ефесянам",),
        BibleBookEnum.Philippians: ("Филиппийцам",),
        BibleBookEnum.Colossians: ("Колоссянам",),
        BibleBookEnum.FirstThessalonians: ("1 Фессалоникийцам",),
        BibleBookEnum.SecondThessalonians: ("2 Фессалоникийцам",),
        BibleBookEnum.FirstTimothy: ("1 Тимофею",),
        BibleBookEnum.SecondTimothy: ("2 Тимофею",),
        BibleBookEnum.Titus: ("Титу",),
        BibleBookEnum.Philemon: ("Филимону",),
        BibleBookEnum.Hebrews: ("Евреям",),
        BibleBookEnum.James: ("Иакова",),
        BibleBookEnum.FirstPeter: ("1 Петра",),
        BibleBookEnum.SecondPeter: ("2 Петра",),
        BibleBookEnum.FirstJohn: ("1 Иоанна",),
        BibleBookEnum.SecondJohn: ("2 Иоанна",),
        BibleBookEnum.ThirdJohn: ("3 Иоанна",),
        BibleBookEnum.Jude: ("Иуды",),
        BibleBookEnum.Revelation: ("Откровение",),
    },
    "he": {
        BibleBookEnum.Genesis: ("בראשית",),
        BibleBookEnum.Exodus: ("שמות",),
        BibleBookEnum.Leviticus: ("ויקרא",),
        BibleBookEnum.Numbers: ("במדבר",),
        BibleBookEnum.Deuteronomy: ("דברים",),
        BibleBookEnum.Joshua: ("יהושע",),
        BibleBookEnum.Judges: ("שופטים",),
        BibleBookEnum.Ruth: ("רות",),
        BibleBookEnum.FirstSamuel: ("שמואל א",),
        BibleBookEnum.SecondSamuel: ("שמואל ב",),
        BibleBookEnum.FirstKings: ("מלכים א",),
        BibleBookEnum.SecondKings: ("מלכים ב",),
        BibleBookEnum.FirstChronicles: ("דברי הימים א",),
        BibleBookEnum.SecondChronicles: ("דברי הימים ב",),
        BibleBookEnum.Ezra: ("עזרא",),
        BibleBookEnum.Nehemiah: ("נחמיה",),
        BibleBookEnum.Esther: ("אסתר",),
        BibleBookEnum.Job: ("איוב",),
        BibleBookEnum.Psalms: ("תהילים",),
        BibleBookEnum.Proverbs: ("משלי",),
        BibleBookEnum.Ecclesiastes: ("קהלת",),
        BibleBookEnum.SongOfSolomon: ("שיר השירים",),
        BibleBookEnum.Isaiah: ("ישעיהו",),
        BibleBookEnum.Jeremiah: ("ירמיהו",),
        BibleBookEnum.Lamentations: ("איכה",),
        BibleBookEnum.Ezekiel: ("יחזקאל",),
        BibleBookEnum.Daniel: ("דניאל",),
        BibleBookEnum.Hosea: ("הושע",),
        BibleBookEnum.Joel: ("יואל",),
        BibleBookEnum.Amos: ("עמוס",),
        BibleBookEnum.Obadiah: ("עובדיה",),
        BibleBookEnum.Jonah: ("יונה",),
        BibleBookEnum.Micah: ("מיכה",),
        BibleBookEnum.Nahum: ("נחום",),
        BibleBookEnum.Habakkuk: ("חבקוק",),
        BibleBookEnum.Zephaniah: ("צפניה",),
        BibleBookEnum.Haggai: ("חגי",),
        BibleBookEnum.Zechariah: ("זכריה",),
        BibleBookEnum.Malachi: ("מלאכי",),
        BibleBookEnum.Matthew: ("מתי",),
        BibleBookEnum.Mark: ("מרקוס",),
        BibleBookEnum.Luke: ("לוקס",),
        BibleBookEnum.John: ("יוחנן",),
        BibleBookEnum.Acts: ("מעשי השליחים",),
        BibleBookEnum.Romans: ("רומים",),
        BibleBookEnum.FirstCorinthians: ("קורינתים א",),
        BibleBookEnum.SecondCorinthians: ("קורינתים ב",),
        BibleBookEnum.Galatians: ("גלטים",),
        BibleBookEnum.Ephesians: ("אפסים",),
        BibleBookEnum.Philippians: ("פיליפים",),
        BibleBookEnum.Colossians: ("קולוסים",),
        BibleBookEnum.FirstThessalonians: ("תסלוניקים א",),
        BibleBookEnum.SecondThessalonians: ("תסלוניקים ב",),
        BibleBookEnum.FirstTimothy: ("טימותיוס א",),
        BibleBookEnum.SecondTimothy: ("טימותיוס ב",),
        BibleBookEnum.Titus: ("טיטוס",),
        BibleBookEnum.Philemon: ("פילימון",),
        BibleBookEnum.Hebrews: ("עברים",),
        BibleBookEnum.James: ("יעקב",),
        BibleBookEnum.FirstPeter: ("פטרוס א",),
        BibleBookEnum.SecondPeter: ("פטרוס ב",),
        BibleBookEnum.FirstJohn: ("יוחנן א",),
        BibleBookEnum.SecondJohn: ("יוחנן ב",),
        BibleBookEnum.ThirdJohn: ("יוחנן ג",),
        BibleBookEnum.Jude: ("יהודה",),
        BibleBookEnum.Revelation: ("ההתגלות",),
    },
    "es": {
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
    },
    "pt": {
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
    },
}

# Localized abbreviations grouped by language.
_BOOK_ABBREVIATIONS_BY_LANGUAGE: Dict[str, Dict[BibleBookEnum, Iterable[str]]] = {
    "ru": {
        BibleBookEnum.Genesis: ("быт",),
        BibleBookEnum.Exodus: ("исх",),
        BibleBookEnum.Leviticus: ("лев",),
        BibleBookEnum.Numbers: ("чис",),
        BibleBookEnum.Deuteronomy: ("втор",),
        BibleBookEnum.Psalms: ("пс",),
        BibleBookEnum.Proverbs: ("прит",),
        BibleBookEnum.Isaiah: ("ис",),
        BibleBookEnum.Matthew: ("мф",),
        BibleBookEnum.Mark: ("мк",),
        BibleBookEnum.Luke: ("лк",),
        BibleBookEnum.John: ("ин", "инн"),
        BibleBookEnum.Acts: ("деян",),
        BibleBookEnum.Romans: ("рим",),
        BibleBookEnum.FirstCorinthians: ("1кор",),
        BibleBookEnum.SecondCorinthians: ("2кор",),
        BibleBookEnum.Galatians: ("гал",),
        BibleBookEnum.Ephesians: ("еф",),
        BibleBookEnum.Philippians: ("флп",),
        BibleBookEnum.Colossians: ("кол",),
        BibleBookEnum.FirstThessalonians: ("1фес",),
        BibleBookEnum.SecondThessalonians: ("2фес",),
        BibleBookEnum.FirstTimothy: ("1тим",),
        BibleBookEnum.SecondTimothy: ("2тим",),
        BibleBookEnum.Titus: ("тит",),
        BibleBookEnum.Philemon: ("флм",),
        BibleBookEnum.Hebrews: ("евр",),
        BibleBookEnum.James: ("иак",),
        BibleBookEnum.FirstPeter: ("1пет",),
        BibleBookEnum.SecondPeter: ("2пет",),
        BibleBookEnum.FirstJohn: ("1ин",),
        BibleBookEnum.SecondJohn: ("2ин",),
        BibleBookEnum.ThirdJohn: ("3ин",),
        BibleBookEnum.Jude: ("иуд",),
        BibleBookEnum.Revelation: ("откр",),
    },
    "he": {
        BibleBookEnum.Psalms: ("תה",),
        BibleBookEnum.Matthew: ("מתי",),
        BibleBookEnum.Mark: ("מרק",),
        BibleBookEnum.Luke: ("לוק",),
        BibleBookEnum.John: ("יוח", "יוחנ"),
    },
    "es": {
        BibleBookEnum.Matthew: ("mat",),
        BibleBookEnum.Luke: ("luc",),
        BibleBookEnum.John: ("juan",),
        BibleBookEnum.Revelation: ("apoc",),
    },
    "pt": {
        BibleBookEnum.John: ("joao",),
        BibleBookEnum.Revelation: ("apoc",),
    },
}


def _register_book_terms(
    table: Dict[str, BibleBookEnum],
    source: Dict[str, Dict[BibleBookEnum, Iterable[str]]],
) -> None:
    for books_for_language in source.values():
        for book, terms in books_for_language.items():
            for term in terms:
                table[term.casefold()] = book


# Centralized lookup table used by parsing logic.
_BOOK_NAME_TO_ENUM: Dict[str, BibleBookEnum] = {
    book.full_name.casefold(): book for book in BibleBookEnum
}
_register_book_terms(_BOOK_NAME_TO_ENUM, _BOOK_NAMES_BY_LANGUAGE)
_register_book_terms(_BOOK_NAME_TO_ENUM, _BOOK_ABBREVIATIONS_BY_LANGUAGE)


class VerseRef:
    def __init__(self, book_enum: BibleBookEnum, chapter: int, verse: int):
        self.book = book_enum
        self.chapter = chapter
        self.verse = verse

    def __str__(self) -> str:
        return f"{self.book.full_name} {self.chapter}:{self.verse}"

    @classmethod
    def from_str(cls, ref: str) -> "VerseRef":
        """Parse a verse reference string like ``John 3:16`` into a VerseRef."""
        if not isinstance(ref, str) or not ref:
            raise ParseVerseRefError()

        match = _VERSE_REF_PATTERN.match(ref)
        if not match:
            raise ParseVerseRefError()

        try:
            chapter = int(match.group("chapter"))
            verse = int(match.group("verse"))
        except ValueError as e:
            raise ParseVerseRefError() from e

        if chapter <= 0 or verse <= 0:
            raise ParseVerseRefError()

        book = _parse_book_name(match.group("book"))
        return cls(book_enum=book, chapter=chapter, verse=verse)


def _parse_book_name(book_text: str) -> BibleBookEnum:
    normalized = " ".join(book_text.split()).casefold()
    if not normalized:
        raise ParseVerseRefError()

    direct = _BOOK_NAME_TO_ENUM.get(normalized)
    if direct is not None:
        return direct

    normalized_without_period = normalized.replace(".", "")
    without_period = _BOOK_NAME_TO_ENUM.get(normalized_without_period)
    if without_period is not None:
        return without_period

    compact = normalized_without_period.replace(" ", "")
    compact_match = _BOOK_NAME_TO_ENUM.get(compact)
    if compact_match is not None:
        return compact_match

    try:
        return BibleBookEnum.from_str(compact)
    except ValueError as e:
        raise ParseVerseRefError() from e


class VerseRangeRef:
    def __init__(self, start: VerseRef, end: VerseRef):
        self.start = start
        self.end = end

    def __str__(self) -> str:
        if self.start.book == self.end.book:
            book_name = self.start.book.full_name
            if self.start.chapter == self.end.chapter:
                return (
                    f"{book_name} {self.start.chapter}:{self.start.verse}"
                    f"-{self.end.verse}"
                )
            return (
                f"{book_name} {self.start.chapter}:{self.start.verse}"
                f"-{self.end.chapter}:{self.end.verse}"
            )
        return (
            f"{self.start.book.full_name} {self.start.chapter}:{self.start.verse}"
            f"-{self.end.book.full_name} {self.end.chapter}:{self.end.verse}"
        )
