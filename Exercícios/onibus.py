lista = [[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]
pessoasTotal = 0; pessoasRestantes = 0

for parada in lista:
    pessoasTotal += parada[0] - parada[1]
print(pessoasTotal)