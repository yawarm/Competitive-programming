from math import sin, cos, pi

N = int(input())
for i in range(N):
  v, theta, x, h1, h2 = map(float, input().split())
  thetaRad = theta * (pi/180)
  t = x / (v * cos(thetaRad))
  y = (v * t * sin(thetaRad)) - (0.5 * 9.81 * t**2)
  if y - h1 >= 1 and h2 - y >= 1:
    print("Safe")
  else:
    print("Not Safe")