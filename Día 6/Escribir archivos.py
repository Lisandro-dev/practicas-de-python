archivo=open('Prueba.txt', 'w')

lista = ['Hola', 'mundo', 'aquí' ,'estoy', 'otra', 'vez']

for p in lista:
    archivo.writelines(p+'\n')

archivo.close()


otro_archivo=open('Prueba1.txt', 'a')
otro_archivo.write('Otra cosa')
otro_archivo.close()