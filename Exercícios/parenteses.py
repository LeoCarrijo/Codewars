import re

# palavra = 'banana'; novaPalavraArray = []

# for char in palavra:
#     qtdChar = len(re.findall(f'{char}', palavra, re.IGNORECASE))
#     if qtdChar == 1:
#         novaPalavraArray.append('(')
#     else:
#         novaPalavraArray.append(')')
    
# print(novaPalavraArray)

word = 'tAwZcsI(T'
word = word.lower()

def CalcQtyChar(char, txt):
    return txt.count(char)

newWord = list(map(lambda char: '(' if CalcQtyChar(char, word) == 1 else ')', word))

print(newWord)