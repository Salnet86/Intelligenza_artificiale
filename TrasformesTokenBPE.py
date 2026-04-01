import collections

# 1. Prepariamo i dati (Dataset di esempio)
dataset = {
    'm e l a </w>': 5,
    'm e l o </w>': 3,
    'p e r a </w>': 2
}

def get_stats(data):
    # Conta le frequenze delle coppie (let stat = {})
    pairs = collections.defaultdict(int)
    for word, freq in data.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pair = (symbols[i], symbols[i+1])
            pairs[pair] += freq
    return pairs

def merge_vocab(pair, data_in):
    # Fonchi i caratteri (Functionmax e sostituzione)
    data_out = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word in data_in:
        new_word = word.replace(bigram, replacement)
        data_out[new_word] = data_in[word]
    return data_out

# Loop di addestramento (es. per 10 iterazioni invece di 50.000 per brevità)
for i in range(10):
    pairs = get_stats(dataset)
    if not pairs:
        break
    # Trova il massimo (Functionmax)
    best_pair = max(pairs, key=pairs.get)
    dataset = merge_vocab(best_pair, dataset)
    print(f"Iterazione {i+1}: Fusa la coppia {best_pair}")
  
