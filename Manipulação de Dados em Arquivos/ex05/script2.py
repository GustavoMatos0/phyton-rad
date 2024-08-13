import os

arq_remover = "arq_remover.txt"

try:
    os.remove(arq_remover)
    print(f"O arquivo {arq_remover} foi removido com sucesso.")
except FileNotFoundError:
    print(f"O arquivo {arq_remover} não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado. {e}")
