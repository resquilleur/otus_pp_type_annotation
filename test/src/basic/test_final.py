from typing import Final


def test_final():
    my_list: Final = []
    my_list.append(1)

    try:
        my_list = []
        my_list = "something else"
    except Exception as e:
        assert e.__class__.__name__ == 'TypeError'
