from functools import reduce
from kivyx.utils.fontfinder import fonts_from_lang

lang2fonts = {
    lang: set(fonts_from_lang(lang))
    for lang in 'zh-Hant zh-Hans ko ja'.split()
}
for lang, fonts in lang2fonts.items():
    print(f"\n-- list of fonts that would support [{lang}] --")
    for font in sorted(fonts, key=lambda font: font.name):
        print(font.name)


print(f"\n-- list of fonts that would support all the CJK glyphs --")
for font in sorted(
        reduce(set.intersection, lang2fonts.values()),
        key=lambda font: font.name):
    print(font.name)
