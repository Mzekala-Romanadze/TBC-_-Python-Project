class Solution(object):
    def longestCommonPrefix(self, user_list):
        if not all(isinstance(element, str) for element in user_list):
            return TypeError("All elements are not string")

        if not 1 <= len(user_list) <= 200:
            return ValueError("Number of strings must be between 1-200.")

        for strs in user_list:
            if not 0 <= len(strs) <= 200:
                return ValueError("Length of each string must be between 0-200.")
            if not strs.islower():
                return ValueError("Each string must consist of only lowercase English letters")

        if not user_list:
            return "Empty list"

        prefix = user_list[0]

        for string in user_list[1:]:
            min_length = min(len(prefix), len(string))

            mutual_prefix = ""
            for c in range(min_length):
                if prefix[c] == string[c]:
                    mutual_prefix += prefix[c]
                else:
                    break
            prefix = mutual_prefix

            if not prefix:
                return '""'

        return prefix


def main():
    solution = Solution()
    list_1 = ["baby", "baby"]
    list_2 = ["flower", "flow", "flight"]
    list_3 = ["russia", "georgia", "north korea"]
    list_4 = ["sky", 30, "daisy"]
    list_5 = []

    example_1 = solution.longestCommonPrefix(list_1)
    print(f"Example 1: {example_1}")
    example_2 = solution.longestCommonPrefix(list_2)
    print(f"Example 2: {example_2}")
    example_3 = solution.longestCommonPrefix(list_3)
    print(f"Example 3: {example_3}")
    example_4 = solution.longestCommonPrefix(list_4)
    print(f"Example 4: {example_4}")
    example_5 = solution.longestCommonPrefix(list_5)
    print(f"Example 5: {example_5}")


if __name__ == '__main__':
    main()
