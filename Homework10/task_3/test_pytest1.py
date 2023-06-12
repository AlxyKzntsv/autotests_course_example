import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_div1():
    assert all_division(8, 4, 2) == 1


@pytest.mark.parametrize('a, result', [
    pytest.param((8, 4), 2, marks=pytest.mark.smoke),
    pytest.param((-8, 4, 2), -1, marks=pytest.mark.skip('bad test'))
])
def test_div12(a, result):
    assert all_division(*a) == result


@pytest.mark.acceptance
@pytest.mark.skip("bad")
def test_div3():
    assert all_division(8) == 8


@pytest.mark.acceptance
def test_div4():
    assert all_division(-8, 4, 2) == -1


@pytest.mark.smoke
def test_zero():
    with pytest.raises(ZeroDivisionError):
        assert all_division(8, 4, 0)
