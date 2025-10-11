

# 🤖 Gemini Chat – Versione Browser e Flask 
#TECNICHE E TECNOLOGIE AI CORSO DI FORMAZIONE SULLA INTELIGENZA ARIFICIALE 
#progetto fatto in aula api javascript e python come interagire con chat gpt scrivere i prompt per generare il codice e strare 


Questo progetto permette di creare una **chat con Gemini AI** sia in **JavaScript puro (browser)** sia in **Python Flask (server)**.  
È un esempio completo per capire come integrare i modelli **Gemini 2.5 Flash** di Google in applicazioni web.

---

## 🔹 Funzionalità

- Chat AI con **interfaccia web moderna** (dark/futuristica).  
- Due modalità:
  1. **JavaScript puro**: funziona direttamente nel browser usando i moduli ES6.  
  2. **Python Flask**: chiave API protetta lato server, risposta Gemini in JSON.  
- Design responsivo, con messaggi utente e bot separati.  
- Possibilità di invio con **Invio ↵** e feedback “Sto pensando...”.  

---

## 📦 Requisiti

### 1️⃣ Browser JavaScript

- Browser moderno con supporto a **ES6 modules** (Chrome, Firefox, Edge, Safari).  
- **Chiave API Google Gemini** per testare localmente:
  - Inserire la chiave nel modulo JS (non sicuro per produzione).  
    

### 2️⃣ Python Flask

