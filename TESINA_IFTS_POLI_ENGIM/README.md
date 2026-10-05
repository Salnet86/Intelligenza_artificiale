

#Autore SALVATORE 
#------------CORSO IFTS ALTA FORMAZIONE EQF 4 
#-------------ORGANIZATO DA ENGIM E POLITECNICO 
# Intelligenza Artificiale e Reti Neurali: Dalle Basi al Deep Learning

Panoramica teorica e pratica sull'Intelligenza Artificiale, il Machine Learning e le Reti Neurali, pensata per l'inserimento in ambito accademico o di progetto (es. tesina).

---

Il Neurone Biologico: Riceve impulsi elettrici dai dendriti, elabora l'informazione nel nucleo e, se viene superata una certa soglia, trasmette il segnale attraverso l'assone.  
Il Perceptron (Neurone Artificiale): Introdotto da 
Frank Rosenblatt nel 1958, è l'unità logica fondamentale. Calcola la somma pesata degli input (z = \sum (w_i \cdot x_i) + b), aggiunge un termine di bias (simile a una tensione di offset in elettronica) e
applica una funzione di attivazione.




## 📋 Indice
1. [Introduzione](#introduzione)
2. [Dalle Basi Biologiche alle Reti Neurali Artificiali](#1-dalle-basi-biologiche-alle-reti-neurali-artificiali)
   - [Il Perceptron e la programmazione in Python](#il-perceptron-in-python-funzione-logica-and)
3. [L'Evoluzione delle Architetture Neurali](#2-levoluzione-delle-architetture-neurali)
4. [Applicazioni Pratiche (NLP e Chatbot)](#3-applicazioni-pratiche-natural-language-processing-nlp-e-chatbot)

---
pip install numpy
pip install tensorflow


## 🧠 Introduzione
L'Intelligenza Artificiale (IA) e il **Machine Learning (ML)** rappresentano il punto d'incontro tra la matematica statistica e l'informatica moderna, consentendo ai sistemi software di apprendere dai dati anziché essere programmati esclusivamente tramite regole rigide (*If-Then*).

---

## 1. Dalle Basi Biologiche alle Reti Neurali Artificiali
Il concetto fondamentale del Deep Learning prende ispirazione dalla struttura del sistema nervoso biologico:
* **Il Neurone Biologico:** Riceve impulsi elettrici dai dendriti, elabora l'informazione nel nucleo e, se viene superata una certa soglia, trasmette il segnale attraverso l'assone.
* **Il Perceptron (Neurone Artificiale):** Introdotto da Frank Rosenblatt nel 1958, è l'unità logica fondamentale. Calcola la **somma pesata degli input** ($z = \sum (w_i \cdot x_i) + b$), aggiunge un termine di **bias** e applica una funzione di attivazione.

### Il Perceptron in Python (Funzione logica AND)
Un singolo neurone può essere addestrato per risolvere problemi di classificazione binaria lineari, come la porta logica AND:

```python
import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.zeros(input_size)
        self.bias = 0
        self.eta = learning_rate

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights) + self.bias
        return 1 if summation > 0 else 0

    def train(self, training_inputs, labels, epochs=10):
        for _ in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                self.weights += self.eta * error * inputs
                self.bias += self.eta * error

# Test con la funzione AND
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
labels = np.array([0, 0, 0, 1])
neuron = Perceptron(input_size=2)
neuron.train(inputs, labels)


2. L'Evoluzione delle Architetture Neurali
Per superare i limiti del singolo neurone (incapace di risolvere la funzione logica non-linearità XOR), le reti si sono evolute in strutture più complesse:
Multi-Layer Perceptron (MLP): Introduce uno o più strati nascosti (hidden layers) tra l'input e l'output, permettendo di apprendere relazioni non lineari complesse grazie all'algoritmo di Backpropagation.
Deep Neural Networks (DNN): Reti caratterizzate da una maggiore profondità, dove ogni strato estrae livelli di astrazione progressivamente superiori (es. bordi \rightarrow forme \rightarrow oggetti completi).
Recurrent Neural Networks (RNN): Progettate per gestire dati sequenziali (come serie temporali, log o testo) grazie a uno stato nascosto che funge da memoria degli input precedenti.
3. Applicazioni Pratiche: Natural Language Processing (NLP) e Chatbot
Un ambito applicativo fondamentale affrontato in laboratorio riguarda l'elaborazione del linguaggio naturale sfruttando la matematica vettoriale e la similarità del coseno:
Vectorization: Le frasi inserite dall'utente e quelle presenti in un dataset vengono convertite in vettori numerici basati sulla frequenza delle parole in un vocabolario comune.
Similarità del Coseno: Si calcola l'angolo geometrico tra il vettore della domanda e quelli del dataset; minore è l'angolo (valore vicino a 1), maggiore è la pertinenza della risposta restituita tramite un'interfaccia web (es. Flask).
