# INTERPOLAÇÃO

nome = "João"
idade = 24
profissao = "professor"
materia = "matemática"

# Old Style % (Não muito usado)

print("Olá, me chamo %s. Tenho %d anos de idade, trabalho como %s e dou aula na matéria de %s." % (nome, idade, profissao, materia))
# Olá, me chamo João. Tenho 24 anos de idade, trabalho como professor e dou aula na matéria de matemática.

# %s -> string
# %d -> int
# %f -> float


# Método format
print("Olá, me chamo {}. Tenho {} anos de idade, trabalho como {} e dou aula na matéria de {}.".format(nome, idade, profissao, materia))
# mesmo resultado de cima...

print("Oi, meu nome é {1} e dou aula de {0}.".format(nome,materia))
# Oi, meu nome é matemática e dou aula de João -> Trocando as posições pelo format()


# f-string
print(f'Olá, me chamo {nome} e tenho {idade} anos de idade.')
# Olá, me chamo João e tenho 24 anos de idade.
