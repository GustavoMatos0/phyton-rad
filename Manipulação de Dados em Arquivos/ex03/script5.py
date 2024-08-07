 # -*- coding: utf-8 -*-

with open('dados2.txt') as arquivo:
    texto = arquivo.read()
    contador = texto.count(",")
    print("Total de virgulas = ", contador)