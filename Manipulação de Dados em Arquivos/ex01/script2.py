arquivo = open("dados1.txt", "r")

conteudo = arquivo.readline()

print("Tipo do conteúdo:", type(conteudo))

print("Conteúdo retornado pelo readlines:")
print (repr(conteudo))


proximoconteudo = arquivo.readline()

print("Próximo Conteudo retornado:")
print(repr(proximoconteudo))


arquivo.close()
