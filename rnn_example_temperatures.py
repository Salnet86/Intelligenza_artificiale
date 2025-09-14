# Docente: Alessandra  
# Lezioni di Informatica — AI — Rete RNN

import numpy as np

# Dati di input (temperature normalizzate /100)
x = np.array([0.20, 0.30, 0.80, 0.12])
target = x.copy()  # target = input (autoassociatore per semplicità)

# Parametri iniziali
W_xh = 0.5
W_hh = 0.1
W_hy = 0.7
b_h = 0.0
b_y = 0.0

eta = 0.1  # learning rate

# Funzioni di attivazione
def tanh(z):
    return np.tanh(z)

def dtanh(z):
    return 1 - np.tanh(z)**2

# Forward pass
h = []
net_h = []
y = []
net_y = []
h_prev = 0.0
for t in range(len(x)):
    net_h_t = W_xh * x[t] + W_hh * h_prev + b_h
    h_t = tanh(net_h_t)
    net_y_t = W_hy * h_t + b_y
    y_t = net_y_t  # output lineare

    net_h.append(net_h_t)
    h.append(h_t)
    net_y.append(net_y_t)
    y.append(y_t)

    h_prev = h_t

print("Forward pass:")
for t in range(len(x)):
    print(f"t={t+1}, x={x[t]:.2f}, h={h[t]:.6f}, y={y[t]:.6f}")

# Calcolo errori output
delta_out = [y[t] - target[t] for t in range(len(x))]
print("\nDelta output:")
print(delta_out)

# Backpropagation through time (BPTT)
delta_h = [0]*len(x)
next_delta = 0
for t in reversed(range(len(x))):
    term_out = delta_out[t] * W_hy
    term_next = next_delta * W_hh
    delta_h[t] = dtanh(net_h[t]) * (term_out + term_next)
    next_delta = delta_h[t]

print("\nDelta hidden:")
print(delta_h)

# Gradienti
dW_hy = sum(delta_out[t] * h[t] for t in range(len(x)))
dW_xh = sum(delta_h[t] * x[t] for t in range(len(x)))
dW_hh = sum(delta_h[t] * (h[t-1] if t>0 else 0) for t in range(len(x)))

db_y = sum(delta_out)
db_h = sum(delta_h)

print("\nGradienti:")
print(f"dW_hy={dW_hy}, dW_xh={dW_xh}, dW_hh={dW_hh}")
print(f"db_y={db_y}, db_h={db_h}")

# Aggiornamento pesi
W_hy -= eta * dW_hy
W_xh -= eta * dW_xh
W_hh -= eta * dW_hh
b_y -= eta * db_y
b_h -= eta * db_h

print("\nPesi aggiornati:")
print(f"W_xh={W_xh}, W_hh={W_hh}, W_hy={W_hy}")
print(f"b_h={b_h}, b_y={b_y}")
