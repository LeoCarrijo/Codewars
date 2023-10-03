def digitalizar(n):
    n = str(n)[::-1]
    lista = [int(x) for x in n]
    return lista

print(digitalizar(1234))