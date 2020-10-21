n = int(input())
l = [int(x) for x in input().split(" ")]
s = 0
for x in l:
    if x < 0:
        n -= 1
    else:
        s += x
print(s/n)