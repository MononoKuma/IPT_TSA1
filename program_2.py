def sum_digits(word):
    total = sum(int(ch) for ch in word if ch.isdigit())
    print(f"Sum of digits: {total}")

word = input("Enter numbers: ")
sum_digits(word)