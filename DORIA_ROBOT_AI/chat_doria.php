<?php
// --- CONFIG DB ---
$host = "localhost";
$user = "";
$pass = "";
$db = "";

$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) {
    die("Connessione DB fallita: " . $conn->connect_error);
}

// --- API AJAX ---
if (isset($_GET['action'])) {
    header('Content-Type: application/json');
    $action = $_GET['action'];

    if ($action === "get_dataset") {
        $sql = "SELECT intent, pattern, response FROM intents";
        $res = $conn->query($sql);
        $data = [];
        while ($row = $res->fetch_assoc()) {
            $data[] = $row;
        }
        echo json_encode($data);
        exit;
    }

    if ($action === "save_chat" && $_SERVER['REQUEST_METHOD'] === 'POST') {
        $inputJSON = file_get_contents('php://input');
        $data = json_decode($inputJSON, true);
        $domanda = $conn->real_escape_string($data['domanda']);
        $risposta = $conn->real_escape_string($data['risposta']);

        $sql = "INSERT INTO chatlog (domanda, risposta, data) VALUES ('$domanda', '$risposta', NOW())";
        echo json_encode(['status' => $conn->query($sql) ? 'ok' : 'error']);
        exit;
    }
}
?>

<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Chat Doria - Assistente Virtuale</title>
<style>
/* ===== page layout ===== */
:root{
  --primary:#0033cc;
  --bg:#c0ffc0;
  --chat-bg:#f4f4f4;
  --bot-bg:#e0e0e0;
  --user-bg:#0078fe;
}
*{box-sizing:border-box}
body { font-family: Arial, Helvetica, sans-serif; background: var(--bg); color: var(--primary); margin:0; padding:0; height:100vh; display:flex; flex-direction:column; }
header { background:var(--primary); color:white; padding:1rem; text-align:center; position:relative; }
.header-title { font-weight:700; font-size:1.1rem; }
#chat-container { display:flex; flex-direction:column; height:calc(100vh - 72px); max-width:980px; margin:16px auto; width:calc(100% - 32px); border-radius:10px; overflow:hidden; box-shadow:0 12px 40px rgba(0,0,0,.15); background:white; position:relative; }

/* chat area */
#chatlog { height:60vh; overflow-y:auto; padding:1rem; background:var(--chat-bg); border-bottom:1px solid #ccc; display:flex; flex-direction:column; gap:.5rem; }
.message { margin:.2rem 0; padding:.6rem .9rem; border-radius:14px; max-width:75%; line-height:1.3; word-wrap:break-word; box-shadow:0 4px 10px rgba(0,0,0,.04); }
.user { background:var(--user-bg); color:white; align-self:flex-end; margin-left:auto; }
.bot { background:var(--bot-bg); color:var(--primary); align-self:flex-start; margin-right:auto; }
.meta { font-size:0.8rem; opacity:.75; margin-bottom:.25rem; }

/* input */
#input-area { display:flex; gap:8px; padding:12px; background:#fff; align-items:center; border-top:1px solid #eee; }
#input { flex:1; padding:10px 12px; font-size:1rem; border:1px solid #ccc; border-radius:10px; }
#sendBtn { padding:.7rem 1rem; background:var(--primary); color:white; border:none; border-radius:10px; cursor:pointer; font-weight:600; }

/* avatar (fixed in basso a destra) */
#avatar {
    position:fixed;
    bottom:20px;
    right:20px;
    width:300px; /* grandezza richiesta */
    height:auto;
    z-index:9999;
    pointer-events:none; /* non interferisce con click */
    filter: drop-shadow(0 12px 30px rgba(0,0,0,.35));
}

/* SVG scaling */
.talker { width:100%; height:auto; display:block; }

/* mouth states: nascondi tutte le parti di default e mostra in base allo stato */
.mouth [data-part]{ display:none; }
.mouth[data-state="closed"]  [data-part="closed"],
.mouth[data-state="mid"]     [data-part="mid"],
.mouth[data-state="open"]    [data-part="open"],
.mouth[data-state="wide"]    [data-part="wide"] { display:block; }

