l = input().split()
counter = 0
while counter < 2:
    print(1 - int(l[counter]))
    counter += 1
while counter > 1 and counter < 5:
    print(2 - int(l[counter]))
    counter += 1
while counter == 5:
    print(8 - int(l[counter]))
    counter += 1 