- Python 3.9+  
- Librerie Python:
```bash
pip install flask google-generativeai


### export GEMINI_API_KEY="LA_TUA_CHIAVE"


📂 gemini-chat
 ├── gemini.html         # Versione browser JS puro
 ├── app.py              # Server Flask
 └── README.md           # Documentazione



Come funziona
JavaScript puro

Utente scrive un messaggio.

JS invia il messaggio al modulo Gemini direttamente.

Gemini risponde → JS aggiorna la chat.

Python Flask

Utente scrive un messaggio → browser invia POST a /ask.

Flask legge il messaggio e lo invia a Gemini (server).

Riceve risposta → invia JSON al browser.

JS aggiorna la chat.

⚠️ Sicurezza

JS puro → chiave visibile nel browser → solo test locali.

Flask → chiave sicura lato server.

Mai pubblicare chiavi API nel codice pubblico.

🎨 Personalizzazioni

Cambiare modello Gemini (gemini-2.5-flash, gemini-pro, ecc.).

Cambiare colori e layout CSS per tema personalizzato.

Salvare cronologia chat in JSON o database.

Aggiungere TTS (Text-to-Speech) o comandi vocali.

🛠 Licenza

MIT – puoi modificare e usare liberamente per progetti personali o commerciali.

👨‍💻 Autore

SalvoNet
Tecnico informatico ed elettronico • Appassionato di AI e machine learning

💬 “L’intelligenza artificiale amplifica la mente umana, non la sostituisce.”










Struttura generale

Questo script è un'applicazione Flask (Python) che:

Crea un piccolo server web locale.

Espone una pagina web con HTML + CSS + JS (la chat).

Riceve messaggi dall’utente via /ask.

Chiama Gemini AI usando la libreria google-generativeai.

Invia la risposta AI al browser in formato JSON.

🔍 Spiegazione riga per riga
📦 Import dei moduli
from flask import Flask, request, jsonify, render_template_string
import google.generativeai as genai
import os


Flask → framework web Python per creare server leggeri.

request → serve per leggere i dati inviati dal browser (es. messaggi utente).

jsonify → converte un dizionario Python in formato JSON (che JavaScript capisce).

render_template_string → genera HTML direttamente da una stringa Python.

google.generativeai → SDK ufficiale di Google per accedere al modello Gemini.

os → serve per leggere variabili d’ambiente (es. chiave API).

⚙️ Inizializzazione di Flask
app = Flask(__name__)


Crea l’app Flask.
__name__ serve a dire a Flask dove si trova il file principale.

🔑 Configurazione della chiave API
genai.configure(api_key=os.getenv("GEMINI_API_KEY", "INSERISCI_LA_TUA_KEY"))


os.getenv() cerca una variabile d’ambiente chiamata GEMINI_API_KEY.
Se non la trova, usa "INSERISCI_LA_TUA_KEY".

Questa chiave serve per autenticarsi con i server di Gemini.

È importante non scriverla in chiaro nel codice, ma metterla come variabile d’ambiente.

🖥️ HTML, CSS e JavaScript

Tutto il contenuto della pagina web è incluso nella stringa html = """ ... """.

In pratica, Flask invia questo codice al browser quando l’utente apre la pagina.
Vediamo i punti chiave:

🔸 Stile CSS
body { background: radial-gradient(...); }
#chat { background: #0d1117; ... }
.user { background: #003366; }
.bot  { background: #003321; }


→ imposta un tema dark futuristico con colori ciano/verdi, box rotondi e ombre.

🔸 JavaScript (gestione chat)
const chat = document.getElementById('chat');
const btn = document.getElementById('btnSend');
const promptArea = document.getElementById('prompt');


Queste righe collegano le variabili JS agli elementi HTML.

Funzione appendMsg()
function appendMsg(text, who) {
  const div = document.createElement('div');
  div.className = 'msg ' + who;
  div.innerHTML = '<b>' + (who==='user'?'Tu':'Gemini') + ':</b> ' + text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}


Serve per aggiungere messaggi alla chat:

Se who='user', mostra "Tu:"

Se who='bot', mostra "Gemini:"

Aggiorna l’interfaccia dinamicamente (senza ricaricare la pagina).

Invio messaggio
btn.onclick = async () => {
  const text = promptArea.value.trim();
  if (!text) return;
  appendMsg(text, 'user');
  promptArea.value = '';
  appendMsg('<i>Sto pensando...</i>', 'bot');


Quando premi “Invia”:

Legge il testo scritto.

Lo mostra subito nella chat.

Aggiunge una riga temporanea “Sto pensando...”.

Chiamata al server Flask
const res = await fetch('/ask', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({prompt: text})
});
const data = await res.json();
chat.lastChild.innerHTML = '<b>Gemini:</b> ' + (data.reply || 'Errore.');


👉 Invoca l’endpoint /ask del server Flask inviando il testo come JSON.
Poi riceve la risposta data.reply e la scrive nella chat.

🧩 Flask – Route principale /
@app.route('/')
def index():
    return render_template_string(html)


Quando apri http://127.0.0.1:5000/, Flask mostra la pagina HTML definita prima.
(Niente file separati: il codice HTML è incluso nello script stesso).

🧠 Endpoint /ask – dove avviene l’AI
@app.route('/ask', methods=['POST'])
def ask():
    try:
        prompt = request.json.get('prompt', '')
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


🔹 Spiegazione:

prompt = request.json.get('prompt', '')
→ Legge il testo inviato dal browser.

model = genai.GenerativeModel("gemini-2.5-flash")
→ Carica il modello AI di Google.

response = model.generate_content(prompt)
→ Invia il testo a Gemini e riceve la risposta.

jsonify({'reply': response.text})
→ Invia al browser un oggetto JSON con la risposta del modello.

▶️ Avvio dell’app Flask
if __name__ == '__main__':
    app.run(debug=True)


Quando esegui python app.py, Flask:

Avvia un mini-server locale.

Mostra nel terminale l’indirizzo (es. http://127.0.0.1:5000).

debug=True mostra errori in tempo reale, utile durante lo sviluppo.

💬 In breve
Parte	Cosa fa
Flask	Gestisce il server e comunica con Gemini
HTML/CSS	Mostra la chat e lo stile grafico
JavaScript	Invia e riceve messaggi in tempo reale
Google Generative AI	Genera il testo di risposta



---



