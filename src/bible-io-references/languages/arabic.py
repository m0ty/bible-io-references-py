from typing import Dict, Iterable
from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    BibleBookEnum.Genesis: ('التكوين', 'سفر التكوين'),
    BibleBookEnum.Exodus: ('الخروج', 'سفر الخروج'),
    BibleBookEnum.Leviticus: ('اللاويين', 'سفر اللاويين'),
    BibleBookEnum.Numbers: ('العدد', 'سفر العدد'),
    BibleBookEnum.Deuteronomy: ('التثنية', 'سفر التثنية'),
    BibleBookEnum.Joshua: ('يشوع', 'سفر يشوع'),
    BibleBookEnum.Judges: ('القضاة', 'سفر القضاة'),
    BibleBookEnum.Ruth: ('راعوث', 'سفر راعوث'),

    BibleBookEnum.FirstSamuel: ('1 صموئيل', 'صموئيل الأول', 'سفر صموئيل الأول'),
    BibleBookEnum.SecondSamuel: ('2 صموئيل', 'صموئيل الثاني', 'سفر صموئيل الثاني'),
    BibleBookEnum.FirstKings: ('1 ملوك', 'الملوك الأول', 'سفر الملوك الأول'),
    BibleBookEnum.SecondKings: ('2 ملوك', 'الملوك الثاني', 'سفر الملوك الثاني'),
    BibleBookEnum.FirstChronicles: ('1 أخبار الأيام', 'أخبار الأيام الأول', 'سفر أخبار الأيام الأول'),
    BibleBookEnum.SecondChronicles: ('2 أخبار الأيام', 'أخبار الأيام الثاني', 'سفر أخبار الأيام الثاني'),

    BibleBookEnum.Ezra: ('عزرا', 'سفر عزرا'),
    BibleBookEnum.Nehemiah: ('نحميا', 'سفر نحميا'),

    BibleBookEnum.Esther: ('أستير', 'استير', 'سفر أستير'),

    BibleBookEnum.Job: ('أيوب', 'سفر أيوب'),
    BibleBookEnum.Psalms: ('المزامير', 'مزامير', 'سفر المزامير'),
    BibleBookEnum.Proverbs: ('الأمثال', 'امثال', 'سفر الأمثال'),
    BibleBookEnum.Ecclesiastes: ('الجامعة', 'سفر الجامعة'),
    BibleBookEnum.SongOfSolomon: ('نشيد الأنشاد', 'نشيد الأناشيد', 'نشيد الإنشاد', 'سفر نشيد الأنشاد'),

    BibleBookEnum.Isaiah: ('إشعياء', 'اشعياء', 'أشعياء', 'سفر إشعياء'),
    BibleBookEnum.Jeremiah: ('إرميا', 'ارميا', 'أرميا', 'سفر إرميا'),
    BibleBookEnum.Lamentations: ('مراثي إرميا', 'مراثي', 'سفر مراثي إرميا'),
    BibleBookEnum.Ezekiel: ('حزقيال', 'سفر حزقيال'),
    BibleBookEnum.Daniel: ('دانيال', 'سفر دانيال'),

    BibleBookEnum.Hosea: ('هوشع', 'سفر هوشع'),
    BibleBookEnum.Joel: ('يوئيل', 'سفر يوئيل'),
    BibleBookEnum.Amos: ('عاموس', 'سفر عاموس'),
    BibleBookEnum.Obadiah: ('عوبديا', 'عوبيديا', 'سفر عوبديا'),
    BibleBookEnum.Jonah: ('يونان', 'سفر يونان'),
    BibleBookEnum.Micah: ('ميخا', 'سفر ميخا'),
    BibleBookEnum.Nahum: ('ناحوم', 'سفر ناحوم'),
    BibleBookEnum.Habakkuk: ('حبقوق', 'سفر حبقوق'),
    BibleBookEnum.Zephaniah: ('صفنيا', 'سفر صفنيا'),
    BibleBookEnum.Haggai: ('حجي', 'حجاي', 'سفر حجي', 'سفر حجاي'),
    BibleBookEnum.Zechariah: ('زكريا', 'سفر زكريا'),
    BibleBookEnum.Malachi: ('ملاخي', 'ملاخى', 'سفر ملاخي'),

    BibleBookEnum.Matthew: ('متى', 'إنجيل متى'),
    BibleBookEnum.Mark: ('مرقس', 'إنجيل مرقس'),
    BibleBookEnum.Luke: ('لوقا', 'إنجيل لوقا'),
    BibleBookEnum.John: ('يوحنا', 'إنجيل يوحنا'),

    BibleBookEnum.Acts: ('أعمال الرسل', 'اعمال الرسل', 'سفر أعمال الرسل'),
    BibleBookEnum.Romans: ('رومية', 'الرسالة إلى أهل رومية'),

    BibleBookEnum.FirstCorinthians: ('1 كورنثوس', 'كورنثوس الأولى', 'الرسالة الأولى إلى أهل كورنثوس'),
    BibleBookEnum.SecondCorinthians: ('2 كورنثوس', 'كورنثوس الثانية', 'الرسالة الثانية إلى أهل كورنثوس'),

    BibleBookEnum.Galatians: ('غلاطية', 'الرسالة إلى أهل غلاطية'),
    BibleBookEnum.Ephesians: ('أفسس', 'افسس', 'الرسالة إلى أهل أفسس'),
    BibleBookEnum.Philippians: ('فيلبي', 'فيلبى', 'الرسالة إلى أهل فيلبي'),
    BibleBookEnum.Colossians: ('كولوسي', 'كولوسى', 'الرسالة إلى أهل كولوسي'),

    BibleBookEnum.FirstThessalonians: ('1 تسالونيكي', 'تسالونيكي الأولى', 'الرسالة الأولى إلى أهل تسالونيكي'),
    BibleBookEnum.SecondThessalonians: ('2 تسالونيكي', 'تسالونيكي الثانية', 'الرسالة الثانية إلى أهل تسالونيكي'),

    BibleBookEnum.FirstTimothy: ('1 تيموثاوس', 'تيموثاوس الأولى', 'الرسالة الأولى إلى تيموثاوس'),
    BibleBookEnum.SecondTimothy: ('2 تيموثاوس', 'تيموثاوس الثانية', 'الرسالة الثانية إلى تيموثاوس'),

    BibleBookEnum.Titus: ('تيطس', 'رسالة تيطس'),
    BibleBookEnum.Philemon: ('فليمون', 'فيلمون', 'رسالة فليمون'),
    BibleBookEnum.Hebrews: ('عبرانيين', 'العبرانيين', 'رسالة إلى العبرانيين'),
    BibleBookEnum.James: ('يعقوب', 'رسالة يعقوب'),

    BibleBookEnum.FirstPeter: ('1 بطرس', 'بطرس الأولى', 'رسالة بطرس الأولى'),
    BibleBookEnum.SecondPeter: ('2 بطرس', 'بطرس الثانية', 'رسالة بطرس الثانية'),

    BibleBookEnum.FirstJohn: ('1 يوحنا', 'يوحنا الأولى', 'رسالة يوحنا الأولى'),
    BibleBookEnum.SecondJohn: ('2 يوحنا', 'يوحنا الثانية', 'رسالة يوحنا الثانية'),
    BibleBookEnum.ThirdJohn: ('3 يوحنا', 'يوحنا الثالثة', 'رسالة يوحنا الثالثة'),

    BibleBookEnum.Jude: ('يهوذا', 'يهودا', 'رسالة يهوذا'),

    BibleBookEnum.Revelation: ('الرؤيا', 'رؤيا يوحنا', 'سفر الرؤيا'),

    # Deuterocanon / Additions
    BibleBookEnum.Tobit: ('طوبيا', 'طوبيت', 'سفر طوبيا', 'سفر طوبيت'),
    BibleBookEnum.Judith: ('يهوديت', 'سفر يهوديت'),
    BibleBookEnum.Wisdom: ('الحكمة', 'حكمة سليمان', 'سفر الحكمة'),
    BibleBookEnum.Sirach: ('يشوع بن سيراخ', 'سيراخ', 'سفر يشوع بن سيراخ'),
    BibleBookEnum.Baruch: ('باروخ', 'سفر باروخ'),

    BibleBookEnum.FirstMaccabees: ('1 المكابيين', 'المكابيين الأول', 'المكابين الأول', 'سفر المكابيين الأول'),
    BibleBookEnum.SecondMaccabees: ('2 المكابيين', 'المكابيين الثاني', 'المكابين الثاني', 'سفر المكابيين الثاني'),
    BibleBookEnum.ThirdMaccabees: ('3 المكابيين', 'المكابيين الثالث', 'المكابين الثالث', 'سفر المكابيين الثالث'),
    BibleBookEnum.FourthMaccabees: ('4 المكابيين', 'المكابيين الرابع', 'المكابين الرابع', 'سفر المكابيين الرابع'),

    BibleBookEnum.EstherAdditions: ('تتمة أستير', 'تتمة سفر أستير', 'أستير (اليونانية)', 'إضافات أستير'),
    BibleBookEnum.DanielSongOfThree: ('صلاة عزريا وتسبحة الفتية الثلاثة', 'تسبحة الفتية الثلاثة', 'نشيد الفتية الثلاثة'),
    BibleBookEnum.DanielSusanna: ('سوسنة', 'قصة سوسنة'),
    BibleBookEnum.DanielBelAndTheDragon: ('بيل والتنين', 'بال والتنين'),

    BibleBookEnum.FirstEsdras: ('1 عزرا', 'إسدراس الأول', 'إزدراس الأول', 'كتاب إسدراس الأول'),
    BibleBookEnum.SecondEsdras: ('2 عزرا', 'إسدراس الثاني', 'كتاب إسدراس الثاني', 'رؤيا إسدراس'),

    BibleBookEnum.PrayerOfManasseh: ('صلاة منسى', 'صلاة منسّى', 'صلاة منسى الملك'),
    BibleBookEnum.Psalm151: ('مزمور 151',),
}

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {

    BibleBookEnum.Genesis: ('التكوين', 'سفر التكوين', 'تك'),
    BibleBookEnum.Exodus: ('الخروج', 'خروج', 'سفر الخروج', 'خر'),
    BibleBookEnum.Leviticus: ('اللاويين', 'سفر اللاويين', 'لا'),
    BibleBookEnum.Numbers: ('العدد', 'سفر العدد', 'عد'),
    BibleBookEnum.Deuteronomy: ('التثنية', 'سفر التثنية', 'تث'),
    BibleBookEnum.Joshua: ('يشوع', 'سفر يشوع', 'يش'),
    BibleBookEnum.Judges: ('القضاة', 'سفر القضاة', 'قض'),
    BibleBookEnum.Ruth: ('راعوث', 'سفر راعوث', 'را'),

    BibleBookEnum.FirstSamuel: (
        'صموئيل الأول', 'سفر صموئيل الأول',
        '1 صموئيل', 'صموئيل 1', '1صموئيل', '1صم'
    ),
    BibleBookEnum.SecondSamuel: (
        'صموئيل الثاني', 'سفر صموئيل الثاني',
        '2 صموئيل', 'صموئيل 2', '2صموئيل', '2صم'
    ),

    BibleBookEnum.FirstKings: (
        'الملوك الأول', 'سفر الملوك الأول',
        '1 ملوك', 'ملوك 1', '1مل'
    ),
    BibleBookEnum.SecondKings: (
        'الملوك الثاني', 'سفر الملوك الثاني',
        '2 ملوك', 'ملوك 2', '2مل'
    ),

    BibleBookEnum.FirstChronicles: (
        'أخبار الأيام الأول', 'سفر أخبار الأيام الأول',
        '1 أخبار الأيام', 'أخبار الأيام 1', '1أخبار', '1اخ'
    ),
    BibleBookEnum.SecondChronicles: (
        'أخبار الأيام الثاني', 'سفر أخبار الأيام الثاني',
        '2 أخبار الأيام', 'أخبار الأيام 2', '2أخبار', '2اخ'
    ),

    BibleBookEnum.Ezra: ('عزرا', 'سفر عزرا', 'عز'),
    BibleBookEnum.Nehemiah: ('نحميا', 'سفر نحميا', 'نح'),

    BibleBookEnum.Esther: (
        'أستير', 'استير', 'سفر أستير', 'أس', 'اس'
    ),

    BibleBookEnum.Job: ('أيوب', 'سفر أيوب', 'أي'),
    BibleBookEnum.Psalms: ('المزامير', 'مزامير', 'سفر المزامير', 'مز'),
    BibleBookEnum.Proverbs: ('الأمثال', 'امثال', 'سفر الأمثال', 'أم', 'ام'),
    BibleBookEnum.Ecclesiastes: ('الجامعة', 'سفر الجامعة', 'جا'),

    BibleBookEnum.SongOfSolomon: (
        'نشيد الأنشاد', 'نشيد الأناشيد', 'نشيد الإنشاد',
        'سفر نشيد الأنشاد', 'نش'
    ),

    BibleBookEnum.Isaiah: (
        'إشعياء', 'اشعياء', 'أشعياء',
        'سفر إشعياء', 'إش', 'اش'
    ),
    BibleBookEnum.Jeremiah: (
        'إرميا', 'ارميا', 'أرميا',
        'سفر إرميا', 'إر', 'ار'
    ),
    BibleBookEnum.Lamentations: (
        'مراثي إرميا', 'مراثي', 'سفر مراثي إرميا', 'مرا'
    ),
    BibleBookEnum.Ezekiel: ('حزقيال', 'سفر حزقيال', 'حز'),
    BibleBookEnum.Daniel: ('دانيال', 'سفر دانيال', 'دا'),

    BibleBookEnum.Hosea: ('هوشع', 'سفر هوشع', 'هو'),
    BibleBookEnum.Joel: ('يوئيل', 'سفر يوئيل', 'يؤ', 'يوء', 'يوئ'),
    BibleBookEnum.Amos: ('عاموس', 'سفر عاموس', 'عا'),
    BibleBookEnum.Obadiah: ('عوبديا', 'عوبيديا', 'سفر عوبديا', 'عو'),
    BibleBookEnum.Jonah: ('يونان', 'سفر يونان', 'يون'),
    BibleBookEnum.Micah: ('ميخا', 'سفر ميخا', 'مي', 'مى'),
    BibleBookEnum.Nahum: ('ناحوم', 'سفر ناحوم', 'نا'),
    BibleBookEnum.Habakkuk: ('حبقوق', 'سفر حبقوق', 'حب'),
    BibleBookEnum.Zephaniah: ('صفنيا', 'سفر صفنيا', 'صف'),
    BibleBookEnum.Haggai: ('حجي', 'حجاي', 'سفر حجي', 'سفر حجاي', 'حج'),
    BibleBookEnum.Zechariah: ('زكريا', 'سفر زكريا', 'زك'),
    BibleBookEnum.Malachi: ('ملاخي', 'ملاخى', 'سفر ملاخي', 'ملا'),

    # Gospels & NT

    BibleBookEnum.Matthew: (
        'متى', 'إنجيل متى',
        'البشارة كما دوّنها متى', 'مت'
    ),
    BibleBookEnum.Mark: (
        'مرقس', 'إنجيل مرقس',
        'البشارة كما دوّنها مرقس', 'مر'
    ),
    BibleBookEnum.Luke: (
        'لوقا', 'إنجيل لوقا',
        'البشارة كما دوّنها لوقا', 'لو'
    ),
    BibleBookEnum.John: (
        'يوحنا', 'إنجيل يوحنا',
        'البشارة كما دوّنها يوحنا', 'يو'
    ),

    BibleBookEnum.Acts: (
        'أعمال الرسل', 'اعمال الرسل',
        'سفر أعمال الرسل', 'أع', 'اع'
    ),

    BibleBookEnum.Romans: (
        'رومية', 'رسالة رومة',
        'الرسالة إلى أهل رومية',
        'رسالة بولس إلى أهل رومية', 'رو'
    ),

    BibleBookEnum.FirstCorinthians: (
        'كورنثوس الأولى',
        'رسالة كورنثوس الأولى',
        'الرسالة الأولى إلى أهل كورنثوس',
        '1 كورنثوس', '1كو'
    ),
    BibleBookEnum.SecondCorinthians: (
        'كورنثوس الثانية',
        'رسالة كورنثوس الثانية',
        'الرسالة الثانية إلى أهل كورنثوس',
        '2 كورنثوس', '2كو'
    ),

    BibleBookEnum.Galatians: ('غلاطية', 'رسالة غلاطية', 'غل'),
    BibleBookEnum.Ephesians: (
        'أفسس', 'افسس',
        'رسالة أفسس', 'الرسالة إلى أهل أفسس',
        'أف', 'اف'
    ),
    BibleBookEnum.Philippians: (
        'فيلبي', 'فيلبى',
        'رسالة فيلبي', 'الرسالة إلى أهل فيلبي',
        'في'
    ),
    BibleBookEnum.Colossians: (
        'كولوسي', 'كولوسى',
        'رسالة كولوسي', 'الرسالة إلى أهل كولوسي',
        'كو'
    ),

    BibleBookEnum.FirstThessalonians: (
        'تسالونيكي الأولى',
        'الرسالة الأولى إلى أهل تسالونيكي',
        '1 تسالونيكي', '1تس'
    ),
    BibleBookEnum.SecondThessalonians: (
        'تسالونيكي الثانية',
        'الرسالة الثانية إلى أهل تسالونيكي',
        '2 تسالونيكي', '2تس'
    ),

    BibleBookEnum.FirstTimothy: (
        'تيموثاوس الأولى',
        'الرسالة الأولى إلى تيموثاوس',
        '1 تيموثاوس', '1تي'
    ),
    BibleBookEnum.SecondTimothy: (
        'تيموثاوس الثانية',
        'الرسالة الثانية إلى تيموثاوس',
        '2 تيموثاوس', '2تي'
    ),

    BibleBookEnum.Titus: ('تيطس', 'رسالة تيطس', 'تي'),
    BibleBookEnum.Philemon: ('فليمون', 'فيلمون', 'رسالة فليمون', 'فل'),

    BibleBookEnum.Hebrews: (
        'عبرانيين', 'العبرانيين',
        'رسالة إلى العبرانيين', 'عب'
    ),

    BibleBookEnum.James: ('يعقوب', 'رسالة يعقوب', 'يع'),

    BibleBookEnum.FirstPeter: (
        'بطرس الأولى', 'رسالة بطرس الأولى',
        '1 بطرس', '1بط'
    ),
    BibleBookEnum.SecondPeter: (
        'بطرس الثانية', 'رسالة بطرس الثانية',
        '2 بطرس', '2بط'
    ),

    BibleBookEnum.FirstJohn: (
        'يوحنا الأولى', 'رسالة يوحنا الأولى',
        '1 يوحنا', '1يو'
    ),
    BibleBookEnum.SecondJohn: (
        'يوحنا الثانية', 'رسالة يوحنا الثانية',
        '2 يوحنا', '2يو'
    ),
    BibleBookEnum.ThirdJohn: (
        'يوحنا الثالثة', 'رسالة يوحنا الثالثة',
        '3 يوحنا', '3يو'
    ),

    BibleBookEnum.Jude: (
        'يهودا', 'يهوذا',
        'رسالة يهوذا', 'يه'
    ),

    BibleBookEnum.Revelation: (
        'رؤيا', 'الرؤيا',
        'رؤيا يوحنا', 'سفر الرؤيا',
        'رؤ'
    ),

    # Deuterocanon

    BibleBookEnum.Tobit: (
        'طوبيا', 'طوبيت', 'طوبيّا',
        'سفر طوبيا', 'سفر طوبيت', 'طو'
    ),
    BibleBookEnum.Judith: ('يهوديت', 'سفر يهوديت',),
    BibleBookEnum.Wisdom: (
        'الحكمة', 'سفر الحكمة',
        'حكمة سليمان', 'حك'
    ),
    BibleBookEnum.Sirach: (
        'يشوع بن سيراخ',
        'سفر يشوع بن سيراخ',
        'حكمة يشوع بن سيراخ',
        'سيراخ', 'سي'
    ),
    BibleBookEnum.Baruch: (
        'باروخ', 'سفر باروخ',
        'سفر نبوة باروخ', 'با'
    ),

    BibleBookEnum.FirstMaccabees: (
        'المكابيين الأول', 'المكابين الأول',
        'سفر المكابيين الأول',
        '1 مكابيين', '1مك', '1مكا'
    ),
    BibleBookEnum.SecondMaccabees: (
        'المكابيين الثاني', 'المكابين الثاني',
        'سفر المكابيين الثاني',
        '2 مكابيين', '2مك', '2مكا'
    ),
    BibleBookEnum.ThirdMaccabees: (
        'المكابيين الثالث', 'المكابين الثالث',
        'سفر المكابيين الثالث',
        '3 مكابيين', '3مك', '3مكا'
    ),
    BibleBookEnum.FourthMaccabees: (
        'المكابيين الرابع', 'المكابين الرابع',
        'سفر المكابيين الرابع',
        '4 مكابيين', '4مك', '4مكا'
    ),

    BibleBookEnum.EstherAdditions: (
        'تتمة أستير', 'تتمة سفر أستير',
        'إضافات أستير', 'أستير اليونانية',
        'تتمة أس'
    ),

    BibleBookEnum.DanielSongOfThree: (
        'صلاة عزريا وتسبحة الفتية الثلاثة',
        'تسبحة الفتية الثلاثة',
        'نشيد الفتية الثلاثة'
    ),

    BibleBookEnum.DanielSusanna: (
        'سوسنة', 'قصة سوسنة'
    ),

    BibleBookEnum.DanielBelAndTheDragon: (
        'بيل والتنين', 'بال والتنين'
    ),

    BibleBookEnum.FirstEsdras: (
        'إسدراس الأول', 'إزدراس الأول',
        '1 إسدراس', 'كتاب إسدراس الأول'
    ),

    BibleBookEnum.SecondEsdras: (
        'إسدراس الثاني', 'إسدراس الرابع',
        'رؤيا إسدراس', 'كتاب إسدراس الثاني'
    ),

    BibleBookEnum.PrayerOfManasseh: (
        'صلاة منسى', 'صلاة منسّى',
        'صلاة منسى الملك'
    ),

    BibleBookEnum.Psalm151: (
        'مزمور 151', 'مز 151', 'مز151'
    ),
}
