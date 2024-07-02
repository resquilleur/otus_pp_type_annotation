a: int
a = 2


try:
    a = "1"
except Exception as e:
    assert e.__class__.__name__ == 'TypeError'
