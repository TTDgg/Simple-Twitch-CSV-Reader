import csv
import os


def analyze_twitch_subs():
    # Nome del file CSV da analizzare (deve essere nella stessa cartella)
    # Modifica questo nome se il tuo file si chiama diversamente
    file_name = "subscriber-list.csv"
    
    # Ottieni il percorso assoluto del file
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, file_name)
    
    if not os.path.exists(file_path):
        print(f"\n[ERRORE] Il file '{file_name}' non è stato trovato nella cartella: {base_path}")
        print("Assicurati di aver scaricato il file CSV da Twitch e rinominato correttamente in 'subscriber-list.csv'.")
        return

    # Contatori delle sub
    gift_subs = 0
    prime_subs = 0
    tier1_paid = 0
    tier2_subs = 0
    tier3_subs = 0
    # Contatore per veterani
    veterans = []

    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Normalizza i nomi delle colonne (rimuove spazi extra)
            if reader.fieldnames:
                reader.fieldnames = [name.strip() for name in reader.fieldnames]

            for row in reader:
                # Estrazione dati (adatta le chiavi se il CSV ha header diversi)
                username = row.get('Username', 'Unknown')
                # Nel tuo CSV le colonne sono "Current Tier" e "Sub Type"
                current_tier = row.get('Current Tier', '').strip().lower() # es. "tier 1"
                sub_type = row.get('Sub Type', '').strip().lower() # es. "prime", "gift", "recurring"
                
                try:
                    tenure = int(row.get('Tenure', 0))
                except ValueError:
                    tenure = 0

                # Logica di classificazione
                # Priorità: Gift -> Prime -> Tier Paganti
                if sub_type == 'gift':
                    gift_subs += 1
                elif sub_type == 'prime':
                    prime_subs += 1
                else:
                    # Se non è gift o prime, controlliamo il Tier (quindi paganti/recurring)
                    if 'tier 1' in current_tier:
                        tier1_paid += 1
                    elif 'tier 2' in current_tier:
                        tier2_subs += 1
                    elif 'tier 3' in current_tier:
                        tier3_subs += 1
                
                # Controllo per lista veterani (> 30 mesi)
                if tenure > 30:
                    # Determina l'etichetta da mostrare (Prime, T1, T2, T3)
                    display_tier = "T1"
                    if 'tier 2' in current_tier:
                        display_tier = "T2"
                    elif 'tier 3' in current_tier:
                        display_tier = "T3"
                    
                    if sub_type == 'prime':
                        display_tier = "Prime"
                        
                    veterans.append((username, display_tier, tenure))

        # Output del report
        print("\n" + "="*30)
        print(" REPORT SUBS ATTIVE TWITCH")
        print("="*30)
        print(f"Subs Gift (Totale) : {gift_subs}")
        print(f"Subs Prime         : {prime_subs}")
        print(f"Subs Tier 1 (Paid) : {tier1_paid}")
        print(f"Subs Tier 2        : {tier2_subs}")
        print(f"Subs Tier 3        : {tier3_subs}")
        print("-" * 30)
        
        print(f"\nLISTA VETERANI (> 30 Mesi): {len(veterans)}")
        print(f"{'Nome':<25} {'Tier':<10} {'Mesi':<5}")
        print("-" * 45)
        
        # Ordina per mesi (decrescente)
        veterans.sort(key=lambda x: x[2], reverse=True)
        
        for name, tier, months in veterans:
            print(f"{name:<25} {tier:<10} {months:<5}")

    except Exception as e:
        print(f"\n[ERRORE] Si è verificato un problema durante la lettura del file:\n{e}")

if __name__ == "__main__":
    analyze_twitch_subs()
