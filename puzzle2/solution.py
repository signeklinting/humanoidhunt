from collections import defaultdict
# Solution to Puzzle 2 of the Humanoid Hunt
# Created by Signe Klinting
# 2021-01-09


signal = open("input.txt", "r+").readline().strip()


def find_char(char):
    
    C = defaultdict(int)

    for i in range(1, len(signal)):
        if signal[i - 1] == char:
            C[signal[i]] += 1
    
    new_char = max(C, key=C.get)
    
    if new_char == ";":
        return ""
    else:
        return new_char + find_char(new_char)

# Finding the first character in the base value
C = defaultdict(int)
for char in signal:
    C[char] += 1

start_char = max(C, key=C.get)

# Finding the subsequent characters in the base value using the "find_char" function
base_value = start_char + find_char(start_char)
print(base_value)