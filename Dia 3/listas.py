mi_lista=['a','b','c']
lista2= ['a', 23, 23.5,"hola"]
print(type(mi_lista))
print(lista2)
#Como saber cuantos elementos tiene una lista, con la propiedad len
resultado=len(lista2)
print(resultado)
#Como extraigo un valor de la lista, con index (indice)
extraccion=lista2[2]
print(extraccion)
#tambien podemos concatenar listas
lista3=["3", 3,3.3]
print(lista3+lista2)
#Vamos a alterar los elementos de una lista ahora
lista3[2]="reeemplazado"
print(lista3)
#Vamos agreguemos un item a la lista
lista3.append("nuevo elemento")
print(lista3)
#remover elemento de la lista, esto lo logramos con pop, si no especificamos en el parentesis el indice a eliminar
#nos elimina la ultima posicion
lista3.pop(0)
print(lista3)
#Como podemos ordenar las listas, con la propiedad sort
lista4=["d","j","e","l"]
lista4.sort()
print(lista4)
#Como podemos invertir el orden de una lista
lista4.reverse()
print(lista4)