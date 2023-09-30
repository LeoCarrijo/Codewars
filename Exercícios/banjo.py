def Banjo(nome):
    return f'{nome} toca banjo' if nome[0].lower() == 'r' else f'{nome} nao toca banjo'

print(Banjo('Leo'))