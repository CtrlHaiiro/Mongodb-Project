# Mongodb-Project

# Descrizione

Il programma consente di cercare concerti e artisti musicali
memorizzati in un **database MongoDB**. Gli utenti possono
effettuare ricerche per nome del concerto, nome dell'artista,
posizione geografica e intervallo di date.

### Funzionalità

* **Ricerca per Concerto:**
  Trova concerti in base al nome.
* **Ricerca per Artista:**
  Trova concerti in base all'artista.
* **Ricerca Concerti vicino a te**:
  Trova concerti vicini a una posizione specificata.
* **Ricerca concerti per intervallo di date**:
  Trova concerti che si svolgono in un determinato intervallo di tempo.

## Configurazione:

1. Installare le librerie necessarie nel proprio ambiente virtuale:

   ` pip install -r requirements.txt`

2. eseguire il modulo generatore_di_eventi, che crea un database di concerti in formato json

   `python generatore_di_eventi.py`

3. inserire il file `'database.json'` all'interno di un database MongoDB avviato tramite docker,
   con la seguente connessione : `"mongodb://localhost:27017/"`, rinominando il database **Concerti** e 
la collection a cui appartiene **concerti**
4. eseguire il modulo `Main`

   `   python main.py`
    