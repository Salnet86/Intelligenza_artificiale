
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense, Concatenate
from tensorflow.keras.models import Model

# --- 1. DATI E PREPARAZIONE ---
# Esempio di frasi grezze
responses = ["ciao come stai", "tutto bene grazie", "buongiorno a te"]
partners = ["salve amico", "come va la vita", "ciao caro"]
labels = np.array([1, 0, 1]) # 0 o 1 (es. positivo/negativo)

# Tokenizer: Serve per convertire parole in numeri
tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(responses + partners)
vocab_size = len(tokenizer.word_index) + 1
max_len = 5

# Trasformazione in sequenze numeriche
res_seq = tokenizer.texts_to_sequences(responses)
part_seq = tokenizer.texts_to_sequences(partners)

# Padding
res_padded = pad_sequences(res_seq, maxlen=max_len, padding='post')
part_padded = pad_sequences(part_seq, maxlen=max_len, padding='post')

# --- 2. MODELLO (Keras Functional API) ---
input_res = Input(shape=(max_len,), name="input_response")
input_part = Input(shape=(max_len,), name="input_partners")

# Embedding (usa vocab_size per gestire tutte le parole note)
emb_res = Embedding(vocab_size, 32)(input_res)
emb_part = Embedding(vocab_size, 32)(input_part)

# RNN
rnn_res = LSTM(32)(emb_res)
rnn_part = LSTM(32)(emb_part)

# Unione
merged = Concatenate()([rnn_res, rnn_part])
output = Dense(1, activation='sigmoid')(merged)

model = Model(inputs=[input_res, input_part], outputs=output)
model.compile(optimizer='adam', loss='binary_crossentropy')

# --- 3. ADDESTRAMENTO ---
model.fit(
    {"input_response": res_padded, "input_partners": part_padded},
    labels,
    epochs=10,
    verbose=0
)
print("Modello addestrato!")

# --- 4. FUNZIONE PER INPUT UTENTE ---
def predici_input(frase_response, frase_partner):
    # Trasforma l'input utente con lo STESSO tokenizer usato per il training
    r_seq = tokenizer.texts_to_sequences([frase_response])
    p_seq = tokenizer.texts_to_sequences([frase_partner])
    
    # Padding
    r_pad = pad_sequences(r_seq, maxlen=max_len, padding='post')
    p_pad = pad_sequences(p_seq, maxlen=max_len, padding='post')
    
    # Predizione
    previsione = model.predict({"input_response": r_pad, "input_partners": p_pad}, verbose=0)
    return previsione[0][0]

# --- ESEMPIO DI UTILIZZO REALE ---
user_res = "ciao come stai"
user_part = "salve amico"

risultato = predici_input(user_res, user_part)
print(f"Probabilità (0-1): {risultato:.4f}")
