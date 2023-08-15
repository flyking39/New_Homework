from typing import Callable, Any, List, Dict
import functools

class Letter(Exception):
    pass


def logging(func: Callable) -> Any:
    @functools.wraps(func)
    def wraps_function(*arks, **kwargs) -> Any:
        name = func.__name__
        if name.startswith('n'):
            print('The function name is {name} and the arguments are {arguments}'.format(name=name, arguments=arks,))
            print(func(*arks, **kwargs))
        else:
            print('Exception')
            print(func(*arks, **kwargs))
            with open('../homework_done_yet_not_checked/Exceptions.txt', 'a') as my_file:
                my_file.write(f'{name} is not eligible' + '\n')
    return wraps_function()


@logging
def number1() -> List:
    return [x ** 2 for x in range(7)]


@logging
def number2() -> List:
    return [(x * 4) / 100 for x in range(20) if x >= 5]


@logging
def string_func1() -> int:
    subject = 'Even though dictionary comprehensions are great for writing elegant code ' \
              'that is easy to read, they are not always the right choice.'
    return subject.count('f')


@logging
def string_func2() -> Dict:
    letters_dictionary = {}
    sentence = 'Even though dictionary comprehensions are great for writing elegant code ' \
               'that is easy to read, they are not always the right choice.'
    for letter in sentence:
        letters_dictionary.setdefault(sentence.count(letter), letter)
    return letters_dictionary


