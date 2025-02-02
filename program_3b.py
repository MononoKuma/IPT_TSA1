def pattern_b():
    for i in range(1, 10, 2):
        print("" * ((7 - i) // 2) + str(i) * i)

pattern_b()