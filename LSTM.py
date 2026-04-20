import torch
import torch.nn as nn

class MioModelloLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(MioModelloLSTM, self).__init__()
        
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        # Strato LSTM
        # batch_first=True significa che l'input sarà (batch, seq, feature)
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        
        # Strato lineare di output (classificazione finale)
        self.fc = nn.Linear(hidden_size, output_size)
        
    def forward(self, x):
        # Inizializziamo lo stato nascosto (h0) e di cella (c0) con zeri
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        
        # Passiamo i dati nella LSTM
        out, _ = self.lstm(x, (h0, c0))
        
        # Prendiamo solo l'output dell'ultimo step temporale
        out = self.fc(out[:, -1, :])
        return out

# ESEMPIO DI UTILIZZO
input_size = 10    # Dimensione embedding (es. output del BPE)
hidden_size = 64   # Neuroni nella memoria interna
num_layers = 2     # Quante LSTM sovrapponiamo
output_size = 2    # Numero di classi in uscita

modello = MioModelloLSTM(input_size, hidden_size, num_layers, output_size)

# Input dummy: batch di 5 frasi, ciascuna lunga 10 token, con vettore embedding da 10
dummy_input = torch.randn(5, 10, 10) 
output = modello(dummy_input)

print(f"Output shape: {output.shape}") # Dovrebbe essere [5, 2]
