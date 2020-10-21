n = int(input())
T = list(map(int, input().split(' ')))
print(len([t for t in T if t < 0]))