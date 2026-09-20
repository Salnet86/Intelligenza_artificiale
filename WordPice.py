#Lezione AI WordSpice corsi di ml 

train WordPiece da rivedere
import re
from collections import defaultdict

def train_wordpiece(corpus, vocab_size=50):
    # 1. PRE-TOKENIZZAZIONE IN CARATTERI SINGOLI (con ##)
    # Esempio: "casa" -> ["c", "##a", "##s", "##a"]
    words_counts = defaultdict(int)
    for line in corpus:
        words = line.strip().split()
        for word in words:
            words_counts[word] += 1

    # Mappa le parole in liste di token iniziali
    splits = {}
    for word in words_counts:
        split = [word[0]] + [f"##{char}" for char in word[1:]]
        splits[word] = split

    # 2. VOCABOLARIO INIZIALE (caratteri unici + token speciali)
    vocab = ["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"]
    character_set = set()
    for word in splits:
        for token in splits[word]:
            character_set.add(token)
    vocab.extend(sorted(list(character_set)))

    # 3. LOOP PRINCIPALE DI ADDESTRAMENTO
    while len(vocab) < vocab_size:
        # A. Calcola il conteggio dei singoli token nel corpus corrente
        token_counts = defaultdict(int)
        for word, count in words_counts.items():
            for token in splits[word]:
                token_counts[token] += count

        # B. Trova e conta tutte le coppie adiacenti
        pair_counts = defaultdict(int)
        for word, count in words_counts.items():
            split = splits[word]
            if len(split) < 2:
                continue
            for i in range(len(split) - 1):
                pair = (split[i], split[i + 1])
                pair_counts[pair] += count

        if not pair_counts:
            break # Nessuna coppia rimasta da unire

        # C. Applica la FORMULA DI WORDPIECE per ogni coppia
        pair_scores = {}
        for pair, pair_count in pair_counts.items():
            s_i, s_j = pair
            cnt_i = token_counts[s_i]
            cnt_j = token_counts[s_j]
            
            # Formula: Conteggio_Coppia / (Conteggio_i * Conteggio_j)
            pair_scores[pair] = pair_count / (cnt_i * cnt_j)

        # D. Seleziona la coppia con lo SCORE MASSIMO
        best_pair = max(pair_scores, key=pair_scores.get)
        s_i, s_j = best_pair

        # E. Crea il nuovo token unito
        # Se s_j ha "##", rimuovilo per la fusione (es. "c" + "##a" -> "ca")
        new_token = s_i + (s_j[2:] if s_j.startswith("##") else s_j)
        vocab.append(new_token)

        # F. Aggiorna i token nel corpus (sostituisci la coppia con il nuovo token)
        for word in splits:
            split = splits[word]
            i = 0
            new_split = []
            while i < len(split):
                if i < len(split) - 1 and split[i] == s_i and split[i + 1] == s_j:
                    new_split.append(new_token)
                    i += 2
                else:
                    new_split.append(split[i])
                    i += 1
            splits[word] = new_split

    return vocab

# --- ESEMPIO DI UTILIZZO ---
corpus = [
    "la casa e la macchina",
    "la macchina bella",
    "una bella casa"
]

# Genera il vocabolario fino a 30 token totali
vocabulario_finale = train_wordpiece(corpus, vocab_size=30)

# Salva nel file vocab.txt (un token per riga, come in BERT)
with open("vocab.txt", "w", encoding="utf-8") as f:
    for token in vocabulario_finale:
        f.write(f"{token}\n")

print("Vocabolario generato e salvato in vocab.txt:")
print(vocabulario_finale)
