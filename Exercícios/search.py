lista = ['oi', 12, 'mundo', 42]
item = 42
lista_palavras = [x for x in lista if type(x) == str]
lista_numeros = [x for x in lista if type(x) == int]
if type(item) == int:
    try:
        posicao = lista_numeros.index(item)
    except:
        posicao = -1
elif type(item) == str:
    try:
        posicao = lista_palavras.index(item)
    except:
        posicao = -1
if posicao != -1:
    print(f'O item esta na posicao {posicao}')
else:
    print('O item não esta presenta na lista...')