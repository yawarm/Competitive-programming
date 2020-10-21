N = int(input())
l = []
counter = 0
for i in range(N):
    a = int(input())
    if a%2 == 0:
        l.append(str(a) + ' is even')
    else:
        l.append(str(a) + ' is odd')
while counter < N:
    print(l[counter])
    counter += 1