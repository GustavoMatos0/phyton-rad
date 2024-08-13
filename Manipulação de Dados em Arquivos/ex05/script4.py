import os 

try:
    os.mkdir("ex06")
    print("Diretório criado")
except PermissionError as e:
    print(e)
except FileExistsError as e:
    print(e)
except Exception as e:
    print(e)
    
    

    