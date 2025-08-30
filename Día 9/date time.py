import datetime
from datetime import date

mi_hora= datetime.time(17, 35)

print(mi_hora)
print(mi_hora.hour)

mi_dia=datetime.date(2025,10,12)
print(mi_dia)
print(mi_dia.ctime())
print(mi_dia.today())

nacimiento=date(2025, 12, 5)
defuncion=date(2070,10,12)
vida=defuncion-nacimiento
print(vida.days)

hoy = datetime.datetime.today()   # fecha y hora actual
print("Ahora:", hoy)

minutos = hoy.minute              # obtiene los minutos
print("Minutos:", minutos)
