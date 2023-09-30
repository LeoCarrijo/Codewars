def MenorPalavra(frase):
    palavras = frase.split(' ')
    tamanhos = []
    for palavra in palavras:
        for letra in palavra:
            if letra in ('!', '?', ',', '.'):
                palavra = palavra[:len(palavra) - 1]
        tamanhos.append(len(palavra))
    return min(tamanhos)

def find_short(s):
    return min(len(x) for x in s.split())

print(MenorPalavra('Oi, eu sou o Goku'))
print(find_short('Oi, eu sou o Goku'))