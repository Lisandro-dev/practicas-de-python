from collections import Counter
from collections import defaultdict
from collections import namedtuple

numeros = [808,5,4,6,7,5,6,4,8,4,2,3,4,64,5,4,2,8,4,1,6]

print(Counter(numeros))

print(Counter('Misssisipi'))

frase = 'Que lo que kiere la chola, lo que kiere es que la besen'

print(Counter(frase))
print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,8,8,8,8,8,8,8,8,8,8])
print(serie.most_common(2))
print(list(serie))

mi_dic = {'uno':'verde', 'dos':'azul', 'tres': 'rojo'}
print(mi_dic['uno'])

mi_dic2 = defaultdict(lambda: 'nada')
mi_dic2['uno']='verde'
mi_dic2['tres']='rojo'
print(mi_dic2['cinco'])

mi_tupla=(200,18,65)
print(mi_tupla)

Persona=namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel=Persona('Ariel', 1.76,80)
print(ariel[1])