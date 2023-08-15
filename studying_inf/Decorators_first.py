import time
from typing import Callable, Any
import functools


def timer(func: Callable) -> Any:
    """
    Декоратор. Который выводит время для декорируемой функции.
    :return:
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        print(round((ended_at - started_at), 5))
        return result
    return wrapped_func


def print_argumets_name(func: Callable) -> Any:
    """
    Декоратор который выводит имя функции и ее аргументы
    :param func:
    :return:
    """
    def wrapped_func(*args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        print('Выполняется функция {func_name}, Аргументы функции {arguments}, '
              '{kwarguments}'.format(func_name=func.__name__, arguments=args, kwarguments=kwargs))
        return result
    return wrapped_func


@timer
@print_argumets_name
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])
    return result


@print_argumets_name
@timer
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])
    return result


# my_result = timer(squares_sum)
# print(timer(squares_sum))
# print(cubes_sum(200))
# my_cubes_sum = timer(cubes_sum, 200)
print(squares_sum())
print(cubes_sum(300))
