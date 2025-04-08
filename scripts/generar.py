import pandas as pd
import os

ruta = os.path.abspath("../SportGenius/data/jugadores.csv")
datos = {
    'altura': [1.80, 1.75, 1.85],
    'peso': [75, 70, 80],
    'velocidad': [10.5, 11.0, 10.0],
    'posicion': ['Delantero', 'Defensa', 'Medio'],
    'nivel': ['Profesional', 'Aficionado', 'Profesional'],
    'rendimiento': [1, 0, 1]
}

df = pd.DataFrame(datos)
df.to_csv(ruta)
print("Datos generados...." + ruta)