archivo=open('Prueba.txt', 'w')

lista = ['Hola', 'mundo', 'aquí' ,'estoy', 'otra', 'vez']

for p in lista:
    archivo.writelines(p+'\n')

archivo.close()


otro_archivo=open('Prueba1.txt', 'a')
otro_archivo.write('Otra cosa')
otro_archivo.close()

 #Ejericio 1
archivo=open('mi_archivo.txt', 'w')

archivo.write('Nuevo texto')
archivo.close()
archivo=open('mi_archivo.txt')
imprimir=archivo.read()

print(imprimir)

#Ejercicio 2
archivo=open('mi_archivo.txt', 'a')

archivo.write('Nuevo inicio de sesión')
archivo.close()
archivo=open('mi_archivo.txt')
imprimir=archivo.read()

print(imprimir)

#Ejercicio 3

archivo=open('registro.txt', 'a')
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

for l in registro_ultima_sesion:
    archivo.writelines(l+'\t')
archivo.close()
archivo=open('registro.txt')
imprimir=archivo.read()

print(imprimir)
