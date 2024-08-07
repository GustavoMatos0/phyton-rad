frase1= "Eu amo comer amoras no cafe da manha"

lista_termos1 = frase1.split()
print(lista_termos1)

frase2 = "Amora abacaxi    abacate        banana"
lista_termos2 = frase2.split()
print(lista_termos2)

frase3 = "Carro rebaixado,moto,aviao"
lista_termos3 = frase3.split(',')
print(lista_termos3)

# Resultado obtido por ocorrências 
print("\nContagem direta frase 1: ",frase1.count('amo'))

# Resultado obtido utilizando a quebra da frase em palavras
contador =0
for termo in lista_termos1:
    if termo == 'amo':
        contador+=1
print("Contagem correta: ",contador)

