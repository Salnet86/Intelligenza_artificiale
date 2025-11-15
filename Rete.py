import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Dati finti
X = np.random.rand(100, 1)
y = 3 * X + 2 + np.random.randn(100, 1) * 0.5

# Creazione modello
model = Sequential()
model.add(Dense(10, input_dim=1, activation='relu'))  # hidden layer
model.add(Dense(1))  # output layer per regressione

# Compilazione
model.compile(optimizer='adam', loss='mse')

# Addestramento
model.fit(X, y, epochs=100, verbose=0)

# Predizione
y_pred = model.predict(X)
