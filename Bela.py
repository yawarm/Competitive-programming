l = []
s = []
rep, dominant = str((input())).split()
dom = {'J': 20, '9': 14, 'K': 4, 'A': 11, 'Q': 3, 'T': 10, '8': 0, '7': 0}
poeng = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}
for i in range(4*int(rep)):
    l.append(input())

index = 0
while index < len(l):
    if l[index].find(dominant) == 1:
        s.append(dom[l[index][0:1]])
    else:
        s.append(poeng[l[index][0:1]])
    index += 1
    
total = sum(s)
print(total)