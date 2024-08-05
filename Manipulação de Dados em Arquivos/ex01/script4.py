arquivo = open("dados1.txt", "r")

print("Iterando sobre o arquivo")
for linha in arquivo:
    print(repr(linha))

arquivo.close()