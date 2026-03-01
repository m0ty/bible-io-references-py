from typing import Dict, Iterable
from ..bible_book_enums import BibleBookEnum

BOOK_NAMES: Dict[BibleBookEnum, Iterable[str]] = {
    # Pentateuch (CUV + common Catholic/Orthodox variants)
    BibleBookEnum.Genesis: ("创世记", "創世記", "创世纪", "創世紀"),
    BibleBookEnum.Exodus: ("出埃及记", "出埃及記", "出谷纪", "出谷紀"),
    BibleBookEnum.Leviticus: ("利未记", "利未記", "肋未纪", "肋未紀"),
    BibleBookEnum.Numbers: ("民数记", "民數記", "户籍纪", "戶籍紀"),
    BibleBookEnum.Deuteronomy: ("申命记", "申命記", "申命纪", "申命紀"),

    # Historical books
    BibleBookEnum.Joshua: ("约书亚记", "約書亞記", "若苏厄书", "若蘇厄書"),
    BibleBookEnum.Judges: ("士师记", "士師記", "民长纪", "民長紀"),
    BibleBookEnum.Ruth: ("路得记", "路得記", "卢德传", "盧德傳"),
    BibleBookEnum.FirstSamuel: ("撒母耳记上", "撒母耳記上", "撒慕尔纪上", "撒慕爾紀上"),
    BibleBookEnum.SecondSamuel: ("撒母耳记下", "撒母耳記下", "撒慕尔纪下", "撒慕爾紀下"),
    BibleBookEnum.FirstKings: ("列王纪上", "列王紀上"),
    BibleBookEnum.SecondKings: ("列王纪下", "列王紀下"),
    BibleBookEnum.FirstChronicles: ("历代志上", "歷代志上", "编年纪上", "編年紀上"),
    BibleBookEnum.SecondChronicles: ("历代志下", "歷代志下", "编年纪下", "編年紀下"),
    BibleBookEnum.Ezra: ("以斯拉记", "以斯拉記", "厄斯德拉上", "厄斯德拉上"),
    BibleBookEnum.Nehemiah: ("尼希米记", "尼希米記", "厄斯德拉下", "厄斯德拉下", "乃赫米雅", "乃赫米雅"),
    BibleBookEnum.Esther: ("以斯帖记", "以斯帖記", "艾斯德尔传", "艾斯德爾傳"),

    # Wisdom books
    BibleBookEnum.Job: ("约伯记", "約伯記", "约伯传", "約伯傳"),
    BibleBookEnum.Psalms: ("诗篇", "詩篇", "圣咏集", "聖詠集"),
    BibleBookEnum.Proverbs: ("箴言", "箴言篇"),
    BibleBookEnum.Ecclesiastes: ("传道书", "傳道書", "训道篇", "訓道篇"),
    BibleBookEnum.SongOfSolomon: ("雅歌", "歌中之歌"),

    # Major prophets
    BibleBookEnum.Isaiah: ("以赛亚书", "以賽亞書", "依撒意亚", "依撒意亞"),
    BibleBookEnum.Jeremiah: ("耶利米书", "耶利米書", "耶肋米亚", "耶肋米亞"),
    BibleBookEnum.Lamentations: ("耶利米哀歌", "哀歌"),
    BibleBookEnum.Ezekiel: ("以西结书", "以西結書", "厄则克耳", "厄則克耳"),
    BibleBookEnum.Daniel: ("但以理书", "但以理書", "达尼尔", "達尼爾"),

    # Minor prophets
    BibleBookEnum.Hosea: ("何西阿书", "何西阿書", "欧瑟亚", "歐瑟亞"),
    BibleBookEnum.Joel: ("约珥书", "約珥書", "岳厄尔", "岳厄爾"),
    BibleBookEnum.Amos: ("阿摩司书", "阿摩司書", "亚毛斯", "亞毛斯"),
    BibleBookEnum.Obadiah: ("俄巴底亚书", "俄巴底亞書", "亚北底亚", "亞北底亞"),
    BibleBookEnum.Jonah: ("约拿书", "約拿書", "约纳", "約納"),
    BibleBookEnum.Micah: ("弥迦书", "彌迦書", "米该亚", "米該亞"),
    BibleBookEnum.Nahum: ("那鸿书", "那鴻書", "纳鸿", "納鴻"),
    BibleBookEnum.Habakkuk: ("哈巴谷书", "哈巴谷書", "哈巴谷", "哈巴谷"),
    BibleBookEnum.Zephaniah: ("西番雅书", "西番雅書", "索福尼亚", "索福尼亞"),
    BibleBookEnum.Haggai: ("哈该书", "哈該書", "哈盖", "哈蓋"),
    BibleBookEnum.Zechariah: ("撒迦利亚书", "撒迦利亞書", "匝加利亚", "匝加利亞"),
    BibleBookEnum.Malachi: ("玛拉基书", "瑪拉基書", "玛拉基亚", "瑪拉基亞"),

    # Gospels & Acts
    BibleBookEnum.Matthew: ("马太福音", "馬太福音", "玛窦福音", "瑪竇福音"),
    BibleBookEnum.Mark: ("马可福音", "馬可福音", "玛尔谷福音", "瑪爾谷福音"),
    BibleBookEnum.Luke: ("路加福音",),
    BibleBookEnum.John: ("约翰福音", "約翰福音", "若望福音", "若望福音"),
    BibleBookEnum.Acts: ("使徒行传", "使徒行傳", "宗徒大事录", "宗徒大事錄"),

    # Pauline epistles
    BibleBookEnum.Romans: ("罗马书", "羅馬書"),
    BibleBookEnum.FirstCorinthians: ("哥林多前书", "哥林多前書", "格林多前书", "格林多前書"),
    BibleBookEnum.SecondCorinthians: ("哥林多后书", "哥林多後書", "格林多后书", "格林多後書"),
    BibleBookEnum.Galatians: ("加拉太书", "加拉太書", "迦拉达书", "迦拉達書"),
    BibleBookEnum.Ephesians: ("以弗所书", "以弗所書", "厄弗所书", "厄弗所書"),
    BibleBookEnum.Philippians: ("腓立比书", "腓立比書", "斐理伯书", "斐理伯書"),
    BibleBookEnum.Colossians: ("歌罗西书", "歌羅西書", "哥罗森书", "哥羅森書"),
    BibleBookEnum.FirstThessalonians: ("帖撒罗尼迦前书", "帖撒羅尼迦前書", "得撒洛尼前书", "得撒洛尼前書"),
    BibleBookEnum.SecondThessalonians: ("帖撒罗尼迦后书", "帖撒羅尼迦後書", "得撒洛尼后书", "得撒洛尼後書"),
    BibleBookEnum.FirstTimothy: ("提摩太前书", "提摩太前書", "弟茂德前书", "弟茂德前書"),
    BibleBookEnum.SecondTimothy: ("提摩太后书", "提摩太後書", "弟茂德后书", "弟茂德後書"),
    BibleBookEnum.Titus: ("提多书", "提多書", "弟铎书", "弟鐸書"),
    BibleBookEnum.Philemon: ("腓利门书", "腓利門書", "费肋孟书", "費肋孟書"),

    # General epistles & Revelation
    BibleBookEnum.Hebrews: ("希伯来书", "希伯來書"),
    BibleBookEnum.James: ("雅各书", "雅各書", "雅各伯书", "雅各伯書"),
    BibleBookEnum.FirstPeter: ("彼得前书", "彼得前書", "伯多禄前书", "伯多禄前書"),
    BibleBookEnum.SecondPeter: ("彼得后书", "彼得後書", "伯多禄后书", "伯多禄後書"),
    BibleBookEnum.FirstJohn: ("约翰一书", "約翰一書", "若望一书", "若望一書"),
    BibleBookEnum.SecondJohn: ("约翰二书", "約翰二書", "若望二书", "若望二書"),
    BibleBookEnum.ThirdJohn: ("约翰三书", "約翰三書", "若望三书", "若望三書"),
    BibleBookEnum.Jude: ("犹大书", "猶大書", "犹达书", "猶達書"),
    BibleBookEnum.Revelation: ("启示录", "啟示錄", "若望默示录", "若望默示錄"),

    # Deuterocanon / Apocrypha (multiple Chinese traditions)
    BibleBookEnum.Tobit: ("多比传", "多比傳", "多俾亚传", "多俾亞傳"),
    BibleBookEnum.Judith: ("犹滴传", "猶滴傳", "友弟德传", "友弟德傳"),
    BibleBookEnum.Wisdom: ("所罗门智训", "所羅門智訓", "智慧篇", "智慧篇"),
    BibleBookEnum.Sirach: ("便西拉智训", "便西拉智訓", "德训篇", "德訓篇"),
    BibleBookEnum.Baruch: ("巴录书", "巴錄書", "巴路克", "巴路克"),

    BibleBookEnum.FirstMaccabees: ("马加比一书", "馬加比一書", "马加比传上", "馬加比傳上", "玛加伯上", "瑪加伯上"),
    BibleBookEnum.SecondMaccabees: ("马加比二书", "馬加比二書", "马加比传下", "馬加比傳下", "玛加伯下", "瑪加伯下"),
    BibleBookEnum.ThirdMaccabees: ("马加比三书", "馬加比三書", "玛加伯三", "瑪加伯三", "玛喀维传三", "瑪喀維傳三"),
    BibleBookEnum.FourthMaccabees: ("马加比四书", "馬加比四書", "玛加伯四", "瑪加伯四", "玛喀维传四", "瑪喀維傳四"),

    # Additions and other texts
    BibleBookEnum.EstherAdditions: ("以斯帖补编", "以斯帖補編", "以斯帖补篇", "以斯帖補篇", "以斯帖记补编", "以斯帖記補編"),
    BibleBookEnum.DanielSongOfThree: ("三童歌", "三童歌", "三青年赞美上主歌", "三青年讚美上主歌"),
    BibleBookEnum.DanielSusanna: ("苏撒拿传", "蘇撒拿傳", "苏撒拿", "蘇撒拿"),
    BibleBookEnum.DanielBelAndTheDragon: ("彼勒与大龙", "彼勒與大龍", "比勒与大龙", "比勒與大龍"),

    BibleBookEnum.FirstEsdras: ("以斯拉续编上卷", "以斯拉續編上卷", "以斯拉上", "以斯拉上", "埃斯德拉斯一书", "埃斯德拉斯一書"),
    BibleBookEnum.SecondEsdras: ("以斯拉续编下卷", "以斯拉續編下卷", "以斯拉下", "以斯拉下", "埃斯德拉斯二书", "埃斯德拉斯二書"),

    BibleBookEnum.PrayerOfManasseh: ("玛拿西祷言", "瑪拿西禱言", "玛拿西祷词", "瑪拿西禱詞", "默纳舍祷词", "默納舍禱詞"),
    BibleBookEnum.Psalm151: ("诗篇151", "詩篇151", "诗篇第151篇", "詩篇第151篇", "诗篇增补", "詩篇增補"),
}

