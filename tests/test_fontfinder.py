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
