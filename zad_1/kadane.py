class EmptyArrayError(Exception):
    def __init__(self, message="Array is empty"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


def kadane(array: list) -> int:
    check_argument(array)
    cur_max = global_max = array[0]
    for element in array[1:]:
        cur_max = max(element, element + cur_max)
        global_max = max(cur_max, global_max)
    return global_max


def check_argument(array: list):
    if not len(array):
        raise EmptyArrayError
    for element in array:
        if not type(element) == int:
            raise TypeError


if __name__ == '__main__':
    array = [1, 1, 2, 3, 4, 5]
    kadane(array=array)
