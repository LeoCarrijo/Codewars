def triangulo(a, b, c):
    sides = sorted([a, b, c])
    if sides[2] >= (sides[1] + sides[0]): return False
    return True

print(triangulo(3, 1, 2))