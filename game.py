import random

def genera_database_casi():
    return {
        "caso_001": {
            "titolo": "Il Furto del Raffaello",
            "info_crimine": {
                "vittima": "Galleria d'Arte Civica",
                "luogo": "Sala del Rinascimento",
                "ora_stimata": "Tra le 02:00 e le 04:00 di notte",
                "descrizione_scena": "Un inestimabile dipinto di Raffaello è stato rimosso dalla cornice. Il vetro della finestra è rotto, ma i frammenti sono sparsi sul marciapiede all'esterno."
            },
            "sospettati": {
                "Marco": {
                    "ruolo": "Custode notturno",
                    "alibi": "Stava facendo la ronda nel lato opposto dell'edificio.",
                    "motivo_apparente": "Ha molti debiti di gioco."
                },
                "Giulia": {
                    "ruolo": "Restauratrice",
                    "alibi": "Era a casa a dormire da sola.",
                    "motivo_apparente": "Voleva sostituire l'originale con una sua copia perfetta per venderlo."
                }
            },
            "prove": {
                "Vetri": {
                    "luogo_ritrovamento": "Marciapiede sotto la finestra",
                    "descrizione": "I frammenti indicano che la finestra è stata colpita dall'interno verso l'esterno, simulando una falsa effrazione."
                },
                "Strumento": {
                    "luogo_ritrovamento": "Nascosto dietro un vaso vicino alla cornice",
                    "descrizione": "Un bisturi di altissima precisione, con minuscole tracce di pittura a olio e tela sul filo della lama."
                }
            },
            "soluzione": {
                "vero_colpevole": "giulia",
                "arma_del_delitto": "bisturi",
                "spiegazione_finale": "Giulia si è nascosta nella galleria dopo la chiusura. Ha usato il suo bisturi da restauro per estrarre la tela senza danneggiarla, poi ha rotto la finestra dall'interno per far credere che i ladri fossero entrati da fuori."
            }
        },
        "caso_002": {
            "titolo": "Il Sabotaggio della Honda CB125R",
            "info_crimine": {
                "vittima": "Pilota amatoriale",
                "luogo": "Paddock del circuito locale",
                "ora_stimata": "Poco prima delle qualifiche",
                "descrizione_scena": "La moto del favorito ha perso i freni alla prima curva. Il pilota è salvo, ma la moto è distrutta."
            },
            "sospettati": {
                "Luca": {
                    "ruolo": "Pilota rivale",
                    "alibi": "Era nel suo box a prepararsi per la gara.",
                    "motivo_apparente": "Voleva assicurarsi la vittoria del campionato."
                },
                "Anna": {
                    "ruolo": "Meccanico",
                    "alibi": "Stava pranzando alla tavola calda del circuito.",
                    "motivo_apparente": "È stata licenziata dal team della vittima la settimana precedente."
                }
            },
            "prove": {
                "Cavo freno": {
                    "luogo_ritrovamento": "Sulla pinza anteriore della moto incidentata",
                    "descrizione": "Il tubo del liquido dei freni non è usurato dal tempo, presenta un taglio netto da recisione."
                },
                "Orma": {
                    "luogo_ritrovamento": "Pozza d'olio vicino al box della vittima",
                    "descrizione": "Un'impronta di uno stivale da corsa con saponette (slider). I meccanici usano scarpe antinfortunistiche, non stivali da pista."
                }
            },
            "soluzione": {
                "vero_colpevole": "luca",
                "arma_del_delitto": "tronchesi",
                "spiegazione_finale": "Luca, già vestito con i suoi stivali da corsa, è entrato di soppiatto nel box rivale e ha usato delle tronchesi per recidere di netto il tubo dei freni, eliminando l'avversario."
            }
        },
        "caso_003": {
            "titolo": "Il Caffè Letale",
            "info_crimine": {
                "vittima": "Amministratore Delegato",
                "luogo": "Ufficio direzionale",
                "ora_stimata": "08:30 del mattino",
                "descrizione_scena": "La vittima è accasciata sulla scrivania. Accanto a lui, una tazzina di caffè mezza vuota."
            },
            "sospettati": {
                "Elena": {
                    "ruolo": "Segretaria",
                    "alibi": "Ha portato il caffè ed è tornata alla sua scrivania fuori dall'ufficio.",
                    "motivo_apparente": "Voleva vendicarsi dei maltrattamenti sul lavoro."
                },
                "Roberto": {
                    "ruolo": "Socio in affari",
                    "alibi": "È arrivato in ufficio alle 08:45, scoprendo il corpo.",
                    "motivo_apparente": "L'azienda stava per essere venduta contro la sua volontà."
                }
            },
            "prove": {
                "Tazzina": {
                    "luogo_ritrovamento": "Sulla scrivania della vittima",
                    "descrizione": "Sul fondo c'è una polvere bianca cristallina che emana un vago sentore di mandorle amare."
                },
                "Contratto": {
                    "luogo_ritrovamento": "Cestino dell'ufficio",
                    "descrizione": "Il contratto di vendita dell'azienda strappato a metà. Su di esso c'è un'impronta digitale fresca appartenente a Roberto."
                }
            },
            "soluzione": {
                "vero_colpevole": "roberto",
                "arma_del_delitto": "veleno",
                "spiegazione_finale": "Roberto è arrivato prima di quanto dichiarato. Ha litigato con la vittima, ha strappato il contratto e, approfittando di una distrazione, ha versato il veleno nel caffè portato dalla segretaria."
            }
        }
    }

