try:
    #Tentativa de criar um arquivo em um diretório protegido por permissões
    with open("arquivo.txt", "w") as arquivo:
        arquivo.write("Conteúdo do arquivo")
except PermissionError as e:
    print(e)
    
try:
    #Tentativa de criar um arquivo que já existe
    with open("arquivo_existente.txt", 'x') as arquivo:
        arquivo.write("Conteúdo do arquivo")
except FileExistsError as e:
    print(e)


try:
    #Tentativa de abrir um arquivo que não existe
    with open ("arquivo_inex.txt" , 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError as e:
    print(e)
    
arquivo.close()