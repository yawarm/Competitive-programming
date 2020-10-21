r = []
r_a = []
c_a = []
rep = int(input())

for i in range(rep):
    revenue, revenue_ad, cost_ad = input().split()
    r.append(revenue)
    r_a.append(revenue_ad)
    c_a.append(cost_ad)

index = 0
while index < len(r):
    if int(r[index]) > int(r_a[index]) - int(c_a[index]):
        print('do not advertise')
    elif int(r_a[index]) - int(c_a[index]) > int(r[index]):
        print('advertise')
    elif int(r[index]) == int(r_a[index]) - int(c_a[index]):
        print('does not matter')
    index += 1