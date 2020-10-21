k = 0
while True:
    n = int(input())
    if n == 0:
        break
    l = []
    for i in range(n):
        if i%2 == 0:
            l.insert(int(i/2), input())
        else:
            l.insert((int(len(l)) - int(i/2)), input())
    k += 1
    print('SET', k)
    for name in l:
        print(name)