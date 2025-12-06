import psutil
import time
import pandas as pd
import numpy as np
t=psutil.sensors_temperatures()
df=pd.DataFrame(t)
coretemps = df['coretemp']
# Leggi tutte le temperature
temps = psutil.sensors_temperatures()  # <-- assegniamo a 'temps'

# Estrai la temperatura di Core 0
core0_temp = [x.current for x in temps['coretemp'] if x.label == 'Core 0']

# Converti in array NumPy
core0_array = np.array(core0_temp)

W = np.array([rd.uniform(0, 0.1) for _ in range(1)])
B = np.array([rd.uniform(0, 0.2) for _ in range(1)])
X = np.array([[core0_array.mean()]])
target=np.array([1])
rate=0.7
for epoche in range(10):
    Y = X @ W + B
    error = target - Y
     # Aggiornamento pesi e bias (regola del percettrone)
    W += rate * X.T @ error
    B += rate * error
    print(f"Epoca {epoche+1}, Output: {Y}, Pesi: {W}, Bias: {B}")
    

core0_array = []
for _ in range(50):
    temps = psutil.sensors_temperatures()
    coretemps = temps.get('coretemp', [])
    core0 = [x.current for x in coretemps if x.label == 'Core 0']
    if core0:
        core0_array.append(core0[0])
    time.sleep(0.2)  # piccola pausa per far variare la temperatura



# Simula 50 temperature che variano
core0_array = np.array([50 + np.random.randn() for _ in range(50)])  # media 50°C ± 1
time_array = np.arange(1, len(core0_array)+1)  # asse temporale

# Inizializza percettrone
W = np.array([rd.uniform(0, 0.1)])
B = np.array([rd.uniform(0, 0.2)])
X = core0_array.reshape(-1, 1)
target = np.ones_like(core0_array)
rate = 0.7

# Salva le predizioni per ogni epoca
Y_list = []

for epoca in range(10):
    Y = X @ W + B
    Y_list.append(Y.copy())
    error = target - Y
    W += rate * X.T @ error
    B += rate * error.mean()

# Crea due grafici separati
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# Grafico 1: temperatura simulata
axes[0].plot(time_array, core0_array, color='blue', label='Temperatura Core 0 simulata')
axes[0].set_xlabel('Campione')
axes[0].set_ylabel('Temperatura (°C)')
axes[0].legend()
axes[0].set_title('Temperatura CPU simulata nel tempo')

# Grafico 2: apprendimento percettrone
for i, Y_epoch in enumerate(Y_list):
    axes[1].plot(time_array, Y_epoch, label=f'Epoca {i+1}')
axes[1].plot(time_array, target, 'k--', label='Target')
axes[1].set_xlabel('Campione')
axes[1].set_ylabel('Predizione Percettrone')
axes[1].legend()
axes[1].set_title('Apprendimento Percettrone')

plt.tight_layout()
plt.show()