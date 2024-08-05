arquivo = open("dados1.txt", "r")

conteudo = arquivo.readlines()

print("Tipo do conteúdo:", type(conteudo))

print("Conteúdo retornado pelo readlines:")
print (repr(conteudo))


arquivo.close()
