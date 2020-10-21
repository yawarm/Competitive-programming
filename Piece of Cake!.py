V, x, y = map(int, input().split())
print((V - x if V - x > x else x) * (V - y if V - y > y else y) * 4)