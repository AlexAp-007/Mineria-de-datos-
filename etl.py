import pandas as pd

#Extraer
datos = pd.read_csv("calificaciones.csv")

#Transformar

datos["Promedio"] = (
    datos["Parcial1"] +
    datos["Parcial2"] +
    datos["Parcial3"]
) / 3


datos["Estatus"] = datos["Promedio"].apply(
    lambda x: "Aprobado" if x >= 70 else "Reprobado"
)


datos = datos.sort_values(by="Promedio", ascending=False)


datos.to_csv("calificaciones_procesadas.csv", index=False)

print(datos)

print("\nETL completado correctamente.")