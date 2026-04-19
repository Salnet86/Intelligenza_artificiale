import numpy as np

# Imposta la dimensione dello spazio latente
latent_dim = 100 
# Numero di campioni (batch size)
batch_size = 32

# Generazione del rumore (distribuzione normale)
noise = np.random.normal(0, 1, (batch_size, latent_dim))
