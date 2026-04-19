import torch
import torch.nn as nn

# Creiamo la stessa matrice 512x64 in una riga sola
# Il metodo .randn crea numeri casuali con media 0 e varianza 1 (Standard Normal)
W_head = torch.randn(512, 64) * 0.1 

print("Matrice inizializzata (Vettorizzata):", W_head.shape)
