from typing import assert_type
from src.basic.return_ex import foo


def test_return_ex():

    assert_type(foo(), int)

    try:
        assert_type(foo(), str)
    except Exception as e:
        assert e.__class__.__name__ == 'TypeError'
