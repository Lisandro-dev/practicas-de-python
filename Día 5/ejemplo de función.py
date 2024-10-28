precios_cafe = [('capuccino', 60000), ('expresso', 41000), ('lagrima', 512000)]

def cafe_mas_caro(lista_precio):
    nombre_cafe=''
    precio_cafe = 0
    for nombre, precio in lista_precio:
        if precio > precio_cafe:
            precio_cafe=precio
            nombre_cafe= nombre
        else: pass
    return nombre_cafe, precio_cafe

cafe_caro, precio_caro= cafe_mas_caro(precios_cafe)
print(f'El cafe mas caro es {cafe_caro}, cuyo precio es {precio_caro}')