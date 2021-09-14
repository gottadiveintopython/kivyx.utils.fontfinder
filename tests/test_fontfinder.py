import pytest

@pytest.mark.parametrize('text', ('', 'A', 'AB'))
def test_short_text(text):
    from kivyx.utils.fontfinder import enum_fonts_from_text
    with pytest.raises(ValueError):
        next(enum_fonts_from_text(text))


def test_duplicated_character():
    from kivyx.utils.fontfinder import enum_fonts_from_text
    with pytest.raises(ValueError):
        next(enum_fonts_from_text('Guido van Rossum'))


def test_the_faster_version_produces_the_same_result_as_the_safer_version():
    from kivyx.utils.fontfinder import (
        _enum_fonts_from_text_ver_safer as safer_ver,
        _enum_fonts_from_text_ver_faster as faster_ver,
        LANG_TEXT_MAP,
    )
    for text in {text for text in LANG_TEXT_MAP.values()}:
        assert tuple(safer_ver(text)) == tuple(faster_ver(text))
