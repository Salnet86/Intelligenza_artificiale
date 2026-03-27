Tokenizer libreria
import torch
import torch.nn as nn
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

# ==========================================
# 1. CONFIGURAZIONE E ADDESTRAMENTO BPE
# ==========================================
tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
tokenizer.pre_tokenizer = Whitespace()
trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"], vocab_size=5000)

# Esempio di testo per inizializzare il vocabolario (usa i tuoi file .txt qui)
dati_addestramento = ["Il sistema elettronico trasforma i segnali in bit e byte."]
tokenizer.train_from_iterator(dati_addestramento, trainer)
vocab_size = tokenizer.get_vocab_size()

# ==========================================
# 2. STRUTTURA DELLA RETE (MATRICI Wq, Wk, Wv)
# ==========================================
class MiniTransformer(nn.Module):
    def __init__(self, vocab_size, embed_size=512):
        super(MiniTransformer, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        
        # Le proiezioni lineari che abbiamo visto insieme
        self.Wq = nn.Linear(embed_size, embed_size)
        self.Wk = nn.Linear(embed_size, embed_size)
        self.Wv = nn.Linear(embed_size, embed_size)
        
        self.fc_out = nn.Linear(embed_size, vocab_size)

    def forward(self, x):
        x = self.embedding(x)
        
        # Calcolo dei vettori Q, K, V dalla tua 'x'
        Q = self.Wq(x)
        K = self.Wk(x)
        V = self.Wv(x)
        
        # Qui il Transformer calcolerebbe l'attenzione (Q * K)
        # Per ora passiamo V al layer di uscita
        out = self.fc_out(V)
        return out

# Inizializziamo il modello
modello = MiniTransformer(vocab_size)
modello.eval() # Imposta per l'uso (Inference)

# ==========================================
# 3. INPUT UTENTE E RISPOSTA
# ==========================================
print("--- SISTEMA AVVIATO ---")

# La riga che hai richiesto per l'input
InpuUtebte = input("inserisci il testo: ")

# Trasformazione BPE
tokens = tokenizer.encode(InpuUtebte)
input_tensor = torch.tensor([tokens.ids]) # Crea il tensore x

# Elaborazione della rete
with torch.no_grad():
    output_rete = modello(input_tensor)
    
    # Prendiamo l'ID dell'ultimo token predetto
    ultimo_token_id = torch.argmax(output_rete[0, -1, :]).item()
    
    # Decodifica l'ID in testo leggibile
    parola_risposta = tokenizer.decode([ultimo_token_id])

print(f"\nIl modello ha ricevuto i tuoi token e ha generato: {parola_risposta}")
