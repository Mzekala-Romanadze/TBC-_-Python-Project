class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        if not (2 <= n <= 104):
            return ValueError("Length of list must be in range 2-104.")

        if not (-109 <= target <= 109):
            return ValueError("Target must be in range -109-109.")

        num_indices = {}
        for i, addend_1 in enumerate(nums):
            if not (-109 <= addend_1 <= 109):
                return ValueError("Numbers must be in range -109-109.")
            addend_2 = target - addend_1
            if addend_2 in num_indices:
                return [num_indices[addend_2], i]
            num_indices[addend_1] = i


def main():
    solution = Solution()
    list_1 = [6, 12, 24, 30, 15, 8, 16, 18, 56, 66]

    example_1 = solution.twoSum(list_1, 78)
    print(f"Example 1: {example_1}")


if __name__ == '__main__':
    main()
