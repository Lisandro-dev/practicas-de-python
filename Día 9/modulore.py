import re

texto="Si necesitas ayuda llama al (658)-598-9977 las 24 horas del día."

patron="ayuda"

busqueda = re.search(patron,texto)
