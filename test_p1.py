import pytest
from p1 import p1_for


@pytest.fixture(scope='function')
def empty_list():
    return []


@pytest.fixture(scope='function')
def pop_list():
    return range(5)


@pytest.fixture(scope='function')
def float_list():
    return [x*0.1 for x in range(10)]


@pytest.fixture(scope='function')
def neg_list():
    return range(-5, 5)


def test_p1_empty(empty_list):
    assert 0 == p1_for(empty_list)


def test_p1_pop(pop_list):
    assert 10 == p1_for(pop_list)


def test_p1_float(float_list):
    assert 4.50 == p1_for(float_list)


def test_p1_neg(neg_list):
    assert -5 == p1_for(neg_list)
