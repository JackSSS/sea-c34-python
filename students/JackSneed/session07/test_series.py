import series as test

def test_fabonacci(n):
    assert test.fabonacci(3) == 2


def test_lucas(n):
    assert test.lucas(3) == 4


def test_sum_series(n, val1=0, val2=1):
    assert test.sum_series(3, 2, 3) == 8
