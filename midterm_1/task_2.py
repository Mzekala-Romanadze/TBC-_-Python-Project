# Task_2: (8 ქულა) Დაწერეთ პროგრამა რომელიც მოხმარებელს მოსთხოვს
# შეიყვანოს მთელი რიცხვი n, სადაც 100<= n < 1000.
# Თუ მომხმარებელი შეიყვანს არასწორ რიცხვს ეკრანზე დაბეჭდეთ
# რომ პროგრამას გადმოეცა არასწორი რიცხვი და შეწყვიტეთ პროგრამის მუშაობა.
# Თუ მომხმარებელი შეიყვანს სწორ რიცხვს, პროგრამამ უნდა იპოვოს ყველა
# 13 ის ჯერადი რიცხვი 1-დან n-მდე. Ეკრანზე დაბეჭდოს
# ეს რიცხვები და მათი საერთო რაოდენობა.

BASE_NUMBER = 13


def find_multiples(n):
    multiples = 0
    for multiple in range(1, n):
        if multiple % BASE_NUMBER == 0:
            print(multiple)
            multiples += 1
    return multiples


def main():
    n = int(input("Enter n [100-1000): "))
    if not 100 <= n < 1000:
        print("Please, enter n in range [100, 1000).")
        return None
    number_of_multiples = find_multiples(n)
    print("Total number of multiples: ", number_of_multiples)


if __name__ == "__main__":
    main()
