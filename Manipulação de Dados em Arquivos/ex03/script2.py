 # -*- coding: utf-8 -*-

arquivo = open('dados2.txt', 'r')

conteudo = arquivo.readline()

print("Tipo de conteúdo: ", type(conteudo))

print("Conteúdo retornado pelo read:")

print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print("Próximo conteúdo retornado: ")
print(repr(proximo_conteudo))



arquivo.close()