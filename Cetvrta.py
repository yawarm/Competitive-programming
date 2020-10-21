p_1 = input().split()
p_2 = input().split()
p_3 = input().split()

x = [p_1[0], p_2[0], p_3[0]]
y = [p_1[1], p_2[1], p_3[1]]

l = sorted(x)
k = sorted(y)

if l[0] == l[1]:
    print(l[-1])
else:
    print(l[0])

if k[0] == k[1]:
    print(k[-1])
else:
    print(k[0])