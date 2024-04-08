# Variáveis são valores que são guardados no programa que podem sofrer alterações no decorrer da execução.
age, name = (18, 'Joãozinho')
print(f'Meu nome é {name} e tenho {age} anos de idade.')
#>> Meu nome é Joãozinho e tenho 18 anos de idade.

print('---')

# Mudando o valor da variável
age, name = (20, 'Maria')
print(f'Meu nome agora é {name} e tenho {age} anos de idade.')
#>> Meu nome agora é Maria e tenho 20 anos de idade.


# CONSTANTES
# Diferente das variáveis, as constantes depois que criadas não podem mais ter seus valores alterados.

# !!! No Python não existe uma palavra-chave pra constante !!!

# Para solucionar isso, usamos uma convenção (uma regra) de declarar constantes em maiúscula
# Ex: AGE, NAME <- Assim, quem ler seu código vai saber que se trata de um valor que não pode ser mudado.
DEBUG = True
STATES = [
    'SP',
    'RJ',
    'MG'
]

# Eu até posso mudar o valor da constante, o interpretador não vai dar erro.
STATES = ['ES', 'BA', 'PB']

# Boas práticas

# O padrão de nomes deve ser snake case (todas_minusculas_separadas_por_underline)
id_aula = 1 # ID da aula

# Nomes sugestivos
# exemplo: quero criar um programa com valor do saque, saldo da conta e nome da pessoa que efetuou a transação

# ERRADO:
# NÃO SER PROGRAMADOR ALFABETO, QUE TUDO COLOCA X, Y, Z (...)
x = 450.5
y = 7812.36
z = 'Rosana Carvalho da Silva Filho'

# CORRETO:
valor_saque = 450.5
valor_saldo = 7812.36
nome_efetuador = 'Rosana Carvalho da Silva Filho'
