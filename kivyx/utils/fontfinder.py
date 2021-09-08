__all__ =(
    'enum_all_fonts', 'get_all_fonts',
    'fonts_that_are_capable_of_redering',
    'fonts_from_lang', 'LANG_TEXT_MAP',
)

from typing import Sequence, Iterator
from functools import lru_cache
from pathlib import Path
from kivy.uix.label import Label
from kivy.core.text import LabelBase

SUFFIXES = ('.ttf', '.otf', '.ttc', )


def enum_all_fonts() -> Iterator[Path]:
    '''Enumerates pre-installed fonts'''
    suffixes = SUFFIXES
    for dir in LabelBase.get_system_fonts_dir():
        for child in Path(dir).iterdir():
            if child.suffix in suffixes:
                yield child


@lru_cache(maxsize=1)
def get_all_fonts() -> Sequence[Path]:
    '''
    Returns a immutable sequence of pre-installed fonts. Return-value
    will be cached.
    '''
    return tuple(enum_all_fonts())


def fonts_that_are_capable_of_rendering(text) -> Iterator[Path]:
    '''Enumerates pre-installed fonts that are capable of rendering the given
    `text`. The `text` must contain more than two characters without
    duplication.

    .. note::

        The longer the `text` is, the more accurate the result will be,
        but the heavier the performance will be.
    '''
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
                # Maybe because it's a color font? idk?
                break
            pixels_set.add(label.texture.pixels)
            if len(pixels_set) != i:
                break
        else:
            yield path


LANG_TEXT_MAP = {
    'zh-Hant': (v := '經傳說'),
    'zh-TW': v,
    'zh-HK': v,
    'zh-MO': v,
    'zh-Hans': (v := '经传说'),
    'zh-CN': v,
    'zh-SG': v,
    'ko': '안녕조',
    'ja': '経伝説',
}


def fonts_from_lang(lang) -> Iterator[Path]:
    '''Enumerates pre-installed fonts that support the given language.

    Read the `LANG_TEXT_MAP`'s code to see the list of available languages.
    '''
    return fonts_that_are_capable_of_rendering(LANG_TEXT_MAP[lang])
