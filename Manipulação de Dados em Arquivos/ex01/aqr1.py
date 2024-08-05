import os

arquivo1 = open("dados1.txt","w", encoding='utf-8')

print(os.path.abspath(arquivo1.name))

arquivo1.write("olá mundo \nHello world")

print(os.path.relpath(arquivo1.name))
print(arquivo1)



arquivo1.close()