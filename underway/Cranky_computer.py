from typing import Callable, Any, List
import functools
list1 = []


def how_are_you(func: Callable) -> Any:

    @functools.wraps(func)
    def wraps_function(*args, **kwargs) -> Any:
        print('How are you doing?')
        user_input = str(input('Enter the response to the program inquire: '))
        print('I am a little sad and cranky, but i guess i have to satisfy your request anyway')
        process = func(*args, **kwargs)
        return process
    return wraps_function()


@how_are_you
def calculations() -> List[int]:
    try:
        for case in range(100):
            if case % 10 <= 5:
                list1.append(case)
            else:
                continue
        print(list1)
        return list1
    except RuntimeError:
        print('program has been finished')


calculations()