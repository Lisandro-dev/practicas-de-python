import os
import shutil


print(os.getcwd())

archivo=open('curso.txt', 'w')
archivo.write('Texto de prueba')
archivo.close()
print(os.listdir())

#shutil lo que nos permite es poder mover archivos

#shutil.move('curso.txt', 'C:\\Users\\lglaf\\OneDrive\\Escritorio')


for ruta, carpetas, archivos in os.walk(r'C:\Users\lglaf\OneDrive\Escritorio'):
    print("Ruta:", ruta)
    print("Carpetas:", carpetas)
    print("Archivos:", archivos)
    print("------")

lista = list(os.walk(r'C:\Users\lglaf\OneDrive\Escritorio'))
print(lista)

