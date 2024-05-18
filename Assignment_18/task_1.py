# This program gets an integer 'n' and generates a sequence for 'n'.
# The first term of the sequence is 'n' and
# each next terms are calculated in accordance with the following formula:
#       if a previous term is even number - multiply it by 2.
#       if a previous term is odd number - multiply it by 3 and add 1.
# The sequence ends when its term reaches 1.
# The problem is solved by 2 functions (without and with caching) to generate the sequence.

cache = {}


def generate_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def generate_sequence_with_cache(n):
    global cache
    if n in cache:
        return cache[n]

    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)

    cache[sequence[0]] = sequence
    return sequence


def main():
    n = int(input("Enter an integer: "))

    print("Generated sequence without caching: ", generate_sequence(n))
    print("Generated sequence with caching: ", generate_sequence_with_cache(n))


if __name__ == "__main__":
    main()
