import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# ------------------------------
# 1️⃣ Creazione dati di esempio
# ------------------------------

# Feature numeriche (es. 2 variabili continue)
X_numerico = np.random.rand(10, 2)

# Feature categoriali -> one-hot (3 categorie)
X_categorico = np.array([
    [1,0,0],
    [0,1,0],
    [0,0,1],
    [1,0,0],
    [0,1,0],
    [0,0,1],
    [1,0,0],
    [0,1,0],
    [0,0,1],
    [1,0,0]
])

# Concateno feature numeriche + one-hot
X = np.hstack((X_numerico, X_categorico))

# Target categoriale (es. 3 classi)
y = np.array([0, 2, 1, 0, 2, 1, 0, 2, 1, 0])
y_onehot = to_categorical(y)  # trasformo in one-hot per Keras

# ------------------------------
# 2️⃣ Creazione modello
# ------------------------------

model = Sequential()
model.add(Dense(8, input_dim=X.shape[1], activation='relu'))  # layer nascosto
model.add(Dense(3, activation='softmax'))  # output: 3 classi

# ------------------------------
# 3️⃣ Compilazione modello
# ------------------------------

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',  # per output one-hot
    metrics=['accuracy']
)

# ------------------------------
# 4️⃣ Addestramento modello
# ------------------------------

history = model.fit(X, y_onehot, epochs=100, batch_size=2, verbose=1)

# ------------------------------
# 5️⃣ Predizione
# ------------------------------

y_pred = model.predict(X)
print("Predizioni (probabilità per classe):\n", y_pred)

# Se vuoi la classe predetta:
y_pred_classes = np.argmax(y_pred, axis=1)
print("Classe predetta:", y_pred_classes)
