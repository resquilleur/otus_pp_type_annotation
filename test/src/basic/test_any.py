import pytest

import src.basic.any


def test_any():
    src.basic.any.foo(1)
    src.basic.any.foo("10")
    with pytest.raises(TypeError) as excinfo:
        # pylint: disable=E1121
        src.basic.any.foo(1, 2)
    assert str(excinfo.value) == 'foo() takes 1 positional argument but 2 were given'
