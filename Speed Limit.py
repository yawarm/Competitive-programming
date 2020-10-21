V = []
T = []
change = 0
while True:
    n = int(input())
    if n == -1:
        break
    for i in range(n):
        v, t = input().split()
        V.append(v)
        T.append(t)
    S = []
    while change < int(len(V)):
        if change == 0:
            S.append(int(V[change]) * int(T[change]))
        else:
            S.append(int(V[change]) * (int(T[change]) - int(T[change - 1])))
        change += 1
    print(sum(S), 'miles')
    del V[:]
    del T[:]
    del S[:]
    change -= change