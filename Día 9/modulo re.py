import re

texto="Si necesitas ayuda llama al (658)-598-9977 las 24 horas del día. Otra ayuda"

patron="ayuda"

busqueda=re.search(patron,texto)

print(busqueda)  # Esto mostrará el objeto Match o None
print(busqueda.start())  # Esto mostrará la posición inicial de la coincidencia
print(busqueda.end())    # Esto mostrará la posición final de la coincidencia

otrabusqueda=re.findall(patron,texto)
print(otrabusqueda)  # Esto mostrará todas las coincidencias encontradas en una lista

for hallazgo in re.finditer(patron,texto):
    print(hallazgo.span())
    print(hallazgo.group())

texto2="Llama al 658-588-9977"
patron2=r'(\d{3})-?(\d{3})-?(\d{4})'
resultado=re.search(patron2,texto2)
print(resultado)
print(resultado.group()) # Muestra el número completo
print(resultado.group(1)) # Muestra el primer grupo (código de área)

clave=input("Ingrese su clave: ")
patron3=r'\D{1}\w{7}' # Una letra seguida de 7 caracteres alfanuméricos
comprobar=re.search(patron3,clave) #Busca la clave en la entrada del usuario
print(comprobar) # Muestra el objeto Match si coincide, o None si no coincide

texto3="No atendemos los jueves ni los viernes"
buscar=re.search(r'...demos...', texto3)
print(buscar)