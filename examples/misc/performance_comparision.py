from timeit import timeit
from kivyx.utils.fontfinder import (
    _enum_fonts_from_text_ver_faster as faster_ver,
    _enum_fonts_from_text_ver_safer as safer_ver,
    LANG_TEXT_MAP,
)

text = LANG_TEXT_MAP['zh-Hant']

# call one so that font files are cached
tuple(faster_ver(text))

# 該当するfontを一つだけ挙げる。多くのアプリではこれで十分と思われる
print('faster: ', timeit(lambda: next(faster_ver(text)), number=100))
print('safer : ', timeit(lambda: next(safer_ver(text)), number=100))

# 該当するfontを全て挙げる。
print('faster: ', timeit(lambda: tuple(faster_ver(text)), number=100))
print('safer : ', timeit(lambda: tuple(safer_ver(text)), number=100))
