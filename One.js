Posta in arrivo
One Hote
// 1. I TUOI DATI IN FORMATO JSON (Stringa)
// Immaginiamo che arrivino così da un database o da un'API
let datiParametriJSON = '{"params": ["casa", "cane", "gatto"]}';

// L'input scritto dall'utente
let inputUtente = "Il mio cane cane corre a casa";

// --- STEP 1: CONVERSIONE JSON E PULIZIA INPUT ---
// Trasformiamo la stringa JSON in un vero oggetto JavaScript
let oggettoDati = JSON.parse(datiParametriJSON);
// Estraiamo l'array dei parametri (i parnes)
let params = oggettoDati.params;

// Trasformiamo l'input dell'utente in un array di parole minuscole
let paroleUtente = inputUtente.toLowerCase().split(" ");


// --- STEP 2: CREAZIONE NUOVO DIZIONARIO ---
let vocabolario = [];

// 1. Inseriamo i parametri estratti dal JSON nel vocabolario
for (let i = 0; i < params.length; i++) {
    vocabolario.push(params[i]);
}

// 2. Confrontiamo e aggiungiamo le parole dell'utente se non esistono già
for (let i = 0; i < paroleUtente.length; i++) {
    let parolaCorrente = paroleUtente[i];
   
    if (!vocabolario.includes(parolaCorrente)) {
        vocabolario.push(parolaCorrente);
    }
}

console.log("Vocabolario finale da JSON + Utente:", vocabolario);


// --- STEP 3: TRASFORMAZIONE IN ONE-HOT ENCODING ---
let vettoreParams = [];
let vettoreUtente = [];

for (let j = 0; j < vocabolario.length; j++) {
    let parolaDizionario = vocabolario[j];

    // Vettore per i parametri del JSON
    if (params.includes(parolaDizionario)) {
        vettoreParams.push(1);
    } else {
        vettoreParams.push(0);
    }

    // Vettore per l'input utente
    if (paroleUtente.includes(parolaDizionario)) {
        vettoreUtente.push(1);
    } else {
        vettoreUtente.push(0);
    }
}

console.log("Vettore Parametri (JSON):", vettoreParams);
console.log("Vettore Utente:           ", vettoreUtente);
