# Tipos de dados

# Um tipo serve pra definir os comportamentos de um valor pro interpretador
# Informa quais operações eu posso fazer com aquilo e quanto de espaço custa na memória

# Alguns tipos built-in (que já vem no Python) são:
"""
Texto -> str
Numérico -> int,float,complex
Sequência -> list,tuple,range
Mapa -> dict
Coleção -> set,frozenset
Booleano -> bool
Binário -> bytes,bytearray,memoryview
"""

# Tipos numéricos

# INTEIROS - int | Possuem precisão ilimitada
# ex: -41 ,1 ,2 ,4 ,-75 ,45 ,45646578 ... 44412452
print('\nNúmero inteiro - INT')
print(1 + 7) # imprime 8

# NÚMEROS DE PONTO FLUTUANTE - float | Usam casas decimais para números racionais.
# ex: 1.2 ,1.4 ,-7.4 ,0.24 ... 45642.12 
print('\nNúmero com ponto flutuante - FLOAT')
print(4.4 + 7.5)

# Tipos Booleano e string

# BOOLEANO - bool | Divide-se em verdadeiro (True) e falso (False), e é uma subclasse de int, por ter o 0 representado como False e 1 True
# ex: True, False, 0, 1
print('\nValor booleano - BOOL')
print(True)

# STRINGS - str | Representam valores alfanuméricos (letras com números e símbolos)
# ex: "Olá, mundo!", 'oi', "a", ""hehe""" <- Você pode representar dessas formas, sem problemas
print('\nString - STR')
print('Olá, mundo! ' + 'Eu amo Python s2')