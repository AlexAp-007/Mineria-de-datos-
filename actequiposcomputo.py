import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv('equipos_computo.csv')

df = df.drop(columns=['ID_Equipo'])

df = pd.get_dummies(df, columns=['Laboratorio'], drop_first=True)

le = LabelEncoder()
df['Estado_Equipo_Encoded'] = le.fit_transform(df['Estado_Equipo'])

y = df['Estado_Equipo_Encoded']
X = df.drop(columns=['Estado_Equipo', 'Estado_Equipo_Encoded'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

mlp = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=1000, random_state=42)
mlp.fit(X_train_scaled, y_train)


y_pred = mlp.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=le.classes_)

print("=== RESULTADOS DE LA EVALUACIÓN ===")
print(f"Precisión (Accuracy): {acc * 100}%")
print("\nReporte de Clasificación:\n", report)


print("\n=== 5 PREDICCIONES DE PRUEBA ===")
sample_X = X_test.head(5)
sample_X_scaled = scaler.transform(sample_X)

predictions = mlp.predict(sample_X_scaled)
predicted_classes = le.inverse_transform(predictions)
actual_classes = le.inverse_transform(y_test.head(5))

for i in range(5):
    print(f"Instancia {i+1}:")
    print(f"  Predicción de la IA: {predicted_classes[i]}")
    print(f"  Estado Real: {actual_classes[i]}")
    if predicted_classes[i] == actual_classes[i]:
        print(" Resultado: Correcto \n")
    else:
        print(" Resultado: Incorrecto \n")