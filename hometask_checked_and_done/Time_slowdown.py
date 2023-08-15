from typing import Callable, Any
import time


def prolongation(func: Callable) -> Any:
    def wraps_function(*args, **kwargs) -> Any:
        time.sleep(2)
        implementation = func(*args, **kwargs)
        return implementation
    return wraps_function


@prolongation
def function(*, manifest: dict, user_key: int) -> Any:
    try:
        print(manifest.get(user_key))
    except ValueError:
        print(f'{manifest.__name__} has no {user_key}')


storage = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
function(manifest=storage, user_key=int(input('Enter the number: ')))
