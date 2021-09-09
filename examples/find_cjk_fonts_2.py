from kivyx.utils.fontfinder import (
    enum_fonts_from_text, LANG_TEXT_MAP as M,
)

print(f"\n-- list of fonts that would support all the CJK glyphs --")
for font in sorted(
        enum_fonts_from_text(''.join((
            M['ko'], M['zh-Hant'], M['zh-Hans'], M['ja'],
        ))),
        key=lambda font: font.name):
    print(font.name)
