word = input("Enter a string: ")

def count_chars(word):
    v, c, sp, o = 0, 0, 0, 0
    for ch in word:
        if ch.lower() in "aeiou":
            v += 1
        elif ch.isalpha():
            c += 1
        elif ch.isspace():
            sp += 1
        else:
            o += 1
    print(f"Vowels: {v}, Consonants: {c}, Spaces: {sp}, Others: {o}")

count_chars(word)