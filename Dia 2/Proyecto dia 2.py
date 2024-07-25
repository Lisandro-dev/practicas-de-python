nombre=input("Por favor dime tu nombre: ")
ventas=input("¿Cual fue el monto de tus ventas?")
ventas=int(ventas)
comision=(ventas*13)/100
#comision=round(comision,2)
print(f"El nombre del vendedor es {nombre} y el total de sus ventas fue de {ventas} pesos y la comision de esas ventas fue de {comision}")