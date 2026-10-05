import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

X = np.array([[[0], [1], [2]], 
              [[1], [2], [3]], 
              [[2], [3], [4]]]) 
y = np.array([3, 4, 5])

model = Sequential([
    SimpleRNN(5, input_shape=(3, 1)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=500, verbose=0)

test_input = np.array([[[3], [4], [5]]])
predizione = model.predict(test_input)
print(f"Predizione del prossimo numero: {predizione[0][0]:.2f}")
