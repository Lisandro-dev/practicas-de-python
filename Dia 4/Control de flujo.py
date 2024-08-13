#Para controlar el flujo de nuestros programas necesitamos 3 palabras el if, else y elif
x=True
mascota="perro"
if mascota=="gato":
    print("Tienes un gato")
elif mascota=="perro":
    print("tienes un perro")
else:
    print("No se que animal tienes")

edad=20
calificacion=12
if edad<18:
    print("Eres menor de edad")
    if calificacion > 7:
        print("Aprobado")
    else:
        print('No aprobado')
else:
    print("Eres adulto")

#Práctica 1
num1=int(input("Ingresa un número:"))
num2=int(input("Ingresa otro número:"))
if num1>num2:
    print(f'{num1} es mayor que {num2}')
elif num2 >num1:
    print(f'{num2} es mayor que {num1}')
else:
    print(f'{num1} y {num2} son iguales')

#Practica2
licencia=False
if edad>18:
    if licencia==True:
        print('Puedes conducir')
    else:
        print('Necesitas una licencia')
else:
    print('Necesitas tener mas de 18 años')
    #Práctica3
habla_ingles=True
sabe_python=False
if habla_ingles == True and sabe_python== True:
    print('Podes trabajar')
elif habla_ingles==True and sabe_python==False:
    print('Necesitas aprender python')
elif habla_ingles==False and sabe_python==True:
    print('Necesitas saber ingles')
else: print('No cumpis las condiciones')