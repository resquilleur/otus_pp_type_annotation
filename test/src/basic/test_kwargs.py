from src.basic.kwargs import foo


def test_kwargs():

    foo(a=1, b="2")

    try:
        foo(a=[1])
    except Exception as e:
        assert e.__class__.__name__ == 'TypeError'
