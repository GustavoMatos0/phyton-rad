arquivo = open("dados1.txt", "r")

conteudo = arquivo.read()

print("Tipo do conteúdo:", type(conteudo))
print (repr(conteudo))

arquivo.close()
