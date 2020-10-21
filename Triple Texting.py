s = input()
length = int(len(s)/3)
index = 0
save = ''
while index < length*3:
    a = s[index]
    save += a
    index += 1
    if index == length or index == length*2:
        save += ' '
s = save.split(' ')
index1 = 0
while index1 < len(s):
    if s.count(s[index1]) == 2 or s.count(s[index1]) == 3:
        print(s[index1])
        break
    index1 += 1