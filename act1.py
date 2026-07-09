import pandas as pd
datos = pd.read_csv("estudiantes.csv")
columnas = ["Edad", "Tareas", "Horas_Estudio", "Calificacion_Final"]
for columna in columnas:
    print(f"\n--- {columna} ---")
    print("Rango:", datos[columna].max() - datos[columna].min())
    print("Varianza:", datos[columna].var())
    print("Desviación estándar:", datos[columna].std())