/* piccoli stili responsivi */
@media (max-width:700px){
  #avatar { width:200px; bottom:12px; right:12px; }
  #chatlog { height:55vh; }
}
</style>
</head>
<body>
<header>
  <div class="header-title">Chat Doria - Assistente Virtuale</div>
</header>

<div id="chat-container">
  <div id="chatlog" aria-live="polite" aria-atomic="false"></div>

  <div id="input-area">
    <input id="input" type="text" placeholder="Scrivi qui..." aria-label="Scrivi qui">
    <button id="sendBtn" aria-label="Invia">Invia</button>
  </div>
</div>

<!-- AVATAR DONNA (dettagliato) -->
<div id="avatar" aria-hidden="false" title="Avatar Doria">
  <svg class="talker" viewBox="0 0 500 500" role="img" aria-label="Avatar donna parlante">
    <defs>
      <clipPath id="faceClip">
        <circle cx="250" cy="210" r="120" />
      </clipPath>
    </defs>

    <!-- capelli di fondo -->
    <g class="hair-back">
      <path fill="#2f2a36" d="M110,180 C110,70 200,50 250,50 C300,50 390,70 390,180 C430,220 430,340 360,380 C340,430 300,460 250,460 C200,460 160,430 140,380 C70,340 70,220 110,180 Z"/>
    </g>

    <!-- testa + collo -->
    <g class="head" transform="translate(0,0)">
      <!-- collo -->
      <rect x="220" y="300" width="60" height="60" fill="#e6b79a" rx="16"/>

      <!-- viso -->
      <g clip-path="url(#faceClip)">
        <circle cx="250" cy="210" r="120" fill="#f6d0b1"/>

        <!-- guance -->
        <circle cx="200" cy="230" r="18" fill="#f2b0a9" opacity=".35"/>
        <circle cx="300" cy="230" r="18" fill="#f2b0a9" opacity=".35"/>

        <!-- occhi -->
        <g class="eyes">
          <ellipse cx="205" cy="200" rx="16" ry="12" fill="#ffffff"/>
          <ellipse cx="295" cy="200" rx="16" ry="12" fill="#ffffff"/>
          <circle cx="205" cy="202" r="5" fill="#1f2937"/>
          <circle cx="295" cy="202" r="5" fill="#1f2937"/>

          <!-- palpebre per blink -->
          <rect class="blink-upper" x="189" y="187" width="32" height="6" rx="3" fill="#f6d0b1"/>
          <rect class="blink-upper" x="279" y="187" width="32" height="6" rx="3" fill="#f6d0b1"/>
          <rect class="blink-lower" x="189" y="206" width="32" height="6" rx="3" fill="#f6d0b1"/>
          <rect class="blink-lower" x="279" y="206" width="32" height="6" rx="3" fill="#f6d0b1"/>
        </g>

        <!-- naso -->
        <path d="M248 205 q4 12 -6 22" stroke="#d89f88" stroke-width="4" fill="none" stroke-linecap="round"/>

        <!-- bocca (multipli stati) -->
        <g class="mouth" data-state="closed" transform="">
          <!-- CHIUSA -->
          <g data-part="closed">
            <path d="M210 260 q40 16 80 0" stroke="#c03952" stroke-width="5" fill="none" stroke-linecap="round"/>
          </g>

          <!-- MEZZA APERTA -->
          <g data-part="mid">
            <path d="M210 258 q40 26 80 0" fill="#c03952"/>
            <ellipse cx="250" cy="262" rx="32" ry="10" fill="#61182a"/>
            <ellipse cx="250" cy="266" rx="26" ry="5" fill="#a92c46"/>
          </g>

          <!-- APERTA -->
          <g data-part="open">
            <path d="M205 252 q45 40 90 0 q-45 30 -90 0" fill="#c03952"/>
            <ellipse cx="250" cy="270" rx="34" ry="16" fill="#61182a"/>
            <rect x="223" y="262" width="54" height="8" rx="4" fill="#f5f5f5"/>
            <rect x="223" y="270" width="54" height="14" rx="6" fill="#b11f39"/>
          </g>

          <!-- LARGA -->
          <g data-part="wide">
            <path d="M195 252 q55 26 110 0 q-55 14 -110 0" fill="#c03952"/>
            <ellipse cx="250" cy="260" rx="44" ry="12" fill="#61182a"/>
          </g>
        </g>
      </g>

      <!-- capelli frontali -->
      <g class="hair-front">
        <path fill="#2f2a36" d="M140,180 C150,110 200,80 250,80 C300,80 350,110 360,180 C320,150 180,150 140,180 Z"/>
        <path fill="#2f2a36" d="M125,180 C120,260 170,300 200,320 C175,280 160,240 170,210 Z"/>
        <path fill="#2f2a36" d="M375,180 C380,260 330,300 300,320 C325,280 340,240 330,210 Z"/>
      </g>
    </g>
  </svg>
