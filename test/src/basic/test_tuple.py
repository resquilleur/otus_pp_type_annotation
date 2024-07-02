from src.basic.tuple import foo


def test_tuple():

    foo(("foo", 1))

    try:
        foo((1, 2))
        foo(("foo", "bar"))
        foo((1, "foo"))
    except Exception as e:
        assert e.__class__.__name__ == 'TypeError'
