#kargs key word args, se usa con doble asterisco, se usa para tener una lista indefinida de elementos en un diccionario
def suma(**kwargs):
    total=0
    for clave, valor in kwargs.items():
        print(f"{clave}={valor}")
        total+=valor

    print(total)

suma(x=3, y=4, r=6)

def prueba(num1,num2,*args,**kwargs):
    print(f"el valos de num1 es {num1}")
    print(f"el valos de num2 es {num2}")
    for x in args:
        print(f"El arg es {x}")
    for clave, valor in kwargs.items():
        print(f"{clave}={valor}")


prueba(23,4,5,8,7,6,1,847,x=3, y=4, r=6)

#Práctica 1

def cantidad_atributos(**kwargs):
    total=0
    for clave, valor in kwargs.items():
        total+=1

    print(f"La cantidad total de argumentos es {total}")
cantidad_atributos(x=3, y=4, r=6)

#Práctica 2

def lista_atributos(**kwargs):
    lista=[]
    for valor in kwargs.values():
        lista.append(valor)
    print(lista)

lista_atributos(x=3, y=4, r=6)


#Práctica 3

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}")
    for clave, valor in kwargs.items():
        print(f"{clave}={valor}")

describir_persona("Juan", color_de_pelo="marron",color_de_ojos="azul")