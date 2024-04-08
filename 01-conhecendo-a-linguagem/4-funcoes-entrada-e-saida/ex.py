# Função input()
# É usada quando queremos ler dados do teclado. Recebe um valor do tipo str que é a mensagem que é exibida ao usuário, depois converte o valor inserido para string e retorna-o
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
#>> Digite seu nome: ------- ♥ Depois insere o valor digitado na variável "nome"


# Função print()
# Usa-se quando queremos exibir valores no console, com 4 argumentos opcionais (sep, end, file e flush)
print(nome, sobrenome, end=" bocó\n") # \n aqui indica uma quebra de linha
print(nome, sobrenome, sep="-")


# Links úteis
# https://docs.python.org/3/library/functions.html#input
# https://docs.python.org/3/library/functions.html#print
