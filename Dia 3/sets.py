#Los sets los podemos declarar con la palabra set y entre parentesis o sin la palabra pero entre llaves
#Los sets admiten valores unicos, es decir que no toma en cuenta los repetidos, son inmutables
#dentro de un set solo se puede poner un argumento, por lo que siempre tenemos que poner doble parentesis
mi_set=set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)
otro_set={1,2,3,4,5}
print(otro_set)
#No podemos buscar por indice dentro de un set o modificarlos, podremos buscar de la siguiente manera
print(2 in otro_set)

#Podemos unir dos sets tambien asi
s1={1,2,3}
s2={3,4,5,}
s3=s1.union(s2)
print(s3)

#Tambien podemos agregar valores al set
otro_set.add(25)
print(otro_set)
#y eliminar
otro_set.remove(1)
print(otro_set)
#Para remover es mas seguro isar el metodo discard, ya que si el elemento a eliminar no existe no nos va
#a tirar error
 #El metodo.pop es para tomar un elemento aleatorio dentro del set y el clear para limpiar to do