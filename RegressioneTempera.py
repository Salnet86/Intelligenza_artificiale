"""
linear_temp_2003.py


Calcola la regressione lineare sulle temperature medie mensili del 2003 (dati fittizi),
poi:
 - Stampa coefficiente angolare (slope) e intercetta (intercept)
 - Plotta dati e linea di regressione


Requisiti:
    pip install numpy matplotlib scikit-learn
"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# 1. Dati fittizi: temperatura media per mese
temperatura_media_mese_2003 = {
    "Gennaio": 3.5,
    "Febbraio": 5.0,
    "Marzo": 9.0,
    "Aprile": 13.5,
    "Maggio": 18.0,
    "Giugno": 22.0,
    "Luglio": 25.0,
    "Agosto": 24.5,
    "Settembre": 20.0,
    "Ottobre": 14.0,
    "Novembre": 8.5,
    "Dicembre": 4.5
}


# 2. Converto i mesi in numeri 1..12 e creo array di temperature
mesi = np.arange(1, 13).reshape(-1, 1) # array colonna: [[1], [2], ..., [12]]
temp = np.array([temperatura_media_mese_2003[m] for m in temperatura_media_mese_2003])


# 3. Istanzio il modello di regressione lineare
model = LinearRegression()


# 4. Eseguo il fitting del modello (trova slope e intercept)
model.fit(mesi, temp)


# 5. Estraggo coefficiente angolare e intercetta
slope = model.coef_[0] # pendenza della retta
intercept = model.intercept_ # punto di incrocio con asse Y


# 6. Stampo l'equazione della retta
print(f"Equazione della retta: temperatura = {slope:.3f} * mese + {intercept:.3f}")


# 7. Calcolo le temperature previste dalla retta
temp_pred = model.predict(mesi)


# 8. Creo il grafico
plt.figure(figsize=(8, 5))
plt.scatter(mesi, temp, color='blue', label='Temp. osservate') # punti reali
plt.plot(mesi, temp_pred, color='red', linewidth=2, label='Regressione') # linea fit
plt.title("Regressione lineare: temperature medie mensili 2003")
plt.xlabel("Mese (1 = Gennaio, ..., 12 = Dicembre)")
plt.ylabel("Temperatura media (°C)")
plt.legend()
plt.grid(True)
plt.show()

