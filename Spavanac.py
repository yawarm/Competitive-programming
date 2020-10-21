hour, minute = (input()).split()
minute = int(minute) - 45

if minute <0:
    minute = 60 + minute
    hour = int(hour) - 1
    if hour < 0:
        hour += 24
else:
    minute

print(hour, minute)