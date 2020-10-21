q = []
t = []
rep = int(input())
for i in range(rep):
    quality, time = (input()).split()
    q.append(quality)
    t.append(time)

index = 0
s = []
while index < len(q):
    ans = float(q[index]) * float(t[index])
    s.append(ans)
    index += 1

Sum = sum(s)
pass
print('%.3f' % Sum)