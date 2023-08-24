"""
Expressões lambda (funções anonimas)!
A expressão lambda ou anonima, é uma função que não possui nome, é utilizada para simplicar e economizar linhas de cod
"""


def funcao(x, y):
    return x * y


var = funcao(10, 10)

#        parametros|return
mult = lambda x, y: x * y  # Faz a mesma função que def de cima!
print(mult(10, 2))  # -> passando valores

# Onde devo usar!
lista = [
    ['P1', 13],
    ['P2', 3],
    ['P3', 10],
    ['P4', 9],
]
"""
def Organizar(item):
return (item[1])

lista.sort(key=Organizar)  # Tive que fazer um def para poder organizar a lista
"""
organizar = lambda i: i[0]

# A dois jeitos para organizar
print(sorted(lista, key=organizar, reverse=True))
print(lista.sort(key=lambda item: item[1]))  # Fiz a mesma coisa que def, mas economizei tempo e memoria!
