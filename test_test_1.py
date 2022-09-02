def test_func_1():
    assert 1 == "1"


def test_func_2():
    a = 3
    b = 5
    c = b - a
    assert a <= c <= b


def test_func_2():
    for i in range(1, 5):
        assert i > i - 1