</div>

<script>
// ====== Rete neurale semplice (client-side) ======
let hiddenSize = 10;
let learningRate = 0.1;
let W1 = Array.from({length:hiddenSize}, ()=>Math.random()*2-1);
let b1 = Array.from({length:hiddenSize}, ()=>Math.random()*2-1);
let W2 = Array.from({length:hiddenSize}, ()=>Math.random()*2-1);
let b2 = Math.random()*2-1;

function sigmoid(x){ return 1/(1+Math.exp(-x)); }
function sigmoidDeriv(x){ return x*(1-x); }

function forward(x){
    let h = W1.map((w,i)=>sigmoid(x*W1[i]+b1[i]));
    let y = sigmoid(h.reduce((sum,val,i)=>sum+val*W2[i],0) + b2);
    return {h, y};
}

function train(x, target){
    let {h, y} = forward(x);
    let error = target - y;
    let dY = error * sigmoidDeriv(y);
    for(let i=0;i<hiddenSize;i++){
        W2[i] += learningRate * dY * h[i];
        let dH = dY*W2[i]*sigmoidDeriv(h[i]);
        W1[i] += learningRate * dH * x;
        b1[i] += learningRate * dH;
    }
    b2 += learningRate * dY;
}

// ====== dataset + inizializzazione ======
let dataset = [];
async function caricaDataset(){
  try{
    const res = await fetch('?action=get_dataset');
    dataset = await res.json();
    // training veloce di esempio
    dataset.forEach(d=>{
      let x = d.pattern.length/100;
      let target = d.pattern.toLowerCase().includes("ciao") ? 1 : 0;
      for(let epoch=0; epoch<50; epoch++){
        train(x, target);
      }
    });
    scriviMessaggio('bot', 'Piacere, sono Doria! In che cosa posso essere utile?');
  }catch(e){
    console.error('Errore caricamento dataset', e);
    scriviMessaggio('bot', 'Piacere, sono Doria! (dataset non caricato)');
  }
}

// ====== utilità testo->numero ======
function textToNumber(text){
  return text.split('').reduce((sum,ch)=>sum+ch.charCodeAt(0),0)/100;
}

// ====== Avatar bocca ======
const mouth = document.querySelector('.mouth');

function setMouth(state){
  if(!mouth) return;
  mouth.setAttribute('data-state', state);
}

// fallback blink occhi (solo estetico)
(function blinkLoop(){
  const uppers = document.querySelectorAll('.blink-upper, .blink-lower');
  if(!uppers.length) return;
  setInterval(()=>{
    uppers.forEach(r=> r.style.transform = 'scaleY(.05)');
    setTimeout(()=> uppers.forEach(r=> r.style.transform = ''), 150);
  }, 4500);
})();

// ====== sintesi vocale con sincronizzazione bocca ======
const synth = window.speechSynthesis;
let voices = [];
function populateVoices(){
  voices = synth.getVoices();
}
if('speechSynthesis' in window){
  populateVoices();
  speechSynthesis.onvoiceschanged = populateVoices;
}

// heuristica di mapping parola->visema
function mouthForWord(word){
  const w = (word||'').toLowerCase();
  if(/[aeiouàèéìòóù]/i.test(w) && w.length > 2){
    if(/[aouàòó]/i.test(w)) return 'wide';
    if(/[eiìéì]/i.test(w)) return 'mid';
    return 'open';
  }
  // consonanti brevi
  return 'open';
}

let fallbackInterval = null;
function startFallbackMouth(){
  clearInterval(fallbackInterval);
  let states = ['mid','open','wide','mid','closed'];
  let i = 0;
  fallbackInterval = setInterval(()=>{
    setMouth(states[i % states.length]);
    i++;
  }, 120);
}
function stopFallbackMouth(){
  clearInterval(fallbackInterval);
  fallbackInterval = null;
  setMouth('closed');
}

