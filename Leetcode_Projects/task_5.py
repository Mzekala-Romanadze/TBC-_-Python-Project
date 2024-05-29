class Solution(object):
    def climbStairs(self, n):
        if not 1 <= n <= 45:
            return ValueError("Wrong input. Choose in range 1-45")

        if n <= 2:
            return n

        number_of_ways = [0] * (n + 1)
        number_of_ways[1] = 1
        number_of_ways[2] = 2

        for i in range(3, n + 1):
            number_of_ways[i] = number_of_ways[i - 1] + number_of_ways[i - 2]

        return number_of_ways[n]


def main():
    solution = Solution()
    user_input_1 = 4
    user_input_2 = 15
    user_input_3 = 300

    number_of_ways = solution.climbStairs(user_input_1)
    print(f"For {user_input_1} => {number_of_ways} ways to climb to the top.")
    number_of_ways = solution.climbStairs(user_input_2)
    print(f"For {user_input_2} => {number_of_ways} ways to climb to the top.")
    number_of_ways = solution.climbStairs(user_input_3)
    print(f"For {user_input_3} => {number_of_ways}.")


if __name__ == '__main__':
    main()