from typing import Dict, Iterable
from ..bible_book_enums import BibleBookEnum

BOOK_ABBREVIATIONS: Dict[BibleBookEnum, Iterable[str]] = {
    # OT abbreviations
    BibleBookEnum.Genesis: ("创", "創"),
    BibleBookEnum.Exodus: ("出",),
    BibleBookEnum.Leviticus: ("利",),
    BibleBookEnum.Numbers: ("民",),
    BibleBookEnum.Deuteronomy: ("申",),
    BibleBookEnum.Joshua: ("书", "書"),
    BibleBookEnum.Judges: ("士",),
    BibleBookEnum.Ruth: ("得",),

    BibleBookEnum.FirstSamuel: ("撒上",),
    BibleBookEnum.SecondSamuel: ("撒下",),
    BibleBookEnum.FirstKings: ("王上",),
    BibleBookEnum.SecondKings: ("王下",),
    BibleBookEnum.FirstChronicles: ("代上",),
    BibleBookEnum.SecondChronicles: ("代下",),

    BibleBookEnum.Ezra: ("拉",),
    BibleBookEnum.Nehemiah: ("尼",),
    BibleBookEnum.Esther: ("斯",),
    BibleBookEnum.Job: ("伯",),
    BibleBookEnum.Psalms: ("诗", "詩"),
    BibleBookEnum.Proverbs: ("箴",),
    BibleBookEnum.Ecclesiastes: ("传", "傳"),
    BibleBookEnum.SongOfSolomon: ("歌",),
    BibleBookEnum.Isaiah: ("赛", "賽"),
    BibleBookEnum.Jeremiah: ("耶",),
    BibleBookEnum.Lamentations: ("哀",),
    BibleBookEnum.Ezekiel: ("结", "結"),
    BibleBookEnum.Daniel: ("但",),
    BibleBookEnum.Hosea: ("何",),
    BibleBookEnum.Joel: ("珥",),
    BibleBookEnum.Amos: ("摩",),
    BibleBookEnum.Obadiah: ("俄",),
    BibleBookEnum.Jonah: ("拿",),
    BibleBookEnum.Micah: ("弥", "彌"),
    BibleBookEnum.Nahum: ("鸿", "鴻"),
    BibleBookEnum.Habakkuk: ("哈",),
    BibleBookEnum.Zephaniah: ("番",),
    BibleBookEnum.Haggai: ("该", "該"),
    BibleBookEnum.Zechariah: ("亚", "亞"),
    BibleBookEnum.Malachi: ("玛", "瑪"),

    # NT abbreviations
    BibleBookEnum.Matthew: ("太",),
    BibleBookEnum.Mark: ("可",),
    BibleBookEnum.Luke: ("路",),
    BibleBookEnum.John: ("约", "約"),
    BibleBookEnum.Acts: ("徒",),

    BibleBookEnum.Romans: ("罗", "羅"),
    BibleBookEnum.FirstCorinthians: ("林前",),
    BibleBookEnum.SecondCorinthians: ("林后", "林後"),
    BibleBookEnum.Galatians: ("加",),
    BibleBookEnum.Ephesians: ("弗",),
    BibleBookEnum.Philippians: ("腓",),
    BibleBookEnum.Colossians: ("西",),
    BibleBookEnum.FirstThessalonians: ("帖前",),
    BibleBookEnum.SecondThessalonians: ("帖后", "帖後"),
    BibleBookEnum.FirstTimothy: ("提前",),
    BibleBookEnum.SecondTimothy: ("提后", "提後"),
    BibleBookEnum.Titus: ("多",),
    BibleBookEnum.Philemon: ("门", "門"),
    BibleBookEnum.Hebrews: ("来", "來"),
    BibleBookEnum.James: ("雅",),
    BibleBookEnum.FirstPeter: ("彼前",),
    BibleBookEnum.SecondPeter: ("彼后", "彼後"),

    # 约 = John (Gospel) unless followed by 1/2/3 (see parsing rules below)
    BibleBookEnum.FirstJohn: ("约一", "約一", "约壹", "約壹"),
    BibleBookEnum.SecondJohn: ("约二", "約二", "约贰", "約貳"),
    BibleBookEnum.ThirdJohn: ("约三", "約三", "约叁", "約參"),

    BibleBookEnum.Jude: ("犹", "猶"),
    BibleBookEnum.Revelation: ("启", "啟"),

    # Deuterocanon / Apocrypha abbreviations (use longer forms to reduce collisions)
    BibleBookEnum.Tobit: ("多比", "多俾"),
    BibleBookEnum.Judith: ("犹滴", "猶滴", "友弟德"),
    BibleBookEnum.Wisdom: ("智慧", "智训", "智訓"),
    BibleBookEnum.Sirach: ("便西拉", "德训", "德訓"),
    BibleBookEnum.Baruch: ("巴录", "巴錄", "巴", "巴路克"),

    BibleBookEnum.FirstMaccabees: ("马加比一", "馬加比一", "马加比上", "馬加比上", "玛加伯上", "瑪加伯上", "马加比传上", "馬加比傳上"),
    BibleBookEnum.SecondMaccabees: ("马加比二", "馬加比二", "马加比下", "馬加比下", "玛加伯下", "瑪加伯下", "马加比传下", "馬加比傳下"),
    BibleBookEnum.ThirdMaccabees: ("马加比三", "馬加比三", "玛加伯三", "瑪加伯三", "马加比三书", "馬加比三書"),
    BibleBookEnum.FourthMaccabees: ("马加比四", "馬加比四", "玛加伯四", "瑪加伯四", "马加比四书", "馬加比四書"),

    BibleBookEnum.EstherAdditions: ("斯补", "斯補", "以斯帖补编", "以斯帖補編", "以斯帖补篇", "以斯帖補篇"),
    BibleBookEnum.DanielSongOfThree: ("三童歌",),
    BibleBookEnum.DanielSusanna: ("苏撒拿", "蘇撒拿"),
    BibleBookEnum.DanielBelAndTheDragon: ("彼勒与大龙", "彼勒與大龍", "比勒与大龙", "比勒與大龍"),

    BibleBookEnum.FirstEsdras: ("以斯拉续编上卷", "以斯拉續編上卷"),
    BibleBookEnum.SecondEsdras: ("以斯拉续编下卷", "以斯拉續編下卷"),

    BibleBookEnum.PrayerOfManasseh: ("玛拿西祷言", "瑪拿西禱言", "玛拿西祷词", "瑪拿西禱詞"),
    BibleBookEnum.Psalm151: ("诗151", "詩151", "诗篇151", "詩篇151", "诗篇增补", "詩篇增補"),
}
