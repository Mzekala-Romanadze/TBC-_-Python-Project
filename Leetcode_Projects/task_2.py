class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        if not (1 <= n <= 5 * (10 ** 4)):
            return ValueError("Length of list must be between 1-5*10^4.")


        counter = {}
        for element in nums:
            if not (-10 ** 9 <= element <= 10 ** 9):
                return ValueError("Numbers must be in range -10^9-10^9.")

            if element in counter:
                counter[element] += 1
            else:
                counter[element] = 1

        for key, value in counter.items():
            if value > n // 2:
                return key

        return None


def main():
    solution = Solution()
    list_1 = [8, 30, 8]
    list_2 = [30, 30, 1, 1, 1, 30, 30]
    list_3 = []
    list_4 = [1, 2, 3]
    list_5 = [66, 66, 88, 88]

    example_1 = solution.majorityElement(list_1)
    print(f"Example 1: {example_1}")
    example_2 = solution.majorityElement(list_2)
    print(f"Example 2: {example_2}")
    example_3 = solution.majorityElement(list_3)
    print(f"Example 3: {example_3}")
    example_4 = solution.majorityElement(list_4)
    print(f"Example 4: {example_4}")
    example_5 = solution.majorityElement(list_5)
    print(f"Example 5: {example_5}")


if __name__ == '__main__':
    main()
