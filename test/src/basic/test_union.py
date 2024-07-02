from src.basic.union import foo


def test_union():

    foo("foo")
    foo(1)

    try:
        foo([])
    except Exception as e:
        assert e.__class__.__name__ == 'TypeError'
