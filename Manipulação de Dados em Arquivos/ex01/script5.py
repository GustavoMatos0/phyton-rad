
arquivo = open("dados1.txt", "r")

conteudo = arquivo.read()
print("Todo conteudo do arquivo")
print(repr(conteudo), "\n")

conteudo_releitura = arquivo.read()
print("Releitura de todo o conteudo do arquivo")
print(repr(conteudo_releitura), "\n")

arquivo.close()


arquivo_reaberto = open("dados1.txt", "r")

conteudo_reaberto = arquivo_reaberto.read()
print("Todo conteudo do arquivo novamente")
print(repr(conteudo_reaberto), "\n")

arquivo_reaberto.seek(0)
conteudo_seek = arquivo_reaberto.read()
print("Todo conteudo do arquivo após o SEEK")
print(repr(conteudo_reaberto))

arquivo_reaberto.close()