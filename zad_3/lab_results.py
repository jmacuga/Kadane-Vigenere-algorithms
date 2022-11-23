class WrongPointsNumError(Exception):
    pass


def check_length(points: list, person: tuple):
    if not len(person[1]) == len(points):
        raise WrongPointsNumError


def calculate_mean_percentage(person_points_sum: int, points: list) -> int:
    return round((person_points_sum / sum(points)) * 100)


def check_person_points(person: tuple) -> tuple:
    new_person = (person[0], [])
    for point in person[1]:
        if type(point) == str:
            if int(point) < 0:
                raise ValueError
            new_person[1].append(int(point))
        elif type(point) == float or point < 0:
            raise ValueError
        else:
            new_person[1].append(point)
    return new_person


def check_points_values(points_list: list, person: tuple):
    for exercise_points, person_points in zip(points_list, person[1]):
        if person_points > exercise_points:
            raise ValueError


def lab_results(points: list, students: list) -> list:
    results = []
    for person in students:
        try:
            check_length(points, person)
            person = check_person_points(person)
            check_points_values(points, person)
            p_sum = sum(person[1])
            mean_percentage = calculate_mean_percentage(sum(person[1]), points)
        except(TypeError, WrongPointsNumError, ValueError):
            p_sum = None
            mean_percentage = None
        results.append((person[0], p_sum, mean_percentage))
    return results
