import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


# --- Generazione dati di esempio senza numpy ---
# Input: 1000 campioni, 5 feature ciascuno
X = []
y = []


random.seed(42)
for _ in range(1000):
    features = [random.random() for _ in range(5)]


    # Simuliamo output con formule lineari + rumore
    temperatura = features[0]*50 + features[1]*20 + random.gauss(0, 0.5)
    pressione = features[2]*5 + features[3]*10 + random.gauss(0, 0.2)
    velocita = features[1]*30 + features[4]*15 + random.gauss(0, 0.3)


    X.append(features)
    y.append([temperatura, pressione, velocita])


# --- Definizione modello ---
model = Sequential([
    Dense(30, activation='relu', input_shape=(5,)),
    Dense(30, activation='relu'),
    Dense(30, activation='relu'),
    Dense(3) # 3 output continui (temperatura, pressione, velocità)
])


# Compilazione modello
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')


# Allenamento modello
model.fit(X, y, epochs=50, batch_size=32, validation_split=0.2)


# Test modello con un nuovo input
X_new = [[0.2, 0.4, 0.1, 0.3, 0.5]]
y_pred = model.predict(X_new)


print(f"Input: {X_new}")
print(f"Predizioni (Temperatura, Pressione, Velocità): {y_pred}")

