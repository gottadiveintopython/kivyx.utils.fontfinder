import pytest

@pytest.mark.parametrize('text', ('', 'A', 'AB'))
def test_short_text(text):
    from kivyx.utils.fontfinder import fonts_that_are_capable_of_rendering
    with pytest.raises(ValueError):
        next(fonts_that_are_capable_of_rendering(text))


def test_duplicated_character():
    from kivyx.utils.fontfinder import fonts_that_are_capable_of_rendering
    with pytest.raises(ValueError):
        next(fonts_that_are_capable_of_rendering('Guido van Rossum'))
