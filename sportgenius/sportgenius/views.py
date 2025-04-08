from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import pickle

def predecir_rendimiento(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        altura = float(request.POST.get('altura'))
        peso = float(request.POST.get('peso'))
        velocidad = float(request.POST.get('velocidad'))
        posicion = request.POST.get('posicion')
        nivel = request.POST.get('nivel')

        # Cargar el modelo entrenado
        with open('models/modelo.pkl', 'rb') as f:
            model = pickle.load(f)

        # Preparar los datos para la predicción
        nuevo_atleta = pd.DataFrame({
            'altura': [altura],
            'peso': [peso],
            'velocidad': [velocidad],
            'posicion_Defensa': [1 if posicion == 'Defensa' else 0],
            'posicion_Delantero': [1 if posicion == 'Delantero' else 0],
            'posicion_Medio': [1 if posicion == 'Medio' else 0],
            'nivel_Profesional': [1 if nivel == 'Profesional' else 0],
            'nivel_Aficionado': [1 if nivel == 'Aficionado' else 0]
        })

        # Hacer la predicción
        prediccion = model.predict(nuevo_atleta)
        return JsonResponse({'prediccion': int(prediccion[0])})

    return render(request, 'talentos/formulario.html')