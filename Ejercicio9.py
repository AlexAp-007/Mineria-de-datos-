import csv

alumnos = []

with open("calificaciones.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector)

    for fila in lector:
        matricula = fila[0]
        nombre = fila[1]
        carrera = fila[2]

        cal1 = float(fila[3])
        cal2 = float(fila[4])
        cal3 = float(fila[5])

        promedio = (cal1 + cal2 + cal3) / 3

        alumnos.append({
            "matricula": matricula,
            "nombre": nombre,
            "carrera": carrera,
            "promedio": promedio
        })

# Promedio general
promedio_general = sum(a["promedio"] for a in alumnos) / len(alumnos)

# Mejor y peor alumno
mejor = max(alumnos, key=lambda x: x["promedio"])
peor = min(alumnos, key=lambda x: x["promedio"])

# Aprobados y reprobados
aprobados = sum(1 for a in alumnos if a["promedio"] >= 60)
reprobados = sum(1 for a in alumnos if a["promedio"] < 60)

# Ranking
ranking = sorted(alumnos, key=lambda x: x["promedio"], reverse=True)

print("===== PROMEDIOS =====")
for alumno in alumnos:
    print(f"{alumno['nombre']} -> {alumno['promedio']:.2f}")

print("\n===== PROMEDIO GENERAL =====")
print(f"{promedio_general:.2f}")

print("\n===== MEJOR ALUMNO =====")
print(f"{mejor['nombre']} -> {mejor['promedio']:.2f}")

print("\n===== PEOR ALUMNO =====")
print(f"{peor['nombre']} -> {peor['promedio']:.2f}")

print("\n===== APROBADOS Y REPROBADOS =====")
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")

print("\n===== RANKING =====")
for i, alumno in enumerate(ranking, start=1):
    print(f"{i}. {alumno['nombre']} -> {alumno['promedio']:.2f}")
    