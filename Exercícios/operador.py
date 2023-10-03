operador = '+'
n1 = 5
n2 = 10

def Operador(op, n1, n2):
    return eval(f'{n1} {op} {n2}')

print(Operador(operador, n1, n2))