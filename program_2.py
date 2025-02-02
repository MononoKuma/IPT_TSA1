def sum_numbers(text):
    total = 0
    
    for char in text:
        if char.isdigit():
            total += int(char)
    
    print(f"Sum of digits: {total}")

text = input("Enter numbers: ")
sum_numbers(text)