def CalcularPapel(n, m):
    return n * m if n >= 0 and m >= 0 else 0

qtdAlunos = 10
deverPapeis = 5

print(CalcularPapel(qtdAlunos, deverPapeis))