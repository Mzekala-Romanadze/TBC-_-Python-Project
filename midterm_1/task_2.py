n = int(input("Enter n in range 100-1000: "))

if 100 <= n <= 1000:
    counter = []
    for i in range(1, n + 1):
        if i % 13 == 0:
            counter.append(i)
    print(counter)
    print(len(counter))
else:
    print("Wrong number. Please, enter n in range 100-1000.")
