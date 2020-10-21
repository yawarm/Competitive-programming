sentence = input()
l1 = sentence.split(' ')
s_l1 = sorted(l1)
l2 = set(l1)
l3 = list(l2)
s_l3 = sorted(l3)

if s_l1 == s_l3:
    print('yes')
else:
    print('no')