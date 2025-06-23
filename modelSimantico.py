from flask import Flask, request, jsonify
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Inizializzare l'app Flask
app = Flask(__name__)

# Dataset di domande e risposte (questo è un esempio di dati che puoi estendere)
dataset = [
    {"pattern": "ciao", "response": "Ciao! Come posso aiutarti oggi?"},
    {"pattern": "come ti chiami", "response": "Mi chiamo Doria, l'assistente virtuale di Salvo."},
    {"pattern": "come stai", "response": "Sto bene, grazie! E tu?"},
    {"pattern": "che lavoro fai", "response": "Lavoro come assistente virtuale, rispondendo alle tue domande."},
    {"pattern": "chi sei", "response": "Sono Doria, l'assistente virtuale progettata per aiutarti."}
]

# Creare un vettore delle risposte
patterns = [item["pattern"] for item in dataset]
responses = [item["response"] for item in dataset]

# Creare un oggetto TfidfVectorizer
vectorizer = TfidfVectorizer()

# Creare un dizionario di risposte che sarà utilizzato per calcolare la similarità
vectorizer.fit(patterns)

# Funzione per ottenere la risposta più simile
def get_response(user_input):
    # Trasformare l'input dell'utente in un vettore
    user_input_vec = vectorizer.transform([user_input])
    
    # Calcolare la similarità coseno tra l'input dell'utente e tutti i pattern nel dataset
    similarities = cosine_similarity(user_input_vec, vectorizer.transform(patterns))
    
    # Trova l'indice del pattern più simile
    best_match_index = np.argmax(similarities)
    
    # Restituire la risposta corrispondente al pattern trovato
    return responses[best_match_index] if similarities[0, best_match_index] > 0.5 else "Non ho capito, puoi riformulare?"

# Route per la conversazione con l'assistente
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()  # Ottieni il JSON con la domanda
    user_input = data.get("question", "").strip()  # Estrai la domanda

    if not user_input:
        return jsonify({"response": "Per favore, fammi una domanda."})
    
    response = get_response(user_input)  # Ottieni la risposta
    return jsonify({"response": response})

# Avviare l'app Flask
if __name__ == '__main__':
    app.run(debug=True)
