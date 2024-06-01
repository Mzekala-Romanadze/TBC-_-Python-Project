# This program gets an integer 'n' and generates a sequence for 'n'.
# The first term of the sequence is 'n' and
# each next terms are calculated in accordance with the following formula:
#       if a previous term is even number - multiply it by 2.
#       if a previous term is odd number - multiply it by 3 and add 1.
# The sequence ends when its term reaches 1.
# The problem is solved by 2 functions (without and with caching) to generate the sequence.

# This program gets an integer 'n' and generates a sequence for 'n'.
# The first term of the sequence is 'n' and
# each next terms are calculated in accordance with the following formula:
#       if a previous term is even number - multiply it by 2.
#       if a previous term is odd number - multiply it by 3 and add 1.
# The sequence ends when its term reaches 1.
# The problem is solved by 2 functions (without and with caching) to generate the sequence.

cache = {}
counter = 0


def generate_sequence(n):
    global cache
    global counter

    counter = 0
    original_n = n

    sequence = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        counter += 1

    cache[original_n] = sequence
    return cache[original_n]


def check_cache_values(n):
    global cache

    sequence = []
    for _, value in cache.items():
        for i in value:
            if i == n:
                index = value.index(i)
                sequence += value[index + 1:]
                break
    return sequence


def generate_sequence_with_cache(n):
    global cache
    global counter
    counter = 0

    checked = check_cache_values(n)

    original_n = n
    sequence = []
    while n != 1:
        if n in cache:
            sequence += cache[n]
            counter += 1
            break
        if checked:
            counter += 1
            return checked
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        counter += 1

    cache[original_n] = sequence
    return cache[original_n]


def main():
    global counter

    num_1 = int(input("Enter an integer: "))
    num_2 = int(input("Enter an integer: "))
    num_3 = int(input("Enter an integer: "))

    print(f"Generated sequence without caching: {generate_sequence(num_1)} Number of calculations: {counter}")
    print(f"Generated sequence with caching: {generate_sequence_with_cache(num_2)} Number of calculations: {counter}")
    print(f"Generated sequence with caching: {generate_sequence_with_cache(num_3)} Number of calculations: {counter}")


if __name__ == "__main__":
    main()
