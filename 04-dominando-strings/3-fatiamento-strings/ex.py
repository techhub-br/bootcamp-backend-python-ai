# Fatiamento de strings - técnica usada pra retornar substrings (partes da string original)

nome = "João Carvalho da Silva Souza Neto Santos"

print(nome[0])
# J <- Primeiro caractere do nome

print(nome[5:13])
# Carvalho <- Pega do caractere 5 até o 12 (conta um a mais no final)

print(nome[:13])
# João Carvalho <- Pega do começo (indice 0) até o 12

print(nome[17:33:2])
# SlaSuaNt <- Incluindo o passo, ele pega a lista de 2 em 2

print(nome[::-1])
# sotnaS oteN azuoS avliS ad ohlavraC oãoJ <- Com o passo negativo, espelha a string
