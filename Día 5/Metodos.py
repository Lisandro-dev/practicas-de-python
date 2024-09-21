dic={'clave1':100,'clave2':200}
#Ejemplo de método
a=dic.popitem()
print(a)
print(dic)
#presionando ctrl y parandote arriba del metodo podesd ver la definición de la clase
#Práctica 1
var1=",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
print(var1.lstrip(':_#,,,,,,:::____##'))
#Práctica 2
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(4,'naranja')
print(frutas)
#Práctica 3
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
b=marcas_smartphones.isdisjoint(marcas_tv)
print(b)