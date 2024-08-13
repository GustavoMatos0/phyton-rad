import os

try:
    entradas = os.scandir("ex05")
    
    for obj in entradas:
        print(obj)
        print("Nome:",obj.name)
        print("Caminho:",obj.path)
        print("É diretório:",obj.is_dir())
        print("É arquivo:",obj.is_file())
        if(obj.is_file):
            print("Tamanho:", obj.stat().st_size, "B")
        print("\n----------------------------------------------------")
        
except FileNotFoundError as e:
    print(f"Caminho não existe {e}")
except NotADirectoryError as e:
    print(f"Caminho não é um diretorio {e}")