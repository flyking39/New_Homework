class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        if (
            s and
            all(char in roman_to_int for char in s) and
            1 <= len(s) <= 15
        ):
            total = 0
            prev_value = 0

            for char in s:
                value = roman_to_int[char]
                if value > prev_value:
                    total += value - 2 * prev_value
                    print(total)
                else:
                    total += value
                prev_value = value
                print(total, prev_value)

            print(total)
            return total
        else:
            raise Exception("Invalid input string")


A = Solution()
A.romanToInt(str(input('')))
