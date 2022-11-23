from lab_results import lab_results, check_length, check_person_points, calculate_mean_percentage
from lab_results import WrongPointsNumError
import pytest


def test_check_length_person_too_short():
    points = [10, 10, 10]
    person = ("Julka Nowakowska", [10, 2])
    with pytest.raises(WrongPointsNumError):
        check_length(points, person)


def test_check_length_person_too_long():
    points = [10, 10, 10]
    person = ("Julka Nowakowska", [10, 2, 2, 3, 4])
    with pytest.raises(WrongPointsNumError):
        check_length(points, person)


def test_check_length_pass():
    points = [10, 10]
    person = ("Julka Nowakowska", [10, 2])
    check_length(points, person)


def test_calculate_mean_percentage():
    points = [20, 20]
    person = ("Julka Nowakowska", [10, 2])
    assert calculate_mean_percentage(sum(person[1]), points) == 30


def test_calculate_mean_percentage2():
    points = [20, 20]
    person = ("Julka Nowakowska", [7, 2])
    assert calculate_mean_percentage(sum(person[1]), points) == 22


def test_calculate_mean_percentage3():
    points = [20, 20]
    person = ("Julka Nowakowska", [20, 20])
    assert calculate_mean_percentage(sum(person[1]), points) == 100


def test_check_person_pass():
    person = ('Anna Nowacka', [1, 2, 3])
    assert check_person_points(person)[1] == [1, 2, 3]


def test_check_person_float():
    person = ('Anna Nowacka', [1.2, 2, 3])
    with pytest.raises(ValueError):
        check_person_points(person)


def test_check_person_char():
    person = ('Anna Nowacka', ['a', 2, 3])
    with pytest.raises(ValueError):
        check_person_points(person)


def test_check_person_points_int_cast():
    person = ('Anna Nowacka', ['1', 2, 3])
    assert check_person_points(person)[1] == [1, 2, 3]


def test_check_person_points_int_cast2():
    person = ('Anna Nowacka', [1, 2, '3'])
    assert check_person_points(person)[1] == [1, 2, 3]


def test_check_person_points_str_float():
    person = ('Anna Nowacka', [1, '2.2', 3])
    with pytest.raises(ValueError):
        check_person_points(person)


def test_check_person_points_negative_int():
    person = ('Anna Nowacka', [-1, 2, 3])
    with pytest.raises(ValueError):
        check_person_points(person)


def test_check_person_points_negative_str():
    person = ('Anna Nowacka', [1, '-2', 3])
    with pytest.raises(ValueError):
        check_person_points(person)


def test_lab_results_pass():
    points = [10, 20, 30]
    students = [("Adam Abacki", [5, 10, 15]), ("Basia Babacka",
                                               [10, 20, 30]), ("Cecylia Cabacka", [1, 2, 3])]
    results = lab_results(points, students)
    assert results[0] == ("Adam Abacki", 30, 50)
    assert results[1] == ("Basia Babacka", 60, 100)
    assert results[2] == ("Cecylia Cabacka", 6, 10)


def test_lab_results_exception():
    points = [10, 20, 30]
    students = [("Adam Abacki", [5, "1o", 15]),
                ("Basia Babacka", [10, 20, 30]), ("Cecylia Cabacka", 55)]
    results = lab_results(points, students)
    assert results[0] == ("Adam Abacki", None, None)
    assert results[1] == ("Basia Babacka", 60, 100)
    assert results[2] == ("Cecylia Cabacka", None, None)


def test_lab_results_cast():
    points = [10, 20, 30]
    students = [("Adam Abacki", ['5', "10", '15']),
                ("Basia Babacka", [10, 20, 30]), ("Cecylia Cabacka", [55, 2, 3, 5])]
    results = lab_results(points, students)
    assert results[0] == ("Adam Abacki", 30, 50)
    assert results[1] == ("Basia Babacka", 60, 100)
    assert results[2] == ("Cecylia Cabacka", None, None)


def test_lab_results_too_much_points():
    points = [10, 20, 30]
    students = [("Adam Abacki", [5, "30", 15]),
                ("Basia Babacka", [10, 40, 30]), ("Cecylia Cabacka", [55, 2, 3])]
    results = lab_results(points, students)
    assert results[0] == ("Adam Abacki", None, None)
    assert results[1] == ("Basia Babacka", None, None)
    assert results[2] == ("Cecylia Cabacka", None, None)
