import collections
import numpy as np

# A. Dataset di partenza
dataset = {
    'm e l a </w>': 5,
    'm e l o </w>': 3,
    'p e r a </w>': 2
}

def get_stats(data):
    pairs = collections.defaultdict(int)
    for word, freq in data.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pair = (symbols[i], symbols[i+1])
            pairs[pair] += freq
    return pairs

def merge_vocab(pair, data_in):
    data_out = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word in data_in:
        new_word = word.replace(bigram, replacement)
        data_out[new_word] = data_in[word]
    return data_out

# B. Loop di addestramento BPE (Trova il MAX e fonde)
for i in range(10):
    pairs = get_stats(dataset)
    if not pairs: break
    best_pair = max(pairs, key=pairs.get) # Il tuo "Functionmax"
    dataset = merge_vocab(best_pair, dataset)

# C. Creazione Vocabolario ID
tokens_unici = set()
for parola in dataset.keys():
    for t in parola.split():
        tokens_unici.add(t)

token_to_id = {token: i for i, token in enumerate(sorted(list(tokens_unici)))}
print(f"Vocabolario ID: {token_to_id}")
