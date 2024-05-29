class Solution(object):
    def romanToInt(self, s):
        n = len(s)
        if not (1 <= n <= 15):
            return ValueError("Wrong symbol. Number of characters must be in range 1-15.")

        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for c in s:
            if c not in roman_to_integer:
                return ValueError("Character is not valid. Available characters: I,V,X,L,C,D,M")

        integer_value = 0
        prev_value = 0
        for symbol in reversed(s):
            current_value = roman_to_integer[symbol]

            if current_value < prev_value:
                integer_value -= current_value
            else:
                integer_value += current_value

            prev_value = current_value

        if not 1 <= integer_value <= 3999:
            return f"{s} is not valid roman number"

        return integer_value


def main():
    solution = Solution()
    user_input_1 = "III"
    user_input_2 = "LVIII"  # 58
    user_input_3 = "MCMXCIV"  # 1994

    result = solution.romanToInt(user_input_1)
    print(f"Roman: {user_input_1} => Integer: {result}")
    result = solution.romanToInt(user_input_2)
    print(f"Roman: {user_input_2} => Integer: {result}")
    result = solution.romanToInt(user_input_3)
    print(f"Roman: {user_input_3} => Integer: {result}")


if __name__ == '__main__':
    main()
