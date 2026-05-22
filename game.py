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
                    "dialoghi": {
                        "1": {
                            "domanda": "Dov'eri tra le 02:00 e le 04:00?",
                            "risposta": "Stavo facendo la ronda nel lato opposto dell'edificio. È una struttura enorme, non ho sentito rumori di vetri rotti."
                        },
                        "2": {
                            "domanda": "Sappiamo che hai molti debiti di gioco...",
                            "risposta": "(Suda) Non sono affari vostri. E comunque sto ripagando tutto, non ruberei mai un'opera d'arte per questo."
                        }
                    }
                },
                "Giulia": {
                    "ruolo": "Restauratrice",
                    "dialoghi": {
                        "1": {
                            "domanda": "Dov'eri stanotte?",
                            "risposta": "Ero a casa a dormire. Vivo da sola, quindi dovrete fidarvi della mia parola."
                        },
                        "2": {
                            "domanda": "Hai accesso agli attrezzi di restauro?",
                            "risposta": "Certo, è il mio lavoro. Ma tengo sempre la mia cassetta degli attrezzi chiusa a chiave nel magazzino."
                        }
                    }
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
                    "dialoghi": {
                        "1": {
                            "domanda": "Dov'eri poco prima delle qualifiche?",
                            "risposta": "Ero nel mio box a concentrarmi. Mi stavo già preparando per scendere in pista."
                        },
                        "2": {
                            "domanda": "Volevi disperatamente vincere questo campionato, vero?",
                            "risposta": "Voglio vincere pulito in pista, non distruggendo la moto di un avversario ai box!"
                        }
                    }
                },
                "Anna": {
                    "ruolo": "Meccanico licenziato",
                    "dialoghi": {
                        "1": {
                            "domanda": "Sappiamo che sei stata licenziata dalla vittima. Cercavi vendetta?",
                            "risposta": "Ero furiosa, lo ammetto. Ma sabotare una moto significa tentare di uccidere qualcuno. Io sono un meccanico, non un'assassina."
                        },
                        "2": {
                            "domanda": "Dov'eri al momento del sabotaggio?",
                            "risposta": "Ero alla tavola calda del circuito a mangiare un panino."
                        }
                    }
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
                    "dialoghi": {
                        "1": {
                            "domanda": "Hai portato tu il caffè alla vittima?",
                            "risposta": "Sì, come ogni mattina alle 08:30 in punto. Poi sono tornata alla mia scrivania all'ingresso."
                        },
                        "2": {
                            "domanda": "È vero che lui ti maltrattava sul lavoro?",
                            "risposta": "Era un tiranno, non lo nego. Ma avevo già pronta la lettera di dimissioni, non avevo motivo di avvelenarlo."
                        }
                    }
                },
                "Roberto": {
                    "ruolo": "Socio in affari",
                    "dialoghi": {
                        "1": {
                            "domanda": "Quando ha scoperto il corpo?",
                            "risposta": "Sono arrivato alle 08:45 per discutere di un contratto, e l'ho trovato già accasciato."
                        },
                        "2": {
                            "domanda": "Siete in disaccordo sulla vendita dell'azienda?",
                            "risposta": "Quell'idiota stava svendendo il lavoro di una vita. Stavo cercando di fargli cambiare idea."
                        }
                    }
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

def mostra_menu_investigazione(ore_rimaste):
    print(f"\n--- MENU INVESTIGAZIONE [Tempo rimasto: {ore_rimaste} ore] ---")
    print("1. Rileggi i dettagli del crimine (-1 ora)")
    print("2. Vai nella sala interrogatori (Scegli le domande, -1 ora per domanda)")
    print("3. Esamina le prove raccolte (-2 ore)")
    print("4. Fai la tua accusa (Risolvi il caso)")
    print("5. Esci dal gioco")
    return input("Scegli un'azione (1-5): ")

def gioca():
    print("Benvenuto nel Database Investigativo!")
    database = genera_database_casi()
    caso_attuale = seleziona_caso_casuale(database)
    print(f"\nÈ stato assegnato un nuovo caso: {caso_attuale['titolo']}")
    
    ore_rimaste = 14 # Aumentato leggermente il tempo base per bilanciare l'interrogatorio a domande
    risolto = False

    while not risolto:
        if ore_rimaste <= 0:
            print("\n" + "="*55)
            print("TEMPO SCADUTO! Il caso è rimasto irrisolto troppo a lungo.")
            print("Il colpevole ha cancellato le sue tracce ed è fuggito.")
            print("="*55)
            break

        scelta = mostra_menu_investigazione(ore_rimaste)

        if scelta == '1':
            ore_rimaste -= 1
            print("\n--- INFORMAZIONI SUL CRIMINE ---")
            for chiave, valore in caso_attuale["info_crimine"].items():
                print(f"{chiave.replace('_', ' ').capitalize()}: {valore}")

        elif scelta == '2':
            # --- MENU SCELTA SOSPETTATO ---
            in_sala_interrogatori = True
            while in_sala_interrogatori and ore_rimaste > 0:
                print("\n--- SALA INTERROGATORI ---")
                nomi_sospettati = list(caso_attuale["sospettati"].keys())
                
                for i, nome in enumerate(nomi_sospettati):
                    ruolo = caso_attuale['sospettati'][nome]['ruolo']
                    print(f"{i+1}. Interroga {nome} ({ruolo})")
                print("0. Torna al menu principale")
                
                scelta_sos = input("\nChi vuoi far sedere al tavolo? (Scegli il numero): ")
                
                if scelta_sos == '0':
                    in_sala_interrogatori = False
                elif scelta_sos.isdigit() and 1 <= int(scelta_sos) <= len(nomi_sospettati):
                    # --- MENU DOMANDE (ALBERO DI DIALOGO) ---
                    indice_sos = int(scelta_sos) - 1
                    sospettato_attuale = nomi_sospettati[indice_sos]
                    dialoghi = caso_attuale["sospettati"][sospettato_attuale]["dialoghi"]
                    
                    in_interrogatorio = True
                    while in_interrogatorio and ore_rimaste > 0:
                        print(f"\n--- INTERROGANDO: {sospettato_attuale} [Ore rimaste: {ore_rimaste}] ---")
                        for id_domanda, dati in dialoghi.items():
                            print(f"{id_domanda}. Chiedi: \"{dati['domanda']}\" (-1 ora)")
                        print("0. Congeda il sospettato")
                        
                        scelta_domanda = input("\nQuale domanda fai? ")
                        
                        if scelta_domanda == '0':
                            in_interrogatorio = False
                        elif scelta_domanda in dialoghi:
                            ore_rimaste -= 1
                            print(f"\n[{sospettato_attuale}]: \"{dialoghi[scelta_domanda]['risposta']}\"")
                            
                            if ore_rimaste <= 0:
                                print("\nIl tuo tempo a disposizione è terminato nel bel mezzo dell'interrogatorio!")
                                break
                        else:
                            print("\nScelta non valida.")
                else:
                    print("\nInput non valido, riprova.")

        elif scelta == '3':
            ore_rimaste -= 2
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
            
            colpevole_reale = caso_attuale["soluzione"]["vero_colpevole"].lower().strip()
            arma_reale = caso_attuale["soluzione"]["arma_del_delitto"].lower().strip()

            if accusa_colpevole.lower().strip() == colpevole_reale and accusa_arma.lower().strip() == arma_reale:
                print("\n" + "="*55)
                print("COMPLIMENTI! Hai individuato il colpevole e l'arma del delitto.")
                print(f"Spiegazione ufficiale: {caso_attuale['soluzione']['spiegazione_finale']}")
                print(f"Hai risolto il caso con ancora {ore_rimaste} ore di anticipo!")
                print("="*55)
                risolto = True
            else:
                print("\nSbagliato. Le tue deduzioni su colpevole e/o arma non sono corrette.")
                print("L'accusa sbagliata ti ha fatto perdere tempo prezioso per l'interrogatorio delle procedure ufficiali.")
                ore_rimaste -= 3 

        elif scelta == '5':
            print("Chiusura dell'indagine. Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    gioca()