# scripts/entrenamiento.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Cargar datos preprocesados
data = pd.read_csv('../SportGenius/data/datos_procesados.csv')

# Dividir los datos en entrenamiento y prueba
X = data.drop('rendimiento', axis=1)
y = data['rendimiento']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un modelo de Random Forest
model = RandomForestClassifier(n_estimators=100, max_depth=None, random_state=42)
model.fit(X_train, y_train)

# Evaluar el modelo
y_pred = model.predict(X_test)
print(f'Precisión del modelo: {accuracy_score(y_test, y_pred)}')

# Guardar el modelo entrenado
with open('../SportGenius/models/modelo.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Modelo guardado en 'models/modelo.pkl'")