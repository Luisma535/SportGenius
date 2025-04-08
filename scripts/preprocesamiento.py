import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import os 
import joblib

# Guardar el encoder y el scaler
 
ruta = os.path.abspath("../SportGenius/data/jugadores.csv")
 # scripts/preprocesamiento.py


# Cargar datos
data = pd.read_csv(ruta)

# Limpieza de datos
data = data.dropna()

# Codificación de variables categóricas
encoder = OneHotEncoder()
categorical_data = encoder.fit_transform(data[['posicion', 'nivel']]).toarray()

# Normalización de datos numéricos
scaler = StandardScaler()
numeric_data = scaler.fit_transform(data[['altura', 'peso', 'velocidad']])

# Combinar datos
processed_data = pd.concat(
    [
        pd.DataFrame(numeric_data, columns=['altura', 'peso', 'velocidad']),
        pd.DataFrame(categorical_data, columns=encoder.get_feature_names_out(['posicion', 'nivel'])),
        data['rendimiento']  # Incluir la columna 'rendimiento'
    ],
    axis=1
)

# Guardar datos preprocesados
processed_data.to_csv('../SportGenius/data/datos_procesados.csv', index=False)
import joblib
joblib.dump(encoder, '../SportGenius/models/encoder.pkl')
joblib.dump(scaler, '../SportGenius/models/scaler.pkl')

print("Datos preprocesados guardados en 'data/datos_procesados.csv'")