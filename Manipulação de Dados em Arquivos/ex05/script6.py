import os 

try:
    os.rmdir("meu_dir")
    print("Diretório removido")
except PermissionError as e:
    print("Sem premissão", e)
except FileExistsError as e:
    print("Diretório não existe", e)
except OSError as e:
    print(e)
except Exception as e:
    print(e)
    
    

    