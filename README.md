# FontFinder

[Youtube](https://www.youtube.com/watch?v=iBDteZhJ3kE) (video is older, and the api is different)  
This module helps to find fonts that support arbitrary language.
So you no longer need to put font files into your apk.

## Usage

```python
from kivyx.utils.fontfinder import enum_fonts_from_text, enum_fonts_from_lang

# print all the fonts that would support traditional Chinese.
for font in enum_fonts_from_text('經傳說'):
    print(font.name)

# print all the fonts that would support Korean.
for font in enum_fonts_from_text('안녕조'):
    print(font.name)

# For CJK fonts, there is a shortcut.
for font in enum_fonts_from_lang('zh-Hans'):  # simplified Chinese
    print(font.name)
for font in enum_fonts_from_lang('ja'):  # Japanese
    print(font.name)
```

## Installation

```
pip install git+https://github.com/gottadiveintopython/kivyx.utils.fontfinder#egg=kivyx.utils.fontfinder
```

## LICENSE

MIT

## Test Environment

- CPython 3.8.10
- Kivy 2.0.0

## Notes

**Current implementation is probably inefficient,**
and might be improved by using `kivy.core.text` instead of `kivy.uix.label`.
