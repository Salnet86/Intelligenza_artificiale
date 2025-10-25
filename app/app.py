from flask import Flask, render_template, request, jsonify
import json
import math
import os

app = Flask(__name__)

# Percorso al file dataset.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'dataset.json')

# Carico il dataset
with open(DATA_PATH, 'r', encoding='utf-8') as f:
    dataset = json.load(f)

# Costruisco il vocabolario unico
vocabulary = {word for entry in dataset for word in entry['input'].lower().split()}

def vectorize(text):
    """Converte il testo in un vettore basato sul vocabolario"""
    tokens = text.lower().split()
    return [tokens.count(word) for word in vocabulary]

def cosine_similarity(vec1, vec2):
    """Calcola la similarità del coseno tra due vettori"""
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    mag1 = math.sqrt(sum(a * a for a in vec1))
    mag2 = math.sqrt(sum(b * b for b in vec2))
    return dot_product / (mag1 * mag2) if mag1 and mag2 else 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    user_vec = vectorize(user_input)

    best_sim = 0
    best_resp = "Non ho capito, puoi ripetere?"

    # Ciclo per trovare la risposta più simile
    for entry in dataset:
        entry_vec = vectorize(entry['input'])
        sim = cosine_similarity(user_vec, entry_vec)

        if sim > best_sim:
            best_sim = sim
            best_resp = entry['output']

    return jsonify({"response": best_resp})

if __name__ == '__main__':
    app.run(debug=True)
