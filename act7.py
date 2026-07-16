import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    r2_score,
    mean_squared_error
)

import os

# ======================================
# CARGAR DATASET
# ======================================

ruta = os.path.join(os.path.dirname(__file__),
                    "dataset_sucursales_mensual.csv")

df = pd.read_csv(ruta)

print("="*60)
print("DATASET ORIGINAL")
print("="*60)

print(df.head())

# ======================================
# ETL
# ======================================

print("\n")
print("="*60)
print("VALORES NULOS")
print("="*60)

print(df.isnull().sum())

# Rellenar valores faltantes con la media

for columna in [
    "Gasto_Publicidad",
    "Descuento_Promedio",
    "Satisfaccion_Cliente",
    "Devoluciones"
]:
    df[columna] = df[columna].fillna(df[columna].mean())

# Eliminar duplicados

df.drop_duplicates(inplace=True)

print("\n")
print("="*60)
print("VALORES NULOS DESPUÉS DE LIMPIAR")
print("="*60)

print(df.isnull().sum())

# Guardar dataset limpio

df.to_csv("dataset_sucursales_limpio.csv", index=False)

print("\nDataset limpio guardado correctamente.")

print("\n")
print("="*60)
print("MEDIA")
print("="*60)
print(df.mean(numeric_only=True))

print("\n")
print("="*60)
print("MEDIANA")
print("="*60)
print(df.median(numeric_only=True))

print("\n")
print("="*60)
print("MODA")
print("="*60)
print(df.mode().iloc[0])

print("\n")
print("="*60)
print("VARIANZA")
print("="*60)
print(df.var(numeric_only=True))

print("\n")
print("="*60)
print("DESVIACIÓN ESTÁNDAR")
print("="*60)
print(df.std(numeric_only=True))

print("\n")
print("="*60)
print("DESCRIPCIÓN GENERAL")
print("="*60)
print(df.describe())

print("\n")
print("="*60)
print("PUBLICIDAD VS VENTAS")
print("="*60)

print(df[['Gasto_Publicidad',
          'Ventas_Totales']].corr())

print("\n")
print("="*60)
print("CLIENTES VS VENTAS")
print("="*60)

print(df[['Clientes_Atendidos',
          'Ventas_Totales']].corr())

print("\n")
print("="*60)
print("SATISFACCIÓN VS VENTAS")
print("="*60)

print(df[['Satisfaccion_Cliente',
          'Ventas_Totales']].corr())

print("\n")
print("="*60)
print("DESCUENTO VS VENTAS")
print("="*60)

print(df[['Descuento_Promedio',
          'Ventas_Totales']].corr())

plt.figure(figsize=(12,8))

sns.heatmap(
    df.select_dtypes(include=np.number).corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Matriz de Correlación")

plt.show()

X = df.drop("Cumplio_Meta", axis=1)

X = pd.get_dummies(X)

y = df["Cumplio_Meta"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

modelo = DecisionTreeClassifier(random_state=42)

modelo.fit(X_train, y_train)

pred = modelo.predict(X_test)

print("\n")
print("="*60)
print("ÁRBOL DE DECISIÓN")
print("="*60)

print("Accuracy")

print(accuracy_score(y_test, pred))

print(classification_report(y_test, pred))

print(confusion_matrix(y_test, pred))

modelo = GaussianNB()

modelo.fit(X_train, y_train)

pred = modelo.predict(X_test)

print("\n")
print("="*60)
print("NAIVE BAYES")
print("="*60)

print("Accuracy")

print(accuracy_score(y_test, pred))

print(classification_report(y_test, pred))

print(confusion_matrix(y_test, pred))

modelo = LogisticRegression(max_iter=1000)

modelo.fit(X_train, y_train)

pred = modelo.predict(X_test)

print("\n")
print("="*60)
print("REGRESIÓN LOGÍSTICA")
print("="*60)

print("Accuracy")

print(accuracy_score(y_test, pred))

print(classification_report(y_test, pred))

print(confusion_matrix(y_test, pred))

X = df[['Gasto_Publicidad']]

y = df['Ventas_Totales']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

modelo = LinearRegression()

modelo.fit(X_train, y_train)

pred = modelo.predict(X_test)

print("\n")
print("="*60)
print("REGRESIÓN LINEAL SIMPLE")
print("="*60)

print("R²")

print(r2_score(y_test, pred))

print("MSE")

print(mean_squared_error(y_test, pred))

X = df.drop("Ventas_Totales", axis=1)

X = pd.get_dummies(X)

y = df["Ventas_Totales"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

modelo = LinearRegression()

modelo.fit(X_train, y_train)

pred = modelo.predict(X_test)

print("\n")
print("="*60)
print("REGRESIÓN MÚLTIPLE")
print("="*60)

print("R²")

print(r2_score(y_test, pred))

print("MSE")

print(mean_squared_error(y_test, pred))

print("\n")
print("="*60)
print("PRÁCTICA FINALIZADA")
print("="*60)