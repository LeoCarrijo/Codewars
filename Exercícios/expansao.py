num = 1034
numStr = str(num)
msg = ''
print(numStr)

lista = [int(n) for n in numStr]
lista = [lista[i] * 10 ** (len(lista) - 1 - i) for i in range(len(lista))]
for i in range(len(lista)):
    if lista[i] == 0:
        continue
    else:
        if i == len(lista) - 1:
            msg += str(lista[i])
        else:
            msg += str(lista[i]) + ' + '
print(msg[len(msg) - 2::])
print(msg)