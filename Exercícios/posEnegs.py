def contarEsomar(arr):
    cont = 0
    soma = 0
    if len(arr) > 0:
        for n in arr:
            if n > 0:
                cont += 1
            elif n < 0:
                soma += n
    else:
        return []
    return [cont, soma]

def atualizado(arr):
    cont = sum(1 for n in arr if n > 0)
    soma = sum(n for n in arr if m < 0)
    return [cont, soma] if len(arr) > 0 else []

print(contarEsomar([10, 20, 30, 0, 20, 0, -12, -12]))
print(atualizado([10, 20, 30, 0, 20, 0, -12, -12]))