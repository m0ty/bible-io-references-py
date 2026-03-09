from typing import Dict, Iterable
from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    # Pentateuch
    BibleBookEnum.Genesis: ("उत्पत्ति", "उत्पत्ति ग्रन्थ"),
    BibleBookEnum.Exodus: ("निर्गमन", "निर्गमन ग्रन्थ"),
    BibleBookEnum.Leviticus: ("लैव्यव्यवस्था", "लैव्यवस्था", "लेवी", "लेवी ग्रन्थ"),
    BibleBookEnum.Numbers: ("गिनती", "गणना", "गणना ग्रन्थ"),
    BibleBookEnum.Deuteronomy: ("व्यवस्थाविवरण", "विधि-विवरण", "विधि-विवरण ग्रन्थ"),

    # History
    BibleBookEnum.Joshua: ("यहोशू", "योशुआ"),
    BibleBookEnum.Judges: ("न्यायियों", "न्यायकर्ता", "न्यायकर्ताओं का ग्रन्थ"),
    BibleBookEnum.Ruth: ("रूत", "रूत का ग्रन्थ"),

    BibleBookEnum.FirstSamuel: ("1 शमूएल", "समूएल का पहला ग्रन्थ"),
    BibleBookEnum.SecondSamuel: ("2 शमूएल", "समूएल का दूसरा ग्रन्थ"),

    BibleBookEnum.FirstKings: ("1 राजा", "राजाओं का पहला ग्रन्थ"),
    BibleBookEnum.SecondKings: ("2 राजा", "राजाओं का दूसरा ग्रन्थ"),

    BibleBookEnum.FirstChronicles: ("1 इतिहास", "पहला इतिहास ग्रन्थ"),
    BibleBookEnum.SecondChronicles: ("2 इतिहास", "दूसरा इतिहास ग्रन्थ"),

    BibleBookEnum.Ezra: ("एज्रा", "एज़्रा", "एज़्रा"),
    BibleBookEnum.Nehemiah: ("नहेमायाह", "नहेम्याह", "नहेम्या"),
    BibleBookEnum.Esther: ("एस्तेर", "एस्तेर का ग्रन्थ"),
    BibleBookEnum.Job: ("अय्यूब", "अय्यूब (योब)", "योब"),

    # Wisdom/Poetry
    BibleBookEnum.Psalms: ("भजन संहिता", "भजन", "स्तोत्र", "स्तोत्र ग्रन्थ"),
    BibleBookEnum.Proverbs: ("नीतिवचन", "सूक्ति ग्रन्थ", "सूक्ति संग्रह"),
    BibleBookEnum.Ecclesiastes: ("सभोपदेशक", "उपदेशक", "उपदेशक ग्रन्थ"),
    BibleBookEnum.SongOfSolomon: ("श्रेष्ठगीत", "सुलेमान का सर्वश्रेष्ठ गीत", "सर्वश्रेष्ठ गीत"),

    # Major prophets
    BibleBookEnum.Isaiah: ("यशायाह", "इसायाह"),
    BibleBookEnum.Jeremiah: ("यिर्मयाह", "यिरमियाह", "येरेमियाह"),
    BibleBookEnum.Lamentations: ("विलापगीत", "शोक गीत"),
    BibleBookEnum.Ezekiel: ("यहेजकेल", "एज़ेकिएल", "एज़ेकिएल"),
    BibleBookEnum.Daniel: ("दानिय्येल", "दानिएल"),

    # Minor prophets
    BibleBookEnum.Hosea: ("होशे", "होशेआ"),
    BibleBookEnum.Joel: ("योएल",),
    BibleBookEnum.Amos: ("आमोस",),
    BibleBookEnum.Obadiah: ("ओबद्याह", "ओबद्दाह", "ओबदयाह"),
    BibleBookEnum.Jonah: ("योना", "योनाह"),
    BibleBookEnum.Micah: ("मीका", "मीकाह"),
    BibleBookEnum.Nahum: ("नहूम",),
    BibleBookEnum.Habakkuk: ("हबक्कूक",),
    BibleBookEnum.Zephaniah: ("सपन्याह", "सफ़न्याह"),
    BibleBookEnum.Haggai: ("हाग्गै", "हग्गय"),
    BibleBookEnum.Zechariah: ("जकर्याह", "ज़कारिया", "जकरयाह"),
    BibleBookEnum.Malachi: ("मलाकी", "मलआकी"),

    # Gospels & Acts
    BibleBookEnum.Matthew: ("मत्ती", "सन्त मत्ती"),
    BibleBookEnum.Mark: ("मरकुस", "सन्त मारकुस"),
    BibleBookEnum.Luke: ("लूका", "सन्त लूकस", "लूकस"),
    BibleBookEnum.John: ("यूहन्ना", "सन्त योहन", "योहन"),

    BibleBookEnum.Acts: ("प्रेरितों के काम", "प्रेरित-चरित", "प्रेरितों"),
    BibleBookEnum.Romans: ("रोमियों", "रोमियो"),

    # Pauline epistles
    BibleBookEnum.FirstCorinthians: ("1 कुरिन्थियों", "1 कोरिंथियों"),
    BibleBookEnum.SecondCorinthians: ("2 कुरिन्थियों", "2 कोरिंथियों"),
    BibleBookEnum.Galatians: ("गलातियों", "गलातिया"),
    BibleBookEnum.Ephesians: ("इफिसियों", "एफ़ेसियों"),
    BibleBookEnum.Philippians: ("फिलिप्पियों", "फ़िलिप्पियों"),
    BibleBookEnum.Colossians: ("कुलुस्सियों", "कलोसियों"),

    BibleBookEnum.FirstThessalonians: ("1 थिस्सलुनीकियों", "1 थेसलनीकियों"),
    BibleBookEnum.SecondThessalonians: ("2 थिस्सलुनीकियों", "2 थेसलनीकियों"),

    BibleBookEnum.FirstTimothy: ("1 तीमुथियुस", "1 तिमथी"),
    BibleBookEnum.SecondTimothy: ("2 तीमुथियुस", "2 तिमथी"),

    BibleBookEnum.Titus: ("तीतुस", "तीतुस के नाम पत्र"),
    BibleBookEnum.Philemon: ("फिलेमोन", "फ़िलेमोन"),
    BibleBookEnum.Hebrews: ("इब्रानियों", "इब्रानीयोँ", "इब्री"),
    BibleBookEnum.James: ("याकूब",),
    BibleBookEnum.FirstPeter: ("1 पतरस",),
    BibleBookEnum.SecondPeter: ("2 पतरस",),
    BibleBookEnum.FirstJohn: ("1 यूहन्ना",),
    BibleBookEnum.SecondJohn: ("2 यूहन्ना",),
    BibleBookEnum.ThirdJohn: ("3 यूहन्ना",),
    BibleBookEnum.Jude: ("यहूदा", "यूदस"),
    BibleBookEnum.Revelation: ("प्रकाशितवाक्य", "प्रकाशित वाक्य", "प्रकाशन", "प्रकाशना-ग्रन्थ"),

    # Deuterocanon (Hindi Catholic naming is consistent across multiple sources)
    BibleBookEnum.Tobit: ("टोबीत", "टोबीत का ग्रन्थ"),
    BibleBookEnum.Judith: ("यूदीत", "यूदीत का ग्रन्थ"),
    BibleBookEnum.Wisdom: ("प्रज्ञा-ग्रन्थ", "प्रज्ञा ग्रन्थ"),
    BibleBookEnum.Sirach: ("प्रवक्ता-ग्रन्थ", "प्रवक्ता ग्रन्थ"),
    BibleBookEnum.Baruch: ("बारूक", "बारूक का ग्रन्थ"),

    BibleBookEnum.FirstMaccabees: ("मक्काबियों का पहला ग्रन्थ", "1 मक्काबियों"),
    BibleBookEnum.SecondMaccabees: ("मक्काबियों का दूसरा ग्रन्थ", "2 मक्काबियों"),

    # Low-standardization in Hindi: keep safe Hindi descriptors
    BibleBookEnum.ThirdMaccabees: ("3 मक्काबियों", "3 मक्काबियों का ग्रन्थ"),
    BibleBookEnum.FourthMaccabees: ("4 मक्काबियों", "4 मक्काबियों का ग्रन्थ"),

    BibleBookEnum.EstherAdditions: ("एस्तेर (यूनानी)", "एस्तेर (ग्रीक)", "एस्तेर की यूनानी परिशिष्ट"),
    BibleBookEnum.DanielSongOfThree: ("दानिय्येल (तीन युवकों का गीत)", "दानिय्येल (तीन जनों का गीत)"),
    BibleBookEnum.DanielSusanna: ("दानिय्येल (सुसन्ना)", "सुसन्ना"),
    BibleBookEnum.DanielBelAndTheDragon: ("दानिय्येल (बेल और अजगर)", "दानिय्येल (बेल और ड्रैगन)"),

    BibleBookEnum.FirstEsdras: ("1 एस्द्रास", "1 एज़्द्रास"),
    BibleBookEnum.SecondEsdras: ("2 एस्द्रास", "2 एज़्द्रास"),
    BibleBookEnum.PrayerOfManasseh: ("मनश्शे की प्रार्थना", "मनश्शे का प्रार्थना-गीत"),
    BibleBookEnum.Psalm151: ("भजन 151", "भजन संहिता 151"),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    # OT
    BibleBookEnum.Genesis: ("उत्प", "उत्प."),
    BibleBookEnum.Exodus: ("निर्ग", "निर्ग."),
    BibleBookEnum.Leviticus: ("लैव्य", "लैव्य.", "लेवी", "लेवी."),
    BibleBookEnum.Numbers: ("गिन", "गिन.", "गण", "गण."),
    BibleBookEnum.Deuteronomy: ("व्यव", "व्यव."),

    BibleBookEnum.Joshua: ("यहो", "यहो."),
    BibleBookEnum.Judges: ("न्यायि", "न्यायि."),
    BibleBookEnum.Ruth: ("रूत", "रूत."),

    BibleBookEnum.FirstSamuel: ("1शमू", "1 शमू", "1शमु", "1 शमु", "1शमू.", "1 शमू."),
    BibleBookEnum.SecondSamuel: ("2शमू", "2 शमू", "2शमु", "2 शमु", "2शमू.", "2 शमू."),

    BibleBookEnum.FirstKings: ("1राजा", "1 राजा", "1राजा.", "1 राजा."),
    BibleBookEnum.SecondKings: ("2राजा", "2 राजा", "2राजा.", "2 राजा."),

    BibleBookEnum.FirstChronicles: ("1इति", "1 इति", "1इति.", "1 इति."),
    BibleBookEnum.SecondChronicles: ("2इति", "2 इति", "2इति.", "2 इति."),

    BibleBookEnum.Ezra: ("एज्रा", "एज्रा.", "एज़्रा", "एज़्रा"),
    BibleBookEnum.Nehemiah: ("नहे", "नहे.", "नेहे", "नेहे."),
    BibleBookEnum.Esther: ("एस्ते", "एस्ते."),
    BibleBookEnum.Job: ("अय्यू", "अय्यू.", "अय्यो", "अय्यो."),

    BibleBookEnum.Psalms: ("भज", "भज.", "भजन", "भजन.", "स्तोत्र", "स्तोत्र."),
    BibleBookEnum.Proverbs: ("नीति", "नीति.", "सूक्ति", "सूक्ति."),
    BibleBookEnum.Ecclesiastes: ("सभो", "सभो."),
    BibleBookEnum.SongOfSolomon: ("श्रेष्ठ", "श्रेष्ठ."),

    BibleBookEnum.Isaiah: ("यशा", "यशा."),
    BibleBookEnum.Jeremiah: ("यिर्म", "यिर्म."),
    BibleBookEnum.Lamentations: ("विला", "विला."),
    BibleBookEnum.Ezekiel: ("यहे", "यहे."),
    BibleBookEnum.Daniel: ("दानि", "दानि."),

    BibleBookEnum.Hosea: ("होशे", "होशे."),
    BibleBookEnum.Joel: ("योए", "योए."),
    BibleBookEnum.Amos: ("आमो", "आमो."),
    BibleBookEnum.Obadiah: ("ओब", "ओब."),
    BibleBookEnum.Jonah: ("योना", "योना."),
    BibleBookEnum.Micah: ("मीका", "मीका."),
    BibleBookEnum.Nahum: ("नहू", "नहू."),
    BibleBookEnum.Habakkuk: ("हब", "हब."),
    BibleBookEnum.Zephaniah: ("सप", "सप."),
    BibleBookEnum.Haggai: ("हाग्गै", "हाग्गै.", "हग्गय", "हग्गय."),
    BibleBookEnum.Zechariah: ("जक", "जक."),
    BibleBookEnum.Malachi: ("मला", "मला."),

    # NT
    BibleBookEnum.Matthew: ("मत", "मत्ती", "मत्ती."),
    BibleBookEnum.Mark: ("मर", "मर."),
    BibleBookEnum.Luke: ("लूका", "लूका."),
    BibleBookEnum.John: ("यूह", "यूह."),

    BibleBookEnum.Acts: ("प्रेरि", "प्रेरि.", "प्रेरितों", "प्रेरितों."),
    BibleBookEnum.Romans: ("रोमि", "रोमि.", "रोम", "रोम."),

    BibleBookEnum.FirstCorinthians: ("1कुरि", "1 कुरि", "1कुरि.", "1 कुरि."),
    BibleBookEnum.SecondCorinthians: ("2कुरि", "2 कुरि", "2कुरि.", "2 कुरि."),

    BibleBookEnum.Galatians: ("गल", "गल."),
    BibleBookEnum.Ephesians: ("इफि", "इफि."),
    BibleBookEnum.Philippians: ("फिलि", "फिलि."),
    BibleBookEnum.Colossians: ("कुलु", "कुलु."),

    BibleBookEnum.FirstThessalonians: ("1थिस्स", "1 थिस्स", "1थिस्स.", "1 थिस्स."),
    BibleBookEnum.SecondThessalonians: ("2थिस्स", "2 थिस्स", "2थिस्स.", "2 थिस्स."),

    BibleBookEnum.FirstTimothy: ("1तीमु", "1 तीमु", "1तीमु.", "1 तीमु."),
    BibleBookEnum.SecondTimothy: ("2तीमु", "2 तीमु", "2तीमु.", "2 तीमु."),

    BibleBookEnum.Titus: ("तीतु", "तीतु."),
    BibleBookEnum.Philemon: ("फिले", "फिले."),
    BibleBookEnum.Hebrews: ("इब्रा", "इब्रा.", "इब्र", "इब्र."),
    BibleBookEnum.James: ("याकू", "याकू."),
    BibleBookEnum.FirstPeter: ("1पत", "1 पत", "1पत.", "1 पत."),
    BibleBookEnum.SecondPeter: ("2पत", "2 पत", "2पत.", "2 पत."),
    BibleBookEnum.FirstJohn: ("1यूह", "1 यूह", "1यूह.", "1 यूह."),
    BibleBookEnum.SecondJohn: ("2यूह", "2 यूह", "2यूह.", "2 यूह."),
    BibleBookEnum.ThirdJohn: ("3यूह", "3 यूह", "3यूह.", "3 यूह."),
    BibleBookEnum.Jude: ("यहू", "यहूदा"),
    BibleBookEnum.Revelation: ("प्रका", "प्रका."),

    # Deuterocanon (no single standardized abbreviation across Hindi editions; keep safe longer forms)
    BibleBookEnum.Tobit: ("टोबीत",),
    BibleBookEnum.Judith: ("यूदीत",),
    BibleBookEnum.Wisdom: ("प्रज्ञा", "प्रज्ञा-ग्रन्थ"),
    BibleBookEnum.Sirach: ("प्रवक्ता", "प्रवक्ता-ग्रन्थ"),
    BibleBookEnum.Baruch: ("बारूक",),

    BibleBookEnum.FirstMaccabees: ("1 मक्काबियों", "मक्काबियों का पहला ग्रन्थ"),
    BibleBookEnum.SecondMaccabees: ("2 मक्काबियों", "मक्काबियों का दूसरा ग्रन्थ"),
    BibleBookEnum.ThirdMaccabees: ("3 मक्काबियों",),
    BibleBookEnum.FourthMaccabees: ("4 मक्काबियों",),

    BibleBookEnum.EstherAdditions: ("एस्तेर (यूनानी)", "एस्तेर (ग्रीक)"),
    BibleBookEnum.DanielSongOfThree: ("तीन युवकों का गीत",),
    BibleBookEnum.DanielSusanna: ("सुसन्ना",),
    BibleBookEnum.DanielBelAndTheDragon: ("बेल और अजगर",),

    BibleBookEnum.FirstEsdras: ("1 एस्द्रास",),
    BibleBookEnum.SecondEsdras: ("2 एस्द्रास",),
    BibleBookEnum.PrayerOfManasseh: ("मनश्शे की प्रार्थना",),
    BibleBookEnum.Psalm151: ("भजन 151", "भजन संहिता 151"),
}
