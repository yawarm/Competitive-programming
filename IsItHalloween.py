Months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

Month, Date = input().split()

if (Month == Months[9] and int(Date) == 31) or ( Month == Months[11] and int(Date) == 25):
    print('yup')
else:
    print('nope')