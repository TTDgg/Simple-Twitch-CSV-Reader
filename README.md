# Twitch Subs Calculator

[English](#english) | [Italiano](#italiano)

<a name="english"></a>
## 🇬🇧 English

This Python script analyzes the Twitch subscriber list CSV file and generates a quick statistical report directly in the terminal.

### Features
- **Subs Count**: Calculates the total of Gift Subs, Prime, and paid subscriptions divided by Tier (1, 2, 3).
- **Veterans List**: Identifies and lists loyal subscribers for more than 30 months, sorting them by duration.

### Requirements
- Python 3.x installed.
- The subscriber `.csv` file downloaded from the Twitch Creator Dashboard.

### Usage Instructions

1. **Download CSV**: Go to the Twitch dashboard and download your subscriber list.
2. **Rename File**: Rename the downloaded file exactly to `subscriber-list.csv` if it is not named this way.
3. **Place File**: Put the `subscriber-list.csv` file in the same folder where `SubsCalculator.py` is located.
4. **Run Script**:
   Open the terminal in the folder and run:
   ```bash
   python SubsCalculator.py
   ```

### Output
The script will print a summary with counts for each sub type and the veterans table to the screen.

---

<a name="italiano"></a>
## 🇮🇹 Italiano

Questo script Python analizza il file CSV della lista abbonati di Twitch e genera un report statistico rapido direttamente nel terminale.

### Funzionalità
- **Conteggio Subs**: Calcola il totale di Sub Gift, Prime, e abbonamenti paganti divisi per Tier (1, 2, 3).
- **Lista Veterani**: Identifica ed elenca gli abbonati fedeli da più di 30 mesi, ordinandoli per durata.

### Requisiti
- Python 3.x installato.
- Il file `.csv` degli abbonati scaricato dalla Dashboard Autore di Twitch.

### Istruzioni per l'uso

1. **Scarica il CSV**: Vai sulla dashboard di Twitch e scarica la lista dei tuoi abbonati.
2. **Rinomina il file**: Rinomina il file scaricato esattamente in `subscriber-list.csv` se non si chiama in questo modo.
3. **Posiziona il file**: Metti il file `subscriber-list.csv` nella stessa cartella dove si trova `SubsCalculator.py`.
4. **Esegui lo script**:
   Apri il terminale nella cartella ed esegui:
   ```bash
   python SubsCalculator.py
   ```

### Output
Lo script stamperà a video un riepilogo con i conteggi per ogni tipo di sub e la tabella dei veterani.
