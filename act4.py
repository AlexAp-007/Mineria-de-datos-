import pandas as pd
import matplotlib.pyplot as plt
datos = pd.read_csv("estudiantes.csv")
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

#
promedios = datos[["Edad", "Asistencia", "Examen"]].mean()
ax[0, 0].bar(promedios.index, promedios.values)
ax[0, 0].set_title("Gráfica de Barras")


ax[0, 1].hist(datos["Calificacion_Final"], bins=5)
ax[0, 1].set_title("Histograma")


ax[1, 0].scatter(datos["Horas_Estudio"], datos["Calificacion_Final"])
ax[1, 0].set_title("Gráfica de Dispersión")
ax[1, 0].set_xlabel("Horas de Estudio")
ax[1, 0].set_ylabel("Calificación")


ax[1, 1].boxplot(datos["Calificacion_Final"])
ax[1, 1].set_title("Boxplot")

plt.tight_layout()
plt.show()