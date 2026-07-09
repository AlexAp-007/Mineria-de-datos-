import pandas as pd
datos = pd.read_csv("estudiantes.csv")
columnas = ["Edad", "Asistencia", "Tareas", "Examen", "Horas_Estudio"]
for columna in columnas:
    print(f"\n--- {columna} ---")
    print("Media:", datos[columna].mean())
    print("Mediana:", datos[columna].median())
    print("Moda:", datos[columna].mode().tolist())