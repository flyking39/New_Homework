# Нужно найти, какие два числа из списков в результате попарного перемножения дадут число 56.
from typing import Any
list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def multiplication(list_1: list, list_2: list, to_find: int) -> Any:
    """
    description
    :param list_1:
    :param list_2:
    :param to_find:
    :return:
    """
    for x in list_1:
        for y in list_2:
            result = x * y
            yield result
            print(x, y, result)
            if result == to_find:
                print('found')
                return result


multiplication(list_1, list_2, to_find)

item = multiplication(list_1, list_2, to_find)
for x in item:
    print(x)
