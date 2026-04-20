from tokenizers import PreTrainedTokenizerFast

# Carichiamo il tokenizer che abbiamo addestrato
try:
    tokenizer = PreTrainedTokenizerFast.from_pretrained("mio_tokenizer_bpe")
except Exception as e:
    print("Errore: Assicurati di aver salvato il tokenizer nella cartella 'mio_tokenizer_bpe'.")
    exit()

print("--- BPE Interactive Mode ---")
print("Scrivi 'esci' per terminare.\n")

while True:
    # Qui usiamo la funzione richiesta
    testo = input("Inserisci il testo da tokenizzare: ")
    
    if testo.lower() == 'esci':
        print("Uscita dal programma.")
        break
    
    # 1. Encoding
    encoded = tokenizer.encode(testo)
    
    # 2. Mostriamo i risultati
    print(f"\n> Token IDs (Numeri): {encoded}")
    
    # Vediamo esattamente quali sub-words ha creato
    tokens = tokenizer.convert_ids_to_tokens(encoded)
    print(f"> Tokens (Sub-words): {tokens}")
    
    # 3. Decoding (Verifica)
    decoded = tokenizer.decode(encoded)
    print(f"> Decodificato: '{decoded}'")
    print("-" * 30)
