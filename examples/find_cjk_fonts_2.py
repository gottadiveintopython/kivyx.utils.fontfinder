from kivyx.utils.fontfinder import (
    fonts_that_are_capable_of_rendering, LANG_TEXT_MAP as M,
)

print(f"\n-- list of fonts that would support all the CJK glyphs --")
for font in sorted(
        fonts_that_are_capable_of_rendering(''.join((
            M['ko'], M['zh-Hant'], M['zh-Hans'], M['ja'],
        ))),
        key=lambda font: font.name):
    print(font.name)
