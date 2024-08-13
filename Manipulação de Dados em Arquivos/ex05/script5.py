import os
import errno

try:
    os.rmdir("meu_dir")
    print("Diretorio removido")
except OSError as e:
    print(e.errno)
    if(e.errno == errno.ENOTEMPTY):
        print("O diretorio não esta vazio")
    else:
        print("Erro inesperado")
    print(e)