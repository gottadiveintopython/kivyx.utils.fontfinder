from kivyx.utils.fontfinder import enum_fonts_from_text

print(f"\n-- list of fonts that would support all the CJK glyphs --")
for font in sorted(enum_fonts_from_text('안經经経녕傳传伝'), key=lambda font: font.name):
    print(font.name)
