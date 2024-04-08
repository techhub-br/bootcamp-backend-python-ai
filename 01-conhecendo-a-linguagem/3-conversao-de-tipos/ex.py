# Em algumas horas precisamos converter o tipo de uma variável pra manipular

# Inteiro pra float
preco = 10
print(preco)
#>> 10
preco = float(preco)
print(preco)
#>> 10.0

print('--------')


# Float para inteiro
quantidade_elementos = 10.40
print(quantidade_elementos)
#>> 10.40
quantidade_elementos = int(quantidade_elementos)
print(quantidade_elementos)
#>> 10

print('---------')


# Numérico para string
preco_casa = 2.50
idade = 14

# FORMA Nº1 - com o construtor str
print(str(preco_casa))
print(str(idade))

# FORMA Nº2 - concatenando strings
mensagem = f"Você tem {idade} anos e consegue comprar uma casa no valor de R${preco_casa}"
print(mensagem)

print('----------')


# String para número
preco_apartamento = "45.20"
idade_maxima = "90"

# print(idade_maxima + 7) -> ERRO! Não concatena string com int
print(int(idade_maxima) + 7)
#>> 97

print('-------------')


# Erro de conversão
# Nem sempre conseguimos converter tipos, então o interpretador nos lança um erro, ex:
preco_computador = "banana"
print(preco_computador) # <- str
# print(int(preco_computador)) <- ValueError: invalid literal for int() with base 10: 'banana'

