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
