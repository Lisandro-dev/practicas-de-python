#Un diccionario se escribe entre llaves, tiene una clave y un valor, clave y valor entre llaves (por separado)
#los separan dos puntos
diccionario={'clave':'valor', 'clave2':'valor2'}
print(type(diccionario))
print(diccionario)
#Como puedo traer el valor de la clave uno, guadandolo en una variable
resultado=diccionario["clave2"]
print(resultado)
#Los diccionarios admiten como valor
# tod tipo de datos, inlcluidas listas y otros diccionarios
dic={'c1':['a','b', 'c'], 'c2':['d','e','f']}
print((dic['c2'][1]).upper())
#agregar una clave y valor a una lista, tambien podemos sobreescribir una clave de la misma forma
dic[2]='g'
print(dic)