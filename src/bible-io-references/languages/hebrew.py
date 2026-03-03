from typing import Dict, Iterable
from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    # Tanakh
    BibleBookEnum.Genesis: ("בראשית",),
    BibleBookEnum.Exodus: ("שמות",),
    BibleBookEnum.Leviticus: ("ויקרא",),
    BibleBookEnum.Numbers: ("במדבר",),
    BibleBookEnum.Deuteronomy: ("דברים",),

    BibleBookEnum.Joshua: ("יהושע",),
    BibleBookEnum.Judges: ("שופטים",),
    BibleBookEnum.Ruth: ("רות",),

    BibleBookEnum.FirstSamuel: ("שמואל א", "שמואל א׳", "שמואל א'"),
    BibleBookEnum.SecondSamuel: ("שמואל ב", "שמואל ב׳", "שמואל ב'"),
    BibleBookEnum.FirstKings: ("מלכים א", "מלכים א׳", "מלכים א'"),
    BibleBookEnum.SecondKings: ("מלכים ב", "מלכים ב׳", "מלכים ב'"),

    BibleBookEnum.FirstChronicles: ("דברי הימים א", "דברי הימים א׳", "דברי הימים א'"),
    BibleBookEnum.SecondChronicles: ("דברי הימים ב", "דברי הימים ב׳", "דברי הימים ב'"),

    BibleBookEnum.Ezra: ("עזרא",),
    BibleBookEnum.Nehemiah: ("נחמיה",),
    BibleBookEnum.Esther: ("אסתר", "מגילת אסתר"),

    BibleBookEnum.Job: ("איוב",),
    BibleBookEnum.Psalms: ("תהילים", "תהלים", "ספר תהילים"),
    BibleBookEnum.Proverbs: ("משלי",),
    BibleBookEnum.Ecclesiastes: ("קהלת",),
    BibleBookEnum.SongOfSolomon: ("שיר השירים",),

    BibleBookEnum.Isaiah: ("ישעיהו", "ישעיה"),
    BibleBookEnum.Jeremiah: ("ירמיהו", "ירמיה"),
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

    # New Testament (Hebrew)
    BibleBookEnum.Matthew: ("מתי", "הבשורה על־פי מתי", "הבשורה על פי מתי", "מתיו"),
    BibleBookEnum.Mark: ("מרקוס", "מרק", "הבשורה על־פי מרקוס", "הבשורה על פי מרקוס"),
    BibleBookEnum.Luke: ("לוקס", "לוק", "לוקאס", "הבשורה על־פי לוקס", "הבשורה על פי לוקס"),
    BibleBookEnum.John: ("יוחנן", "הבשורה על־פי יוחנן", "הבשורה על פי יוחנן"),

    BibleBookEnum.Acts: ("מעשי השליחים", "מעשי"),
    BibleBookEnum.Romans: ("רומים", "רומאים", "אל הרומיים", "אל הרומאים", "אגרת פולוס השליח אל־הרומיים"),

    BibleBookEnum.FirstCorinthians: ("קורינתים א", "קורינתיים א", "אגרת פולוס הראשונה אל־הקורנתים", "אגרת פולוס הראשונה אל־הקורנתיים"),
    BibleBookEnum.SecondCorinthians: ("קורינתים ב", "קורינתיים ב", "אגרת פולוס השנייה אל־הקורנתים", "אגרת פולוס השנייה אל־הקורנתיים"),

    BibleBookEnum.Galatians: ("גלטים", "גלטיים", "אל הגלטים", "אל הגלטיים"),
    BibleBookEnum.Ephesians: ("אפסים", "אפסיים", "אל האפסים", "אל האפסיים"),
    BibleBookEnum.Philippians: ("פיליפים", "פיליפיים", "אל הפיליפים", "אל הפיליפיים"),
    BibleBookEnum.Colossians: ("קולוסים", "קולוסיים", "אל הקולוסים", "אל הקולוסיים"),

    BibleBookEnum.FirstThessalonians: ("תסלוניקים א", "תסלוניקיים א", "אל התסלוניקים הראשונה", "אל התסלוניקיים הראשונה"),
    BibleBookEnum.SecondThessalonians: ("תסלוניקים ב", "תסלוניקיים ב", "אל התסלוניקים השנייה", "אל התסלוניקיים השנייה"),

    BibleBookEnum.FirstTimothy: ("טימותיוס א", "טימותיאוס א", "אל טימותיוס א", "אל טימותיאוס א"),
    BibleBookEnum.SecondTimothy: ("טימותיוס ב", "טימותיאוס ב", "אל טימותיוס ב", "אל טימותיאוס ב"),
    BibleBookEnum.Titus: ("טיטוס", "אל טיטוס"),
    BibleBookEnum.Philemon: ("פילימון", "פילמון", "אל פילימון", "אל פילמון"),
    BibleBookEnum.Hebrews: ("עברים", "עבריים", "אל העברים", "אל העבריים"),
    BibleBookEnum.James: ("יעקב", "יעקוב", "אגרת יעקב"),
    BibleBookEnum.FirstPeter: ("פטרוס א", "פטרוס א׳", "פטרוס א'", "כיפא א", "כיפא א׳", "כיפא א'"),
    BibleBookEnum.SecondPeter: ("פטרוס ב", "פטרוס ב׳", "פטרוס ב'", "כיפא ב", "כיפא ב׳", "כיפא ב'"),
    BibleBookEnum.FirstJohn: ("יוחנן א", "יוחנן א׳", "יוחנן א'", "אגרת יוחנן הראשונה"),
    BibleBookEnum.SecondJohn: ("יוחנן ב", "יוחנן ב׳", "יוחנן ב'", "אגרת יוחנן השנייה"),
    BibleBookEnum.ThirdJohn: ("יוחנן ג", "יוחנן ג׳", "יוחנן ג'", "אגרת יוחנן השלישית"),
    BibleBookEnum.Jude: ("יהודה", "אגרת יהודה"),
    BibleBookEnum.Revelation: ("התגלות", "ההתגלות", "חזון יוחנן", "חזון"),

    # Deuterocanon / Apocrypha in Hebrew usage
    BibleBookEnum.Tobit: ("טוביה", "ספר טוביה", "טובי", "ספר טובי", "טובית"),
    BibleBookEnum.Judith: ("יהודית", "ספר יהודית"),
    BibleBookEnum.Wisdom: ("חכמת שלמה", "ספר חכמת שלמה"),
    BibleBookEnum.Sirach: ("בן סירא", "בן־סירא", "ספר בן סירא", "ספר בן־סירא", "חכמת בן סירא", "חכמת בן־סירא"),
    BibleBookEnum.Baruch: ("ברוך", "ספר ברוך"),

    BibleBookEnum.FirstMaccabees: ("מקבים א", "מקבים א׳", "מקבים א'", "מכבים א", "חשמונאים א", "חשמונאים א׳", "חשמונאים א'"),
    BibleBookEnum.SecondMaccabees: ("מקבים ב", "מקבים ב׳", "מקבים ב'", "מכבים ב", "חשמונאים ב", "חשמונאים ב׳", "חשמונאים ב'"),
    BibleBookEnum.ThirdMaccabees: ("מקבים ג", "מקבים ג׳", "מקבים ג'", "מכבים ג"),
    BibleBookEnum.FourthMaccabees: ("מקבים ד", "מקבים ד׳", "מקבים ד'", "מכבים ד"),

    BibleBookEnum.EstherAdditions: ("תוספות למגילת אסתר", "תוספות לאסתר", "אסתר (יוונית)", "אסתר יוונית"),
    BibleBookEnum.DanielSongOfThree: ("תפילת עזריה", "תפילת עזריה ושירת שלושת האנשים", "שירת שלושת האנשים", "שירת שלושת הנערים", "תפילת עזריה ושיר שלושת האנשים בתוך הכבשן"),
    BibleBookEnum.DanielSusanna: ("שושנה", "מעשה שושנה", "דניאל (שושנה)"),
    BibleBookEnum.DanielBelAndTheDragon: ("בל והתנין", "בל והדרקון", "בל והדרקון", "דניאל (בל והדרקון)"),

    # IMPORTANT: Corrected to avoid clash with Ezra chapters; these are apocrypha names in Hebrew
    BibleBookEnum.FirstEsdras: ("עזרא החיצוני", "עזרא החיצון"),
    BibleBookEnum.SecondEsdras: ("חזון עזרא", "עזרא הרביעי", "עזרא ד׳", "עזרא ד'"),

    BibleBookEnum.PrayerOfManasseh: ("תפילת מנשה", "תפילת מנשה מלך יהודה"),
    BibleBookEnum.Psalm151: ("תהילים קנא", "תהלים קנא", "מזמור קנא", "תהילים 151", "תהלים 151"),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    # Tanakh – abbreviations from Hebrew reference lists (accept multiple punctuation variants)
    BibleBookEnum.Genesis: ("בר׳", "בר'", "בר"),
    BibleBookEnum.Exodus: ("שמ׳", "שמ'", "שמ"),
    BibleBookEnum.Leviticus: ("וי׳", "וי'", "ויק׳", "ויק'", "ויק"),
    BibleBookEnum.Numbers: ("במ׳", "במ'", "במד׳", "במד'", "במד"),
    BibleBookEnum.Deuteronomy: ("דב׳", "דב'", "דב"),

    BibleBookEnum.Joshua: ("יהו׳", "יהו'", "יהו"),
    BibleBookEnum.Judges: ("שו׳", "שו'", "שופ׳", "שופ'", "שופ"),
    BibleBookEnum.Ruth: ("רות",),

    BibleBookEnum.FirstSamuel: ("ש״א", "ש\"א", "שמ״א", "שמ\"א", "שמ א", "שמא"),
    BibleBookEnum.SecondSamuel: ("ש״ב", "ש\"ב", "שמ״ב", "שמ\"ב", "שמ ב", "שמב"),

    BibleBookEnum.FirstKings: ("מ״א", "מ\"א", "מל״א", "מל\"א", "מלא"),
    BibleBookEnum.SecondKings: ("מ״ב", "מ\"ב", "מל״ב", "מל\"ב", "מלב"),

    BibleBookEnum.FirstChronicles: ("דה״א", "דה\"א", "דבה״א", "דבה\"א"),
    BibleBookEnum.SecondChronicles: ("דה״ב", "דה\"ב", "דבה״ב", "דבה\"ב"),

    BibleBookEnum.Ezra: ("עז׳", "עז'", "עז"),
    BibleBookEnum.Nehemiah: ("נחמ׳", "נחמ'", "נחמ"),
    BibleBookEnum.Esther: ("אס׳", "אס'", "אס"),

    BibleBookEnum.Job: ("איוב", "אי׳", "אי'"),
    BibleBookEnum.Psalms: ("תה׳", "תה'", "תה", "תהל"),
    BibleBookEnum.Proverbs: ("מש׳", "מש'", "מש"),
    BibleBookEnum.Ecclesiastes: ("קה׳", "קה'", "קה"),
    BibleBookEnum.SongOfSolomon: ("שה״ש", "שה\"ש", "שהש"),

    BibleBookEnum.Isaiah: ("יש׳", "יש'", "יש"),
    BibleBookEnum.Jeremiah: ("יר׳", "יר'", "יר"),
    BibleBookEnum.Lamentations: ("איכה",),
    BibleBookEnum.Ezekiel: ("יח׳", "יח'", "יח"),
    BibleBookEnum.Daniel: ("דנ׳", "דנ'", "דנ"),

    BibleBookEnum.Hosea: ("הו׳", "הו'", "הו"),
    BibleBookEnum.Joel: ("יואל",),
    BibleBookEnum.Amos: ("עמ׳", "עמ'", "עמ"),
    BibleBookEnum.Obadiah: ("עו׳", "עו'", "עו"),
    BibleBookEnum.Jonah: ("יונה",),
    BibleBookEnum.Micah: ("מי׳", "מי'", "מי"),
    BibleBookEnum.Nahum: ("נח׳", "נח'", "נח"),
    BibleBookEnum.Habakkuk: ("חב׳", "חב'", "חב"),
    BibleBookEnum.Zephaniah: ("צפ׳", "צפ'", "צפ"),
    BibleBookEnum.Haggai: ("חגי",),
    BibleBookEnum.Zechariah: ("זכ׳", "זכ'", "זכ"),
    BibleBookEnum.Malachi: ("מל׳", "מל'", "מלכ"),

    # New Testament – common Hebrew user-entered abbreviations/codes
    BibleBookEnum.Matthew: ("מתי", "מתיו"),
    BibleBookEnum.Mark: ("מרק", "מרקוס"),
    BibleBookEnum.Luke: ("לוק", "לוקס", "לוקאס"),
    BibleBookEnum.John: ("יוח", "יוחנ", "יוחנן"),

    BibleBookEnum.Acts: ("מעש", "מעשי", "מעשי השליחים"),
    BibleBookEnum.Romans: ("רומ", "רומים", "רומאים"),

    BibleBookEnum.FirstCorinthians: ("קור-א", "קור״א", "קור\"א", "קורינתים א", "קורינתיים א"),
    BibleBookEnum.SecondCorinthians: ("קור-ב", "קור״ב", "קור\"ב", "קורינתים ב", "קורינתיים ב"),

    BibleBookEnum.Galatians: ("גלט", "גלטים", "גלטיים"),
    BibleBookEnum.Ephesians: ("אפס", "אפסים", "אפסיים"),
    BibleBookEnum.Philippians: ("פיליפ", "פיליפים", "פיליפיים"),
    BibleBookEnum.Colossians: ("קול", "קולוסים", "קולוסיים"),

    BibleBookEnum.FirstThessalonians: ("תסל-א", "תסל״א", "תסל\"א", "תסלוניקים א", "תסלוניקיים א"),
    BibleBookEnum.SecondThessalonians: ("תסל-ב", "תסל״ב", "תסל\"ב", "תסלוניקים ב", "תסלוניקיים ב"),

    BibleBookEnum.FirstTimothy: ("טימ-א", "טימ״א", "טימ\"א", "טימותיוס א", "טימותיאוס א"),
    BibleBookEnum.SecondTimothy: ("טימ-ב", "טימ״ב", "טימ\"ב", "טימותיוס ב", "טימותיאוס ב"),

    BibleBookEnum.Titus: ("טיט", "טיטוס"),
    BibleBookEnum.Philemon: ("פילימ", "פילמון", "פילימון"),
    BibleBookEnum.Hebrews: ("עבר", "עברים", "עבריים"),
    BibleBookEnum.James: ("יעקב", "יעקוב"),
    BibleBookEnum.FirstPeter: ("פטר-א", "פטר״א", "פטר\"א", "פטרוס א", "כיפא א"),
    BibleBookEnum.SecondPeter: ("פטר-ב", "פטר״ב", "פטר\"ב", "פטרוס ב", "כיפא ב"),

    BibleBookEnum.FirstJohn: ("יוח-א", "יוח״א", "יוח\"א", "יוחנן א"),
    BibleBookEnum.SecondJohn: ("יוח-ב", "יוח״ב", "יוח\"ב", "יוחנן ב"),
    BibleBookEnum.ThirdJohn: ("יוח-ג", "יוח״ג", "יוח\"ג", "יוחנן ג"),

    BibleBookEnum.Jude: ("יהד", "יהודה"),
    BibleBookEnum.Revelation: ("חזון", "התגלות", "ההתגלות"),

    # Deuterocanon / Additions – Hebrew short forms are not fully standardized; prefer full Hebrew names + tooling IDs
    BibleBookEnum.Tobit: ("טוביה", "טובי", "TOB", "Tob"),
    BibleBookEnum.Judith: ("יהודית", "JDT", "Jdt"),
    BibleBookEnum.Wisdom: ("חכמת שלמה", "WIS", "Wis"),
    BibleBookEnum.Sirach: ("בן סירא", "SIR", "Sir"),
    BibleBookEnum.Baruch: ("ברוך", "BAR", "Bar"),

    BibleBookEnum.FirstMaccabees: ("מקבים א", "מכבים א", "חשמונאים א", "1MA", "1Macc"),
    BibleBookEnum.SecondMaccabees: ("מקבים ב", "מכבים ב", "חשמונאים ב", "2MA", "2Macc"),
    BibleBookEnum.ThirdMaccabees: ("מקבים ג", "מכבים ג", "3MA", "3Macc"),
    BibleBookEnum.FourthMaccabees: ("מקבים ד", "מכבים ד", "4MA", "4Macc"),

    BibleBookEnum.EstherAdditions: ("תוספות לאסתר", "תוספות למגילת אסתר", "ESG", "EsthGr"),
    BibleBookEnum.DanielSongOfThree: ("תפילת עזריה", "שירת שלושת האנשים", "S3Y", "PrAzar"),
    BibleBookEnum.DanielSusanna: ("שושנה", "מעשה שושנה", "SUS", "Sus"),
    BibleBookEnum.DanielBelAndTheDragon: ("בל והתנין", "בל והדרקון", "BEL", "Bel"),

    # IMPORTANT: use distinct names to avoid collision with Ezra chapters
    BibleBookEnum.FirstEsdras: ("עזרא החיצוני", "1ES", "1Esd"),
    BibleBookEnum.SecondEsdras: ("חזון עזרא", "עזרא הרביעי", "2ES", "2Esd"),

    BibleBookEnum.PrayerOfManasseh: ("תפילת מנשה", "MAN", "PrMan"),
    BibleBookEnum.Psalm151: ("תהילים קנא", "תהלים קנא", "מזמור קנא", "PS2", "AddPs"),
}
