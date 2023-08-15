from typing import Any

Roman_dictionary = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
print(Roman_dictionary.keys())


class Last_value_exception():
    def __iter__(self, final, pre_final):
        return final > pre_final


class Solution:

    def decryption(self, user_input: str) -> Any:
        if (
                user_input and
                all(char in Roman_dictionary for char in user_input) and
                1 <= len(user_input) <= 15
        ):
            prev_value = 0
            for index, element in enumerate(user_input):
                a = user_input[-2]
                try:
                    if Roman_dictionary.get(element[index]) > \
                            Roman_dictionary.get(element[index + 1]):
                        prev_value += Roman_dictionary.get(element)
                        print(prev_value)
                    else:
                        prev_value += Roman_dictionary.get(element[index + 1]) - \
                                      Roman_dictionary.get(element[index])
                        print(prev_value)
                except Exception:
                    print('that is it')
                    global value1, value2, total
                    value1 = Roman_dictionary.get(element[-1])
                    value2 = Roman_dictionary.get(a)
                    total = prev_value
        else:
            raise ValueError('wrong input')


A = Solution()
B = Last_value_exception()
value1 = 0
value2 = 0
total = 0


def counting():
    A.decryption('LXIV')
    # B.__iter__(value1, value2)
    # if B.__iter__(value1, value2) is True:
    #     print(total + (value1 - value2))
    # else:
    #     print(total + value1)


counting()
