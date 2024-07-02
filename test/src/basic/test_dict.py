from src.basic.dict import foo


def test_foo():

    foo({"foo": "bar"})

    try:
        foo({"foo": 1})
    except Exception as e:
        assert e.__class__.__name__ == 'TypeError'
