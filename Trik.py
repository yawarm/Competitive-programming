s = input()

index = 0
pos = 1
while index < int(len(s)):
    if s[index] == 'A':
        if pos == 1:
            pos += 1
        elif pos == 2:
            pos -= 1
    if s[index] == 'B':
        if pos == 2:
            pos += 1
        elif pos == 3:
            pos -= 1
    if s[index] == 'C':
        if pos == 1:
            pos += 2
        elif pos == 3:
            pos -= 2
    index += 1

print(pos)