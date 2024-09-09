#Esta es la opción para enumerar una lista sin enumeradores:
lista=['a','b','c']
indice=0
for item in lista:
    print(indice,item)
    indice +=1

#Con enumeradores:
for indice, item in enumerate(lista):
    print(indice, item)

#Podemos almacenar la información de la siguiente manera:

mis_tuples=list(enumerate(lista))
print(mis_tuples)

# Esto me guardo en una nueva lista, no solo el valor, sino tambien el indice, si quisiera consultar el valor de la posición 1
print(mis_tuples[1][1])
 #Práctica 1: Imprime en pantalla frases como la siguiente: '{nombre} se encuentra en el índice {indice}'
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el indice {indice}')
#Practica 2: Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".palabra="Python"0
lista_indices=list(enumerate('Python'))

#Práctica 3: Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre[0]=="M":
        print(indice)
