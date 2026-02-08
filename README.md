# Twitch Subs Calculator

Questo script Python analizza il file CSV della lista abbonati di Twitch e genera un report statistico rapido direttamente nel terminale.

## Funzionalità
- **Conteggio Subs**: Calcola il totale di Sub Gift, Prime, e abbonamenti paganti divisi per Tier (1, 2, 3).
- **Lista Veterani**: Identifica ed elenca gli abbonati fedeli da più di 30 mesi, ordinandoli per durata.

## Requisiti
- Python 3.x installato.
- Il file `.csv` degli abbonati scaricato dalla Dashboard Autore di Twitch.

## Istruzioni per l'uso

1. **Scarica il CSV**: Vai sulla dashboard di Twitch e scarica la lista dei tuoi abbonati.
2. **Rinomina il file**: Rinomina il file scaricato esattamente in `subscriber-list.csv` se non si chiama in questo modo.
3. **Posiziona il file**: Metti il file `subscriber-list.csv` nella stessa cartella dove si trova `SubsCalculator.py`.
4. **Esegui lo script**:
   Apri il terminale nella cartella ed esegui:
   ```bash
   python SubsCalculator.py
   ```

## Output
Lo script stamperà a video un riepilogo con i conteggi per ogni tipo di sub e la tabella dei veterani.
