#-*- coding: utf-8 -*-

arquivo = open('dados2.txt', 'r')

conteudo = arquivo.read()

print("Tipo de conteúdo: ", type(conteudo))

print("Conteúdo retornado pelo read:")

print(repr(conteudo))

arquivo.close()