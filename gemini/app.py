from flask import Flask, request, jsonify, render_template_string
import google.generativeai as genai
import os

app = Flask(__name__)

# Imposta la chiave API
genai.configure(api_key=os.getenv("GEMINI_API_KEY", "INSERISCI_LA_TUA_KEY"))

# Template HTML + JS + CSS
html = """
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <title>🤖 Gemini Chat con Flask</title>
  <style>
    body {
      font-family: 'Consolas', monospace;
      background: radial-gradient(circle at 30% 20%, #0a0f12 0%, #000000 100%);
      color: #e0e0e0;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      height: 100vh; margin: 0;
    }
    #chat {
      background: #0d1117;
      width: 90%; max-width: 600px;
      height: 400px;
      border: 1px solid #00ffc855;
      border-radius: 10px;
      padding: 10px; overflow-y: auto;
      box-shadow: 0 0 15px #00ffc830 inset;
    }
    .msg { margin: 10px; padding: 8px; border-radius: 8px; max-width: 75%; }
    .user { background: #003366; color: #aaddff; margin-left: auto; }
    .bot { background: #003321; color: #aaffcc; margin-right: auto; }
    textarea { width: 90%; max-width: 600px; height: 60px;
      margin-top: 10px; border-radius: 8px; border: 1px solid #00ffc870;
      background: #0d1117; color: #00ffc8; padding: 8px; resize: none; }
    button {
      margin-top: 8px; padding: 10px 20px; border: none;
      background: linear-gradient(135deg,#00ffc8,#009970);
      border-radius: 8px; color: #000; font-weight: bold;
      cursor: pointer; transition: 0.2s;
    }
    button:hover { box-shadow: 0 0 20px #00ffc8; transform: scale(1.05); }
  </style>
</head>
<body>
  <h2>🤖 Gemini Chat (Flask)</h2>
  <div id="chat"></div>
  <textarea id="prompt" placeholder="Scrivi un messaggio..."></textarea>
  <button id="btnSend">Invia</button>

  <script>
    const chat = document.getElementById('chat');
    const btn = document.getElementById('btnSend');
    const promptArea = document.getElementById('prompt');

    function appendMsg(text, who) {
      const div = document.createElement('div');
      div.className = 'msg ' + who;
      div.innerHTML = '<b>' + (who==='user'?'Tu':'Gemini') + ':</b> ' + text;
      chat.appendChild(div);
      chat.scrollTop = chat.scrollHeight;
    }

    btn.onclick = async () => {
      const text = promptArea.value.trim();
      if (!text) return;
      appendMsg(text, 'user');
      promptArea.value = '';
      appendMsg('<i>Sto pensando...</i>', 'bot');
      const res = await fetch('/ask', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({prompt: text})
      });
      const data = await res.json();
      chat.lastChild.innerHTML = '<b>Gemini:</b> ' + (data.reply || 'Errore.');
    };
  </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html)

@app.route('/ask', methods=['POST'])
def ask():
    try:
        prompt = request.json.get('prompt', '')
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
