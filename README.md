# Intelligenza_artificiale
Intelligenza Artificiale 




Relazione sul Corso "Addetto alla Logistica Automatica" - Ambito IoT Introduzione Il corso "Addetto alla logistica automatica" si inserisce nel contesto dell'Internet of Things (IoT) e mira a formare professionisti in grado di gestire e ottimizzare processi logistici attraverso l'uso delle tecnologie automatizzate. Questo programma è realizzato in collaborazione con Forit Group, Politecnico Rizzo e Fomatemps, sotto l'agenzia Gi Group.

Obiettivi del Corso Formazione Teorica: Acquisire conoscenze teoriche riguardanti la logistica automatica e l'IoT. Applicazioni Pratiche: Sviluppare competenze pratiche in machine learning e intelligenza artificiale, applicandole a casi reali. Lavoro di Gruppo: Collaborare in team per risolvere problemi complessi e realizzare progetti significativi. Progetti di Machine Learning Durante il corso, abbiamo lavorato su diversi progetti di machine learning. Di seguito sono riportati alcuni esempi:

    Predizione della Domanda Descrizione: Sviluppare un modello per prevedere la domanda di prodotti in base a variabili storiche, come vendite passate e tendenze di mercato. Tecnologie Utilizzate: Python, Scikit-learn, Pandas.
    Ottimizzazione della Catena di Fornitura Descrizione: Implementare un modello di regressione per ottimizzare il livello di inventario in base alla domanda prevista. Tecnologie Utilizzate: Python, NumPy, Matplotlib.
    Classificazione degli Ordini Descrizione: Creare un modello di classificazione per categorizzare gli ordini in base a variabili come la dimensione e il tipo di prodotto. Tecnologie Utilizzate: Python, Scikit-learn. Esercitazioni di Intelligenza Artificiale Abbiamo anche effettuato esercitazioni pratiche sull'intelligenza artificiale, in particolare utilizzando Python. Le attività includevano:

Introduzione a TensorFlow e Keras: Sviluppo di modelli di deep learning per la classificazione delle immagini. Progetti di Natural Language Processing (NLP): Creazione di modelli per l'analisi del sentiment e il riconoscimento di intenti. Lavoro di Gruppo Il lavoro di gruppo è stato fondamentale per il successo del corso. Attraverso la collaborazione con i compagni, abbiamo:

Condiviso Conoscenze: Abbiamo scambiato idee e strategie per affrontare le sfide comuni. Sviluppato Progetti Collaborativi: Abbiamo lavorato insieme su progetti complessi, apprendendo l'importanza della comunicazione e della cooperazione. Prossimi Passi Sviluppo Professionale: Continuare ad approfondire le conoscenze in IoT e intelligenza artificiale. Applicazioni Pratiche: Cercare opportunità di applicazione delle competenze apprese nel mondo reale, contribuendo all'innovazione nel settore della logistica.
Sviluppo di un Programma di Intelligenza Artificiale

Durante il corso per "Addetto alla logistica automatica", ho lavorato su un progetto che prevedeva lo sviluppo di un programma di intelligenza artificiale. Grazie al supporto del docente Rizzo, abbiamo potuto analizzare e riutilizzare programmi già esistenti, concentrandoci sulla loro manutenzione e ottimizzazione. Questa esperienza mi ha permesso di approfondire le mie competenze nell'IA e di comprendere meglio le sfide associate allo sviluppo software.
Assistenza del Docente

Durante il corso, abbiamo ricevuto supporto e guida dal docente Rizzo. La sua esperienza e conoscenza ci hanno aiutato a navigare le complessità del materiale e ad affrontare le sfide associate allo sviluppo di un software complesso.

 

 

Relazione sul Progetto di Analisi dei Prezzi Farmaceutici Introduzione L'obiettivo di questo progetto è stato sviluppare un modello di regressione per prevedere il prezzo dei farmaci basato su diverse caratteristiche, tra cui dosaggio, concorrenza e tipo di farmaco. Utilizzando tecniche di machine learning, abbiamo esplorato e implementato vari modelli, in particolare la regressione polinomiale e il modello Random Forest, al fine di migliorare l'accuratezza delle previsioni.

Dataset Abbiamo utilizzato un dataset simulato con le seguenti caratteristiche:

Dosaggio (mg) Concorrenza (n° competitors) Tipo di Farmaco (1 per generico, 0 per brand) Prezzo ($)

Il dataset conteneva inizialmente alcuni valori mancanti, che sono stati gestiti attraverso tecniche di imputazione.

Fasi del Progetto

    Preprocessing dei Dati Controllo dei Valori Mancanti: Abbiamo verificato la presenza di valori mancanti nel dataset e abbiamo applicato tecniche di imputazione per riempire i valori vuoti. Questo è stato fatto per garantire la qualità e l'integrità dei dati prima dell'analisi.

    Modello di Regressione Polinomiale Creazione del Modello: Abbiamo sviluppato un modello di regressione polinomiale utilizzando la libreria Scikit-learn. Questo modello è stato addestrato sui dati di addestramento e valutato su un test set.

Valutazione del Modello: Le prestazioni del modello sono state misurate utilizzando il Mean Squared Error (MSE) e il coefficiente di determinazione 𝑅 2 R 2 . I risultati iniziali sono stati deludenti, con un MSE di 11584.68 e un 𝑅 2 R 2 di -11.45.

    Modello Random Forest Implementazione del Modello: Successivamente, abbiamo implementato un modello di Random Forest, un algoritmo di ensemble che utilizza un insieme di alberi decisionali per migliorare le previsioni.

Ottimizzazione degli Iperparametri: Abbiamo utilizzato la ricerca a griglia (Grid Search) per ottimizzare gli iperparametri del modello, identificando i migliori parametri:

max_depth: None min_samples_split: 5 n_estimators: 200 Valutazione Finale: Nonostante l'ottimizzazione, il modello ha presentato un MSE di 2770.42 e un 𝑅 2 R 2 di -1.98, indicando che il modello non ha ancora raggiunto prestazioni soddisfacenti.

Risultati e Discussione I risultati ottenuti dai modelli suggeriscono che ci sono opportunità di miglioramento. Le prestazioni scadenti possono essere attribuite a vari fattori, tra cui:

Qualità dei Dati: La presenza di outlier o dati inconsistenti può influenzare negativamente le previsioni. Feature Engineering: È possibile che alcune variabili non siano adeguate o che siano necessarie interazioni più complesse tra le caratteristiche. Scelta del Modello: Altri algoritmi di regressione, come il Gradient Boosting, potrebbero fornire risultati migliori. Conclusioni e Prossimi Passi Il progetto ha fornito un'interessante panoramica sull'uso di tecniche di machine learning per la previsione dei prezzi farmaceutici. Tuttavia, i risultati ottenuti indicano che è necessario un ulteriore lavoro per migliorare le prestazioni del modello.

Raccomandazioni Esplorare Altri Modelli: Considerare l'implementazione di modelli alternativi come il Gradient Boosting o le reti neurali. Analizzare i Dati: Effettuare un'analisi più approfondita per identificare outlier e migliorare la qualità dei dati. Espansione del Dataset: Raccogliere più dati per migliorare la robustezza delle previsioni
abbiamo sviluppato ricerca volti su google co uno script 

 

