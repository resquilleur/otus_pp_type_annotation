from src.basic.typealias import Vector


def test_typealias():
    def foo(v: Vector):
        ...

    foo([1.1, 2])

    try:
        foo(1)
        foo(["1"])
    except Exception as e:
        assert e.__class__.__name__ == 'TypeError'
