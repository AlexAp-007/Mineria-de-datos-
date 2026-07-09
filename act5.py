import pandas as pd
 
df = pd.read_csv("estudiantes_modelo.csv")
print("Cantidad de alumnos:", len(df))
 
print("Columnas del dataset:")
print(df.columns)
 
print("Cantidad de aprobados y reprobados:")
print(df["Resultado"].value_counts())