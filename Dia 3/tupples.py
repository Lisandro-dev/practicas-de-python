mi_tuple=(1,2,3,4)
print(type(mi_tuple))
print(mi_tuple[1])
print(mi_tuple[-1])


otro_tuple=(1,2,4,(12,45),5)
print(otro_tuple[3][0])

tercero=(1,2,3,1)
#el metodo count me permite contar cuantas veces aparece el uno en el tupple
print(tercero.count(1))
#el metodo index me idica conde se encuentra el valor
print(tercero.index(2))
