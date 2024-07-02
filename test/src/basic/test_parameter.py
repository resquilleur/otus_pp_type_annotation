from src.basic.parameter import foo


def test_parameter():

    foo(10)

    try:
        foo("10")
    except Exception as e:
        assert e.__class__.__name__ == 'TypeError'
