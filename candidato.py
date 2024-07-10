import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

# 1. Leer los datos
data = pd.read_csv('datos_candidatos.csv')

# 2. Crear un nuevo DataFrame para el candidato
nuevo_candidato = pd.DataFrame({
    'ExperienciaTotal': [10],
    'ExpProyectosSimilares': [4],
    'ExpGestionProyectos': [2],
    'TituloUniversitario': [1],
    'Certificaciones': [2],
    'CursosAdicionales': [3],
    'SoftwareDiseno': [4],
    'Normativas': [4],
    'CalculosEstructurales': [3],
    'Liderazgo': [5],
    'Comunicacion': [4],
    'Referencias': [5]
})

# 3. Separar características y objetivo
X = data.drop('Exitoso', axis=1)
y = data['Exitoso']

# 4. Inicializar y ajustar StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5. Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 6. Crear y entrenar el modelo SVM
model = SVC(kernel='linear', C=1.0)
model.fit(X_train, y_train)

# 7. Escalar los datos del nuevo candidato
nuevo_candidato_scaled = scaler.transform(nuevo_candidato)

# 8. Predecir el resultado para el nuevo candidato
prediccion = model.predict(nuevo_candidato_scaled)

# 9. Imprimir la predicción
print(f'Predicción para el nuevo candidato: {prediccion}')
