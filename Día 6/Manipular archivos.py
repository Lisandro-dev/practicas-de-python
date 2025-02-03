#Como se abre y lee y cierra archivos
mi_archivo=open('Prueba.txt')


una_linea= mi_archivo.readline()
print(una_linea.upper())

una_linea= mi_archivo.readline()
print(una_linea)

una_linea= mi_archivo.readline()
print(una_linea)



mi_archivo.close()
