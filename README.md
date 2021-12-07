(This project was archived in favor of https://github.com/gottadiveintopython/i18n.)

# FontFinder

[Youtube](https://www.youtube.com/watch?v=iBDteZhJ3kE) (video is older, and the api is different)  

This module helps to find fonts that support specified language.
So you no longer need to put font files into your app.

## Usage

```python
from kivyx.utils.fontfinder import enum_fonts_from_text, enum_fonts_from_lang

# print all the fonts that would support traditional Chinese.
for font in enum_fonts_from_text('經傳說'):
    print(font.name)

# print all the fonts that would support Korean.
for font in enum_fonts_from_text('안녕조'):
    print(font.name)

# For CJK, Arabic and Hindi fonts, there is an alternative.
for lang in 'zh-Hant zh-Hans ko ja hi ar'.split():
    print(f"-- list of fonts that would support [{lang}] --")
    for font in enum_fonts_from_lang(lang):
        print(font.name)
```

## Installation

```
pip install git+https://github.com/gottadiveintopython/kivyx.utils.fontfinder#egg=kivyx.utils.fontfinder
```

## LICENSE

MIT

## Test Environment

- CPython 3.8.12
- Kivy 2.0.0

## Add your language

If you want `enum_fonts_from_lang()` to suport your language,
open a pull request that adds key/value to `DISCRIMINANT` in `fontfinder.py`.