function parlaTesto(testo){
  if(!testo) return;
  if(!('speechSynthesis' in window)){
    // nessuna API, solo fallback animazione per un tempo stimato
    startFallbackMouth();
    const ms = Math.min(15000, Math.max(800, testo.length * 70));
    setTimeout(()=> stopFallbackMouth(), ms);
    return;
  }

  const utter = new SpeechSynthesisUtterance(testo);
  // seleziona voce italiana se possibile
  const v = voices.find(v => /it/i.test(v.lang)) || voices.find(v => /italian/i.test(v.name)) || voices[0];
  if(v) utter.voice = v;
  utter.lang = utter.voice?.lang || 'it-IT';
  utter.rate = 1;
  utter.pitch = 1;

  utter.onstart = () => {
    // prova fallback iniziale leggera
    startFallbackMouth();
  };

  // se il browser fornisce onboundary, usalo per sincronizzare parola per parola
  if ('onboundary' in SpeechSynthesisUtterance.prototype || true) {
    // non tutti i browser chiamano onboundary; gestiamo comunque
    utter.onboundary = (ev) => {
      if(ev.name === 'word' || typeof ev.charIndex === 'number'){
        // calcola parola corrente
        const idx = ev.charIndex || 0;
        const upto = testo.slice(0, idx + (ev.charLength || 0));
        const parts = upto.split(/\s+/);
        const current = parts[parts.length-1] || '';
        const state = mouthForWord(current);
        setMouth(state);
      }
    };
  }

  utter.onend = () => {
    stopFallbackMouth();
  };
  utter.onerror = () => {
    stopFallbackMouth();
  };

  // speak
  try{
    speechSynthesis.cancel(); // cancella precedente
    speechSynthesis.speak(utter);
  }catch(e){
    // fallback se speak fallisce
    startFallbackMouth();
    setTimeout(()=> stopFallbackMouth(), Math.min(12000, testo.length*60));
  }
}

// ====== UI: scrivi messaggio nella chat ======
function scriviMessaggio(tipo, testo){
  const log = document.getElementById('chatlog');
  const div = document.createElement('div');
  div.className = 'message ' + tipo;
  if(tipo === 'bot'){
    // permetti HTML limitato? qui inseriamo solo testo semplice (escape)
    div.textContent = testo;
    // fai parlare l'avatar
    parlaTesto(testo);
  } else {
    div.textContent = testo;
  }
  log.appendChild(div);
  log.scrollTop = log.scrollHeight;
}

// ====== risposta: prima dataset, poi fallback rete neurale ======
async function generaRisposta(input){
  // ricerca semplice nel dataset (pattern contain)
  let risposta = dataset.find(d => input.toLowerCase().includes(d.pattern.toLowerCase()));
  if(risposta) return risposta.response;

  // fallback rete neurale
  let x = textToNumber(input);
  let {y} = forward(x);
  return y > 0.5 ? "Ciao!" : "Mi spiace, non ho una risposta precisa. 🤖";
}

// ====== invio domanda, salvataggio ======
async function inviaDomanda(){
  const inputEl = document.getElementById('input');
  const domanda = inputEl.value.trim();
  if(!domanda) return;
  scriviMessaggio('user', domanda);
  inputEl.value = '';
  const risposta = await generaRisposta(domanda);
  scriviMessaggio('bot', risposta);

  // salva chat sul server
  try{
    await fetch('?action=save_chat', {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({domanda, risposta})
    });
  }catch(e){
    console.warn('save_chat failed', e);
  }
}

// utility per mappare testo->numero per la rete
function textToNumber(text){
  return text.split('').reduce((sum,ch)=>sum+ch.charCodeAt(0),0)/100;
}

// ====== eventi UI ======
document.getElementById('sendBtn').addEventListener('click', inviaDomanda);
document.getElementById('input').addEventListener('keydown', e => { if(e.key==='Enter') inviaDomanda(); });

// carica dataset al caricamento della pagina
window.addEventListener('load', caricaDataset);
</script>
</body>
</html>
