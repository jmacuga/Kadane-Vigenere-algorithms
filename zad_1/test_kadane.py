from kadane import kadane, EmptyArrayError
import pytest


def test_kadane_normal():
    array = [-1, 2, -3, -4, 5, 6, 7]
    assert(kadane(array) == 18)


def test_kadane_normal_2():
    array = [10, -1, 10, 2]
    assert(kadane(array) == 21)


def test_kadane_normal_3():
    array = [10, -1, 10]
    assert(kadane(array) == 19)


def test_kadane_negative():
    array = [-10, -1, -10]
    assert(kadane(array) == -1)


def test_kadane_normal_case_3():
    array = [10, 1, -10]
    assert(kadane(array) == 11)


def test_kadane_TypeError1():
    array = [1.2, 1, 2]
    with pytest.raises(TypeError):
        kadane(array=array)


def test_kadane_TypeError2():
    array = [2, 'a', 2]
    with pytest.raises(TypeError):
        kadane(array=array)


def test_kadane_EmptyArrayError():
    array = []
    with pytest.raises(EmptyArrayError):
        kadane(array=array)


