import os
nome_antigo = "arq_antigo.txt"
nome_novo = "arq_novo.txt"

try:
    os.rename(nome_antigo, nome_novo)
    print(f"O arquivo {nome_antigo} foi renomeado para {nome_novo}.")
except FileNotFoundError:
    print(f"O arquivo {nome_antigo} nao foi encontrado.")
except Exception as e:
    print(f"Erro inesperado {e}")