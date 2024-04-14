curso = 'Python'

print(curso.upper())
# PYTHON -> Joga tudo pra maiúsculo

print(curso.lower())
# python -> Joga tudo pra minúsculo

print(curso.title())
# Python -> Transforma a primeira letra de todas palavras em maiúsculo

# =-=-=-=-=-=-=-=-=-=

palavra_nova = "    batata    "

print(palavra_nova.strip())
# batata -> remove todos espaços no fim e no começo

print (palavra_nova.lstrip())
# "batata    " -> remove os espaços da esquerda

print(palavra_nova.rstrip())
# "    batata" -> remove os espaços da direita

# =-=-=-=-=-=-=-=-=-=

fruta = "morangos"

print(fruta.center(10, '#'))
# #morangos# -> centraliza o texto e adiciona o caractere 

print('.'.join(fruta))
# m.o.r.a.n.g.o.s -> separa a string em letras e adiciona um separador em cada.





