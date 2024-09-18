#La función matcvh es como el switch, el valor tiene que estar antes del match
serie='1'
match serie:
    case "1":
        print('Uno')
    case '2':
        print('Dos')
    case '3':
        print('Tres')
    case _:
        print('no hay numero')
#Lo que hice aca abajo es pasarle una estructura en lugar de un numero, y dependiendo de esa estructura el resultado
cliente={'nombre': 'Federico',
         'edad':45,
         'ocupacion': 'instructor'
    }
pelicula={'titulo': 'Matrix',
          'ficha_tecnica': {'protagonista': 'Keanu Reeves',
                            'director': 'wasowski'}}
elementos=[cliente, pelicula, "libro"]
for e in elementos:
    match e:
        case {'nombre': nombre,
         'edad':edad,
         'ocupacion': ocupacion}:
            print(f'es un cliente {nombre} y tiene {edad} años y su profesion es {ocupacion}')
        case {'titulo': titulo,
          'ficha_tecnica': {'protagonista': protagonista,
                            'director': director}}:
            print(f'Es la pelicula {titulo} y su director es {director} su protagonista {protagonista}')
        case _:
            print('No se que es esto')