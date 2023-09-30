def CalcularMedia(media, notas):
    return True if media > round(sum(notas) / len(notas), 1) else False

notas = [5, 3, 5, 2, 8, 4, 5]
media = 4.7

print(CalcularMedia(media, notas))