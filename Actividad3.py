import pandas as pd
 
datos = pd.read_csv("estudiantes.csv")
 
correlaciones = datos.corr(numeric_only=True)
print(correlaciones)
 

relacion = datos["Matricula"].corr(datos["Calificacion_Final"])
print("Correlación matrícula/calificación:", relacion)


relacion = datos["Edad"].corr(datos["Calificacion_Final"])
print("Correlación edad/calificación:", relacion)


relacion = datos["Asistencia"].corr(datos["Calificacion_Final"])
print("Correlación asistencia/calificación:", relacion)


relacion = datos["Examen"].corr(datos["Calificacion_Final"])
print("Correlación examen/calificación:", relacion)


relacion = datos["Horas_Estudio"].corr(datos["Calificacion_Final"])
print("Correlación horas de estudio/calificación:", relacion)