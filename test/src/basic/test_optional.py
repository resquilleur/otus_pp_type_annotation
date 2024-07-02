from src.basic.optional import foo


def test_optional():

    foo(10)
    foo(None)
    foo()

    try:
        foo("10")
    except Exception as e:
        assert e.__class__.__name__ == 'TypeError'
