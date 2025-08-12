import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


# --- Dataset di esempio (generato casualmente) ---
# Input: 5 features (esempio)
np.random.seed(42)
X = np.random.rand(1000, 5)


# Output: temperatura, pressione, velocità (3 valori continui)
# Qui simuliamo valori come combinazioni lineari + rumore
y = np.zeros((1000, 3))
y[:, 0] = X[:, 0] * 50 + X[:, 1] * 20 + np.random.randn(1000) * 0.5 # temperatura
y[:, 1] = X[:, 2] * 5 + X[:, 3] * 10 + np.random.randn(1000) * 0.2 # pressione
y[:, 2] = X[:, 1] * 30 + X[:, 4] * 15 + np.random.randn(1000) * 0.3 # velocità


# --- Definizione modello ---
model = Sequential([
    Dense(30, activation='relu', input_shape=(5,)),
    Dense(30, activation='relu'),
    Dense(30, activation='relu'),
    Dense(3) # 3 output continui, senza attivazione (regressione)
])


# Compilazione modello
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')


# Allenamento modello
history = model.fit(X, y, epochs=50, batch_size=32, validation_split=0.2)


# Prova con nuovi dati
X_new = np.array([[0.2, 0.4, 0.1, 0.3, 0.5]])
y_pred = model.predict(X_new)


print(f"Input: {X_new}")
print(f"Predizioni (Temperatura, Pressione, Velocità): {y_pred}")

