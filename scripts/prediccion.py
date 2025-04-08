# scripts/prediccion.py
import pandas as pd
import pickle
import joblib

# Cargar el modelo entrenado
with open('../SportGenius/models/modelo.pkl', 'rb') as f:
    model = pickle.load(f)

# Cargar el encoder y el scaler
encoder = joblib.load('../SportGenius/models/encoder.pkl')
scaler = joblib.load('../SportGenius/models/scaler.pkl')

# Datos de un nuevo atleta (ejemplo)
nuevo_atleta = pd.DataFrame({
    'altura': [1.80],
    'peso': [75],
    'velocidad': [10.5],
    'posicion': ['Delantero'],
    'nivel': ['Profesional']
})

# Codificar las columnas categóricas
categorical_data = encoder.transform(nuevo_atleta[['posicion', 'nivel']]).toarray()

# Normalizar los datos numéricos
numeric_data = scaler.transform(nuevo_atleta[['altura', 'peso', 'velocidad']])

# Combinar datos
nuevo_atleta_procesado = pd.concat(
    [
        pd.DataFrame(numeric_data, columns=['altura', 'peso', 'velocidad']),
        pd.DataFrame(categorical_data, columns=encoder.get_feature_names_out(['posicion', 'nivel']))
    ],
    axis=1
)

# Hacer la predicción
prediccion = model.predict(nuevo_atleta_procesado)
print(f'Predicción de rendimiento: {prediccion[0]}')