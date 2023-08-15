from typing import Callable, Dict, Any
import time
import functools


def debug(func: Callable) -> Any:
    @functools.wraps(func)
    def wraps_function(*args, **kwargs) -> Any:
        print(*args, **kwargs)
        print('{} is the name of the function and  {} are the arguments of the function'.format(func.__name__, *args, **kwargs))
        start_at = time.time()
        result = func(*args, **kwargs)
        end_at = time.time()
        print(end_at - start_at)
        return result
    return wraps_function


@debug
def function(stuff: dict, criteria: int) -> Dict:
    new_dictionary = {}
    try:
        for entity in stuff.keys():
            if entity > criteria:
                print('{name} has passed the process of jury judgement and with {score} score '
                      'goes forward'.format(name=stuff.get(entity), score=entity))
                new_dictionary.setdefault(stuff.get(entity), entity)
            else:
                print('You have been dismissed due to scanty score')
    except Exception as x:
        print(x)
    print(new_dictionary)
    return new_dictionary


A = {20: 'Jimmy', 10: 'Mike', 30: 'Kelly'}
function(A, criteria=int(input('Enter the minimal score for continuation: ')))
