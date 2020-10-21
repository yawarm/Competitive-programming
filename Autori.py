name = input()
l = name.split('-')
index = 0
nam_1 = ''

while index <= len(l) - 1:
    nam = l[index][0:1]
    nam_1 += nam
    index += 1

print(nam_1)