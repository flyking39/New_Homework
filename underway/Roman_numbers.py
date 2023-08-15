Roman_dictionary = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
print(Roman_dictionary.keys())


class Solution:

    def decryption(self, s: str) -> int:
        if (
                s and
                all(char in Roman_dictionary for char in s) and
                1 <= len(s) <= 15
        ):
            total = 0
            prev_value = 0
            for index, element in enumerate(s):
                try:
                    if element[index] > element[index + 1]:
                        prev_value += Roman_dictionary.get(element)
                    else:
                        prev_value += Roman_dictionary.get(element[index + 1]) - \
                                      Roman_dictionary.get(element[index])
                        return prev_value
                except Exception:
                    if element[index] > element[index - 1]:

                        prev_value += element[index - 1] - element[index]
        else:
            raise ValueError('wrong input')




A = Solution()
print(A.decryption('LXIV'))
