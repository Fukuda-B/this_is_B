import unicodedata
B = [
    "B","Ｂ","Ⓑ","Ḅ",
    "🄑",          "ᴮ",
    "𝐁",           "𝐵",
    "𝑩",           "ℬ",
    "𝓑","𝔅","𝔹","𝖡",
    "𝗕",            "𝘉",
    "𝘽",             "𝙱",
    "ʙ",             "🄱",
    "🅑",            "🅱",
    "Ƀ","Ɓ","Ƃ","Ḃ","𝕭",
]
[print(f"{B[i]}{'  ' if unicodedata.east_asian_width(B[i]) == 'F' else '   '}{format(ord(B[i]), '#08x')}") for i in range(len(B))]