def seleziona_caso_casuale(database):
    id_caso = random.choice(list(database.keys()))
    return database[id_caso]

def mostra_menu_investigazione():
    print("\n--- MENU INVESTIGAZIONE ---")
    print("1. Rileggi i dettagli del crimine")
    print("2. Interroga i sospettati e verifica gli alibi")
    print("3. Esamina le prove raccolte")
    print("4. Fai la tua accusa (Risolvi il caso)")
    print("5. Esci dal gioco")
    return input("Scegli un'azione (1-5): ")

def gioca():
    print("Benvenuto nel Database Investigativo!")
    database = genera_database_casi()
    caso_attuale = seleziona_caso_casuale(database)
    print(f"\nÈ stato assegnato un nuovo caso: {caso_attuale['titolo']}")
    risolto = False

    while not risolto:
        scelta = mostra_menu_investigazione()

        if scelta == '1':
            print("\n--- INFORMAZIONI SUL CRIMINE ---")
            for chiave, valore in caso_attuale["info_crimine"].items():
                print(f"{chiave.replace('_', ' ').capitalize()}: {valore}")

        elif scelta == '2':
            print("\n--- SOSPETTATI ---")
            for nome, info in caso_attuale["sospettati"].items():
                print(f"\nSospettato: {nome}")
                for chiave, valore in info.items():
                    print(f" - {chiave.replace('_', ' ').capitalize()}: {valore}")

        elif scelta == '3':
            print("\n--- PROVE ---")
            for nome_prova, info in caso_attuale["prove"].items():
                print(f"\nProva: {nome_prova}")
                for chiave, valore in info.items():
                    print(f" - {chiave.replace('_', ' ').capitalize()}: {valore}")

        elif scelta == '4':
            print("\n--- ACCUSA FINALE ---")
            print("(Usa una sola parola per rispondere, es. il nome esatto o l'oggetto)")
            
            accusa_colpevole = input("Chi è il vero colpevole? ")
            accusa_arma = input("Quale oggetto/arma è stato usato? ")
            
            # Estraiamo le risposte corrette dal database per fare il confronto
            colpevole_reale = caso_attuale["soluzione"]["vero_colpevole"].lower().strip()
            arma_reale = caso_attuale["soluzione"]["arma_del_delitto"].lower().strip()

            # Verifichiamo che ENTRAMBE le deduzioni siano giuste
            if accusa_colpevole.lower().strip() == colpevole_reale and accusa_arma.lower().strip() == arma_reale:
                print("\nCOMPLIMENTI! Hai individuato il colpevole e l'arma del delitto.")
                print(f"Spiegazione ufficiale: {caso_attuale['soluzione']['spiegazione_finale']}")
                risolto = True
            else:
                print("\nSbagliato. Le tue deduzioni su colpevole e/o arma non sono corrette.")
                print("Il capo della polizia ti invita a rivedere attentamente le prove e gli alibi.")

        elif scelta == '5':
            print("Chiusura dell'indagine. Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    gioca()