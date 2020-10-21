num1, num2, cases = input().split()
num1 = int(num1)
num2 = int(num2)
cases = int(cases)

nums = []

for i in range(cases):
  vari = i+1
  nums.append(vari)
for i in nums:
  if i%num1 == 0 and i%num2 == 0:
    print ("FizzBuzz")
  elif i%num1 == 0:
    print ("Fizz")
  elif i%num2 == 0:
    print ("Buzz")
  else:
    print (i)