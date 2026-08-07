import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Leer el archivo CSV
df = pd.read_csv("clientes (1).csv")

# Mostrar las columnas del archivo
print("Columnas del archivo:")
print(df.columns.tolist())

# Mostrar las primeras filas
print("\nPrimeras filas del dataset:")
print(df.head())

# Variables de entrada
X = df[[
    "Compras_Mensuales",
    "Gasto_Mensual_MXN",
    "Visitas_Web_Mensuales",
    "Satisfaccion"
]]

# Variable de salida
y = df["Nivel_Consumo_Referencia"]

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Escalar datos
escalador = StandardScaler()

X_train_escalado = escalador.fit_transform(X_train)
X_test_escalado = escalador.transform(X_test)

# Crear modelo
modelo = MLPClassifier(
    hidden_layer_sizes=(8, 6),
    activation="relu",
    max_iter=1000,
    random_state=42
)

# Entrenar
modelo.fit(X_train_escalado, y_train)

# Predicciones
predicciones = modelo.predict(X_test_escalado)

print("\nExactitud del modelo:")
print(accuracy_score(y_test, predicciones))

print("\nMatriz de confusión:")
print(confusion_matrix(y_test, predicciones))

print("\nReporte de clasificación:")
print(classification_report(y_test, predicciones))

comparacion = pd.DataFrame({
    "Real": y_test.values,
    "Predicción": predicciones
})

print("\nComparación de resultados:")
print(comparacion)

# Nuevos clientes
nuevos_clientes = pd.DataFrame({
    "Compras_Mensuales": [1, 10, 18],
    "Gasto_Mensual_MXN": [500, 12000, 25000],
    "Visitas_Web_Mensuales": [2, 25, 50],
    "Satisfaccion": [2.5, 4.2, 5.0]
})

# Escalar y predecir
nuevos_clientes_escalados = escalador.transform(nuevos_clientes)
predicciones_nuevas = modelo.predict(nuevos_clientes_escalados)

print("\nPredicciones para nuevos clientes:")
print(predicciones_nuevas)

# Curva de aprendizaje
plt.plot(modelo.loss_curve_)
plt.xlabel("Iteraciones")
plt.ylabel("Error o pérdida")
plt.title("Proceso de aprendizaje de la red neuronal")
plt.show()