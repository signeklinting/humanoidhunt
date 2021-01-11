# Solution to Puzzle 1 of the Humanoid Hunt
# Created by Signe Klinting
# 2021-01-09


password = ""

for line in open("input.txt", "r+").readlines():
    channel = line.strip()

    i = 0
    count = 0

    while i < len(channel):
        byte = int(channel[i:i + 8], 2)
        if byte < len(channel) / 8:
            count = 1
            i = byte * 8
        else:
            if count == 0:
                i += 8
            else:
                password += chr(byte)
                break

print(password)
