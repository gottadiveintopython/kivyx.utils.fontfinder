'''
Font Finder
===========

Notes for maintainers
---------------------

There are two types of implementations in this module:

* ``_enum_fonts_from_text_ver_safer()``, which only uses Kivy's public api.
* ``_enum_fonts_from_text_ver_faster()``, which uses Kivy's private api.

The safer one is ridiculously inefficient because:

* First, it uses a Label widget yet this module doesn't need to display anything.
* Second, it ends up copying a texture two extra times for each character.
  (RAM -> VRAM -> RAM)

Thus, the safer one is not used by the public api, and exists only for
unittests.
'''

__all__ =(
    'enum_all_fonts', 'get_all_fonts',
    'enum_fonts_from_text', 'enum_fonts_from_lang',
)

from typing import Sequence, Iterator
from functools import lru_cache
from pathlib import Path

SUFFIXES = {'.ttf', '.otf', '.ttc', }


def enum_all_fonts() -> Iterator[Path]:
    '''Enumerates pre-installed fonts'''
    from kivy.core.text import LabelBase
    suffixes = SUFFIXES
    for dir in LabelBase.get_system_fonts_dir():
        for child in Path(dir).iterdir():
            if child.suffix in suffixes:
                yield child


@lru_cache(maxsize=1)
def get_all_fonts() -> Sequence[Path]:
    '''
    Returns an immutable sequence of pre-installed fonts. Return-value
    will be cached.
    '''
    return tuple(enum_all_fonts())


def _enum_fonts_from_text_ver_safer(text) -> Iterator[Path]:
    '''Enumerates pre-installed fonts that are capable of rendering the given
    ``text``. The ``text`` must contain more than two characters without
    duplication.

    .. note::

        The longer the ``text`` is, the more accurate the result will be,
        but the heavier the performance will be.
    '''
    from kivy.uix.label import Label
    if len(text) < 3:
        raise ValueError(f"'text' must contain more than two characters")
    if len(set(text)) < len(text):
        raise ValueError(f"'text' should not contain duplicated characters")
    label = Label(font_size=15)
    for path in get_all_fonts():
        label.font_name = str(path)
        pixels_set = set()
        for i, c in enumerate(text, start=1):
            label.text = c
            try:
                label.texture_update()
            except ValueError:
                # 'NotoColorEmoji.ttf' causes the following error.
                # ValueError: Couldn't load font file: for font /???/???/NotoColorEmoji.ttf
                # Maybe because it's a colored font? idk?
                break
            pixels_set.add(label.texture.pixels)
            if len(pixels_set) != i:
                break
        else:
            yield path


def _enum_fonts_from_text_ver_faster(text) -> Iterator[Path]:
    from kivy.core.text import Label
    if len(text) < 3:
        raise ValueError(f"'text' must contain more than two characters")
    if len(set(text)) < len(text):
        raise ValueError(f"'text' should not contain duplicated characters")
    label = Label()
    label._size = (16, 16)
    for path in get_all_fonts():
        label.options['font_name'] = str(path)
        label.resolve_font_name()
        pixels_set = set()
        for i, c in enumerate(text, start=1):
            label.text = c
            label._render_begin()
            label._render_text(c, 0, 0)
            pixels_set.add(label._render_end().data)
            if len(pixels_set) != i:
                break
        else:
            yield path


_enum_fonts_from_text_ver_faster.__doc__ = _enum_fonts_from_text_ver_safer.__doc__
enum_fonts_from_text = _enum_fonts_from_text_ver_faster
LANG_TEXT_MAP = {
    'ar': 'الجزيرةAB',
    'hi': 'भारतAB',
    'ja': '経伝説あAB',
    'ko': '안녕조AB',
    'zh-Hans': (v := '哪经传说AB'),
    'zh-CN': v,
    'zh-SG': v,
    'zh-Hant': (v := '哪經傳說AB'),
    'zh-TW': v,
    'zh-HK': v,
    'zh-MO': v,
}


def enum_fonts_from_lang(lang) -> Iterator[Path]:
    '''Enumerates pre-installed fonts that support the given language. '''
    return enum_fonts_from_text(LANG_TEXT_MAP[lang])
