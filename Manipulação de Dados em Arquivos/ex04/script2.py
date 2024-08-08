from datetime import datetime

frutas = ['Jabuticaba', 'Laranja', 'Pera', 'Tomate']
for fruta in frutas:
    mfruta = f"Nome: {fruta:12} - Número de letras: {len(fruta):5}"
    print(mfruta)
    
print()

pi = 3.1415

# {variavel_float:largura.precisao f}

string_pi = f"O número de PI é: {pi:.1f}"
deslocado_pi = f"PI deslocado é: {pi:10.1f}"
preciso_pi = f"PI mais preciso é: {pi:.4f}"

print(string_pi)
print(deslocado_pi)
print(preciso_pi)

print()

data = datetime.now()

mydata= f"A data de hoje é {data}"
mydata_format = f"A data de hoje formatada é {data:%d/%m/%Y}"
print(mydata)
print(mydata_format)