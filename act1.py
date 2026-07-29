import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("dataset_clientes.csv")

X = df[[
    "Edad",
    "Compras_Mensuales",
    "Gasto_Mensual_MXN",
    "Visitas_Web_Mensuales",
    "Dias_Desde_Ultima_Compra",
    "Tiempo_Sesion_Min",
    "Clicks_Promedio"
]]

X = X.dropna()

escalador = StandardScaler()
X_escalado = escalador.fit_transform(X)
import matplotlib.pyplot as plt

inercias = []

for k in range(1, 11):
    modelo = KMeans(n_clusters=k, random_state=42, n_init=10)
    modelo.fit(X_escalado)
    inercias.append(modelo.inertia_)

plt.figure(figsize=(8,5))
plt.plot(range(1,11), inercias, marker='o')
plt.title("Método del Codo")
plt.xlabel("Número de Clusters")
plt.ylabel("Inercia")
plt.grid(True)
plt.show()

modelo = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clusters = modelo.fit_predict(X_escalado)

df_limpio = X.copy()
df_limpio["Cluster"] = clusters

print(df_limpio)

print("\nPromedio por cluster:\n")
print(df_limpio.groupby("Cluster").mean())
