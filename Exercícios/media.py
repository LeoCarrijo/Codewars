n1 = 70
n2 = 80
n3 = 90

def nota(x, y, z):
    media = sum([x, y, z]) / 3
    if 90 <= media <= 100: return 'A'
    elif 80 <= media < 90: return 'B'
    elif 70 <= media < 80: return 'C'
    elif 60 <= media < 70: return 'D'
    return 'F'

print(nota(n1, n2, n3))