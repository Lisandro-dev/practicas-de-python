#zip lo que hace es mezclar dos listas en un tupple

nombres = ['Ana', 'Hugo', 'Mario']
edades = [58,47,12]
pais=['Peru','Madrid','Cacheuta']
combinados=list(zip(nombres,pais, edades))

for nombre, ciudad, edad in combinados:
    print(f'Su nombre es {nombre}, su ciudad es {ciudad} y su edad es {edad}')

#Práctica 1
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combi=list(zip(paises, capitales))
for x, i in combi:
    print(f'El pais {x} tiene su capital llamada {i}')

#Práctica 2
marcas = ['vw','bic','nike']
productos =['autos','biromes', 'zapatillas']
mezcla=list(zip(marcas, productos))
for e,r in mezcla:
    print(f'El producto {r} es de la marca {e}')

#Práctica 3
espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros=list(zip(espaniol,portugues,ingles))
print(numeros)
num=1
for q,a,z in numeros:

    print(f'En español {num} se dice {q}, en portugues {a} y en inlges {z}')
    num +=1