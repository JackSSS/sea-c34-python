import series as test

def test_fabonacci():
    assert test.fabonacci(3) == 2


def test_lucas():
    assert test.lucas(3) == 4


def test_sum_series():
    assert test.sum_series(3, 2, 3) == 8
