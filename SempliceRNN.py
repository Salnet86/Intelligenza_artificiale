import math

x = [0.9, 0.6, 0.7, 1, 2]

m = 0.0   # memoria iniziale

Wx = 0.5
Wm = 0.1
bias = 0.05

for t, input_val in enumerate(x):
    print(f"\nTempo {t}")
    print(f"Memoria prima   : {m:.4f}")

    new_m = math.tanh(Wx * input_val + Wm * m + bias)

    print(f"Input           : {input_val}")
    print(f"Memoria attuale : {new_m:.4f}")

    # aggiornamento della memoria
    m = new_m
