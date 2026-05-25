import random

# --- CLASSE PER I COLORI E STILI (Codici ANSI) ---
class Stile:
    RESET = '\033[0m'
    GRASSETTO = '\033[1m'
    ROSSO = '\033[91m'
    VERDE = '\033[92m'
    GIALLO = '\033[93m'
    BLU = '\033[94m'
    VIOLA = '\033[95m'
    CIANO = '\033[96m'
   
# --- FUNZIONI DI SUPPORTO PER L'INTERFACCIA ---
def stampa_titolo(testo):
    print(f"\n{Stile.CIANO}{Stile.GRASSETTO}{'='*60}")
    print(f"{testo.center(60)}")
    print(f"{'='*60}{Stile.RESET}")

def stampa_sottotitolo(testo):
    print(f"\n{Stile.BLU}{Stile.GRASSETTO}--- {testo} ---{Stile.RESET}")

def stampa_errore(testo):
    print(f"\n{Stile.ROSSO}{Stile.GRASSETTO}[!] {testo}{Stile.RESET}")

def stampa_successo(testo):
    print(f"\n{Stile.VERDE}{Stile.GRASSETTO}[✔] {testo}{Stile.RESET}")

def formatta_tempo(ore):
    colore = Stile.VERDE if ore > 6 else Stile.GIALLO if ore > 3 else Stile.ROSSO
    return f"{colore}{Stile.GRASSETTO}{ore} ore{Stile.RESET}"

# --- DATABASE CASI ---
def genera_database_casi():
    return {
        "caso_001": {
            "titolo": "Il Furto del Raffaello",
            "info_crimine": {
                "vittima": "Galleria d'Arte Civica",
                "luogo": "Sala del Rinascimento",
                "ora_stimata": "Tra le 02:00 e le 04:00 di notte"
            },
            "sospettati": {
                "Marco": {
                    "ruolo": "Custode notturno",
                    "dialoghi": {
                        "1": {"domanda": "Dov'eri tra le 02:00 e le 04:00?", "risposta": "Stavo facendo la ronda nel lato opposto dell'edificio.", "visibile": True},
                        "2": {"domanda": "Sappiamo che hai molti debiti...", "risposta": "Non ruberei mai un'opera d'arte per questo.", "visibile": True}
                    }
                },
                "Giulia": {
                    "ruolo": "Restauratrice",
                    "dialoghi": {
                        "1": {"domanda": "Dov'eri stanotte?", "risposta": "Ero a casa a dormire da sola.", "visibile": True},
                        "2": {"domanda": "Hai accesso agli attrezzi di restauro?", "risposta": "Certo, ma tengo la mia cassetta chiusa a chiave nel magazzino.", "visibile": True},
                        # SBLOCCATA DA: Tablet Decifrato (Contiene una menzogna!)
                        "3": {"domanda": "Perché cercavi online come rimuovere una tela antica?", "risposta": "Oh, quello... era solo per una ricerca accademica che sto scrivendo per un'università estera! Non c'entra nulla col furto.", "visibile": False},
                        # SBLOCCATA DA: Crafting (Giulia + Strumento) -> Mette Giulia alle strette
                        "4": {"domanda": "Il bisturi ritrovato è tuo. Spiega i frammenti di vetro esterni.", "risposta": "(Inizia a tremare) Va bene, va bene! Ho simulato l'effrazione dall'interno. Ma l'ho fatto perché Marco mi ricattava con i suoi debiti!", "visibile": False}
                    }
                }
            },
            "prove": {
                "Vetri": {"luogo_ritrovamento": "Marciapiede sotto la finestra", "descrizione": "Frammenti colpiti dall'interno verso l'esterno."},
                "Tablet Bloccato": {
                    "cifrato": True,
                    "decifrato": False,
                    "luogo_ritrovamento": "Bancone del restauro",
                    "descrizione": "Il tablet di Giulia chiede una password. C'è un suggerimento: 'L'attrezzo più tagliente (Anagramma di TRIBUSI)'.",
                    "testo_nascosto": "T R I B U S I",
                    "parola_sblocco": "bisturi",
                    "descrizione_sbloccata": "Cronologia ricerche: 'Come rimuovere una tela antica senza danneggiare i bordi'.",
                    "sblocca_dialogo": ("Giulia", "3") # Sblocca domanda 3 di Giulia
                },
                "Strumento": {"luogo_ritrovamento": "Nascosto dietro un vaso", "descrizione": "Un bisturi di altissima precisione con tracce di pittura a olio."}
            },
            "combinazioni": {
                "giulia_bisturi": {
                    "elementi_richiesti": ["Giulia", "Strumento"],
                    "scoperta": "Il bisturi ritrovato è un attrezzo specifico da restauro. Questo smentisce la sua versione sulla cassetta chiusa e sblocca un duro confronto.",
                    "sbloccato": False,
                    "nome_nuova_prova": "Deduzione: La bugia di Giulia",
                    "sblocca_dialogo": ("Giulia", "4") # Sblocca domanda 4 di Giulia
                }
            },
            "soluzione": {
                "vero_colpevole": "giulia",
                "arma_del_delitto": "bisturi",
                "spiegazione_finale": "Giulia ha estratto la tela col bisturi e rotto la finestra dall'interno. Nella domanda 4 tenta di incolpare Marco, ma la cronologia del tablet dimostra che pianificava il furto da sola molto tempo prima."
            }
        },
        "caso_002": {
            "titolo": "Il Sabotaggio della Honda CB125R",
            "info_crimine": {"vittima": "Pilota amatoriale", "luogo": "Paddock del circuito", "ora_stimata": "Prima delle qualifiche"},
            "sospettati": {
                "Luca": {"ruolo": "Pilota rivale", "dialoghi": {"1": {"domanda": "Dov'eri prima delle qualifiche?", "risposta": "Nel mio box a concentrarmi.", "visibile": True}}},
                "Anna": {"ruolo": "Meccanico", "dialoghi": {"1": {"domanda": "Cercavi vendetta?", "risposta": "Ero furiosa, ma non sono un'assassina.", "visibile": True}}}
            },
            "prove": {
                "Orma": {"luogo_ritrovamento": "Pozza d'olio", "descrizione": "Impronta di uno stivale da corsa con saponette."},
                "Lucchetto": {"cifrato": True, "decifrato": False, "luogo_ritrovamento": "Armadio Luca", "descrizione": "Lucchetto a parola.", "testo_nascosto": ".......SI", "parola_sblocco": "tronchesi", "descrizione_sbloccata": "Tronchesi sporche di liquido freni."}
            },
            "combinazioni": {},
            "soluzione": {"vero_colpevole": "luca", "arma_del_delitto": "tronchesi", "spiegazione_finale": "Luca ha reciso il tubo dei freni."}
        },
        "caso_003": {
            "titolo": "Il Caffè Letale",
            "info_crimine": {"vittima": "Amministratore Delegato", "luogo": "Ufficio direzionale", "ora_stimata": "08:30"},
            "sospettati": {
                "Elena": {"ruolo": "Segretaria", "dialoghi": {"1": {"domanda": "Hai portato tu il caffè?", "risposta": "Sì, alle 08:30 in punto.", "visibile": True}}},
                "Roberto": {"ruolo": "Socio", "dialoghi": {"1": {"domanda": "Quando ha scoperto il corpo?", "risposta": "Sono arrivato alle 08:45.", "visibile": True}}}
            },
            "prove": {
                "Contratto": {"luogo_ritrovamento": "Cestino", "descrizione": "Contratto strappato con impronta di Roberto."}
            },
            "combinazioni": {},
            "soluzione": {"vero_colpevole": "roberto", "arma_del_delitto": "veleno", "spiegazione_finale": "Roberto ha avvelenato il caffè prima delle 08:45."}
        },
        "caso_004": {
            "titolo": "Il Manoscritto Scomparso",
            "info_crimine": {
                "vittima": "Archivio Storico",
                "luogo": "Sezione Letteratura Medievale",
                "ora_stimata": "Notte fonda"
            },
            "sospettati": {
                "Beatrice": {
                    "ruolo": "Bibliotecaria",
                    "dialoghi": {
                        "1": {"domanda": "Dov'eri questa notte?", "risposta": "Facevo l'inventario nell'ala est dell'archivio, lontano dalle teche.", "visibile": True}
                    }
                },
                "Virgilio": {
                    "ruolo": "Professore Universitario",
                    "dialoghi": {
                        "1": {"domanda": "Cosa ci faceva qui fino a tardi?", "risposta": "Studiavo il Canto 26 dell'Inferno. I miei studi sono puramente poetici, non mi occupo di scritti politici.", "visibile": True},
                        # SBLOCCATA DA: Anagramma Sbloccato (Menzogna del prof!)
                        "2": {"domanda": "Abbiamo trovato i suoi appunti sulla 'politica dantesca'...", "risposta": "Ah, quelli? È solo una vecchia tesina di un mio studente che stavo correggendo, non è roba mia!", "visibile": False},
                        # SBLOCCATA DA: Crafting (Virgilio + Graffetta)
                        "3": {"domanda": "I testimoni dicono che lei sa usare i grimaldelli. E questa graffetta?", "risposta": "Va bene! Volevo solo consultare il De Monarchia di nascosto perché Beatrice non me lo concedeva mai. Ma quando sono entrato, la teca era già vuota!", "visibile": False}
                    }
                }
            },
            "prove": {
                "Teca": {"luogo_ritrovamento": "Centro della sala", "descrizione": "Una teca in vetro forzata. Manca il saggio politico 'De Monarchia' di Dante."},
                "Serratura Elettronica": {
                    "cifrato": True,
                    "decifrato": False,
                    "luogo_ritrovamento": "Porta dello studio di Virgilio",
                    "descrizione": "Un appunto cifrato sulla scrivania del prof. È un anagramma: 'ACILITOP'.",
                    "testo_nascosto": "A C I L I T O P",
                    "parola_sblocco": "politica",
                    "descrizione_sbloccata": "Appunti personali di Virgilio: 'Analisi strutturale della politica dantesca'.",
                    "sblocca_dialogo": ("Virgilio", "2")
                },
                "Strumento": {"luogo_ritrovamento": "Tappeto vicino alla teca", "descrizione": "Una spessa graffetta di metallo piegata ad arte per scassinare."}
            },
            "combinazioni": {
                "virgilio_graffetta": {
                    "elementi_richiesti": ["Virgilio", "Strumento"],
                    "scoperta": "Un ex collega di Virgilio rivela che il professore ha l'hobby del lockpicking (apertura serrature). La graffetta è sua.",
                    "sbloccato": False,
                    "nome_nuova_prova": "Deduzione: Abilità sospette",
                    "sblocca_dialogo": ("Virgilio", "3")
                }
            },
            "soluzione": {
                "vero_colpevole": "virgilio",
                "arma_del_delitto": "graffetta",
                "spiegazione_finale": "Virgilio mente fino alla fine. Ha scassinato la teca con la graffetta per rubare il testo e usarlo nelle sue pubblicazioni segrete."
            }
        },
        "caso_005": {
            "titolo": "Il Sabotaggio Biologico",
            "info_crimine": {
                "vittima": "Progetto Scolastico",
                "luogo": "Laboratorio di Chimica",
                "ora_stimata": "Pausa pranzo"
            },
            "sospettati": {
                "Leo": {
                    "ruolo": "Studente modello",
                    "dialoghi": {
                        "1": {"domanda": "Eri in laboratorio durante la pausa?", "risposta": "Sì, ripassavo chimica inorganica da solo al mio banco.", "visibile": True},
                        # SBLOCCATA DA: Registro Decifrato
                        "2": {"domanda": "Il registro dice che hai aperto l'armadietto dei reagenti.", "risposta": "L'ho aperto solo per prendere del semplice distillato! Non ho toccato gli acidi.", "visibile": False},
                        # SBLOCCATA DA: Crafting (Leo + Flacone)
                        "3": {"domanda": "Ci sono le tue impronte sul becher dell'acido acido corrosivo.", "risposta": "Va bene! Ho gettato l'acido sul cervello di vitello dei miei compagni. Volevo sabotarli perché il loro progetto era migliore del mio!", "visibile": False}
                    }
                },
                "Sofia": {
                    "ruolo": "Rappresentante",
                    "dialoghi": {
                        "1": {"domanda": "Cosa facevi nei corridoi?", "risposta": "Cercavo solo dei gessetti per la lavagna.", "visibile": True}
                    }
                }
            },
            "prove": {
                "Preparato": {"luogo_ritrovamento": "Bancone", "descrizione": "Un cervello di vitello da analizzare completamente corroso da sostanze chimiche."},
                "Registro Digitale": {
                    "cifrato": True,
                    "decifrato": False,
                    "luogo_ritrovamento": "PC del laboratorio",
                    "descrizione": "Il log richiede il numero atomico del carbonio (usa la cifra):",
                    "testo_nascosto": "C = ?",
                    "parola_sblocco": "6",
                    "descrizione_sbloccata": "Log: Armadietto reagenti aperto alle 13:15 dall'utente 'Leo'.",
                    "sblocca_dialogo": ("Leo", "2")
                },
                "Flacone": {"luogo_ritrovamento": "Lavandino", "descrizione": "Un becher con residui di acido corrosivo."}
            },
            "combinazioni": {
                "leo_flacone": {
                    "elementi_richiesti": ["Leo", "Flacone"],
                    "scoperta": "La polizia scientifica rileva impronte digitali nitide di Leo sul becher dell'acido.",
                    "sbloccato": False,
                    "nome_nuova_prova": "Deduzione: Impronte sull'acido",
                    "sblocca_dialogo": ("Leo", "3")
                }
            },
            "soluzione": {
                "vero_colpevole": "leo",
                "arma_del_delitto": "acido",
                "spiegazione_finale": "Leo ha usato le sue credenziali per prendere l'acido e distruggere il cervello di vitello analizzato dai suoi rivali per mantenere il primato dei voti."
            }
        }
    }

def seleziona_caso_manualmente(database):
    while True:
        stampa_titolo("SELEZIONE DEL CASO")
        chiavi_casi = list(database.keys())
        for i, id_caso in enumerate(chiavi_casi):
            print(f"{Stile.CIANO}{i+1}.{Stile.RESET} {database[id_caso]['titolo']}")
        scelta = input(f"\n{Stile.GRASSETTO}Quale caso vuoi affrontare?: {Stile.RESET}").strip()
        if scelta.isdigit() and 1 <= int(scelta) <= len(chiavi_casi):
            return database[chiavi_casi[int(scelta) - 1]]
        stampa_errore("Selezione non valida.")

def mostra_menu_investigazione(ore_rimaste):
    stampa_titolo(f"MENU INVESTIGAZIONE | Tempo rimasto: {formatta_tempo(ore_rimaste)}")
    print(f"{Stile.CIANO}1.{Stile.RESET} Rileggi i dettagli del crimine      {Stile.ROSSO}(-1 ora){Stile.RESET}")
    print(f"{Stile.CIANO}2.{Stile.RESET} Vai nella sala interrogatori        {Stile.ROSSO}(-1 ora x domanda){Stile.RESET}")
    print(f"{Stile.CIANO}3.{Stile.RESET} Esamina le prove e i cifrari       {Stile.ROSSO}(-2 ore){Stile.RESET}")
    print(f"{Stile.CIANO}4.{Stile.RESET} Lavagna Deduzioni (Unisci indizi)   {Stile.ROSSO}(-1 ora){Stile.RESET}")
    print(f"{Stile.CIANO}5.{Stile.RESET} Fai la tua accusa (Risolvi il caso)")
    print(f"{Stile.CIANO}6.{Stile.RESET} Esci dal gioco")
    return input(f"\n{Stile.GRASSETTO}Scelta (1-6): {Stile.RESET}")

def gioca():
    print(f"\n{Stile.VERDE}{Stile.GRASSETTO}=== DATABASE INVESTIGATIVO INIZIALIZZATO ==={Stile.RESET}")
    database = genera_database_casi()
    caso_attuale = seleziona_caso_manualmente(database)
   
    print(f"\nÈ stato caricato il caso: {Stile.GIALLO}{Stile.GRASSETTO}{caso_attuale['titolo']}{Stile.RESET}")
   
    ore_rimaste = 16
    risolto = False

    while not risolto:
        if ore_rimaste <= 0:
            stampa_errore("TEMPO SCADUTO! Il colpevole è fuggito.")
            break

        scelta = mostra_menu_investigazione(ore_rimaste)

        if scelta == '1':
            ore_rimaste -= 1
            stampa_sottotitolo("INFORMAZIONI SUL CRIMINE")
            for chiave, valore in caso_attuale["info_crimine"].items():
                print(f"{Stile.GRASSETTO}{chiave.replace('_', ' ').capitalize()}:{Stile.RESET} {valore}")

        elif scelta == '2':
            in_sala_interrogatori = True
            while in_sala_interrogatori and ore_rimaste > 0:
                stampa_sottotitolo("SALA INTERROGATORI")
                nomi_sospettati = list(caso_attuale["sospettati"].keys())
               
                for i, nome in enumerate(nomi_sospettati):
                    print(f"{Stile.CIANO}{i+1}.{Stile.RESET} Interroga {Stile.GIALLO}{nome}{Stile.RESET}")
                print(f"{Stile.CIANO}0.{Stile.RESET} Torna al menu principale")
               
                scelta_sos = input(f"\n{Stile.GRASSETTO}Chi vuoi interrogare?: {Stile.RESET}")
                if scelta_sos == '0': in_sala_interrogatori = False
                elif scelta_sos.isdigit() and 1 <= int(scelta_sos) <= len(nomi_sospettati):
                    sospettato_attuale = nomi_sospettati[int(scelta_sos) - 1]
                    dialoghi = caso_attuale["sospettati"][sospettato_attuale]["dialoghi"]
                   
                    in_interrogatorio = True
                    while in_interrogatorio and ore_rimaste > 0:
                        stampa_sottotitolo(f"INTERROGANDO: {sospettato_attuale.upper()}")
                       
                        # Mostra SOLO i dialoghi impostati come visibili
                        domande_valide = {}
                        for id_domanda, dati in dialoghi.items():
                            if dati["visibile"]:
                                domande_valide[id_domanda] = dati
                                print(f"{Stile.CIANO}{id_domanda}.{Stile.RESET} \"{dati['domanda']}\" {Stile.ROSSO}(-1 ora){Stile.RESET}")
                               
                        print(f"{Stile.CIANO}0.{Stile.RESET} Congeda il sospettato")
                       
                        scelta_domanda = input(f"\n{Stile.GRASSETTO}Quale domanda fai?: {Stile.RESET}")
                        if scelta_domanda == '0': in_interrogatorio = False
                        elif scelta_domanda in domande_valide:
                            ore_rimaste -= 1
                            print(f"\n{Stile.GIALLO}[{sospettato_attuale}]:{Stile.RESET} \"{domande_valide[scelta_domanda]['risposta']}\"")
                        else:
                            stampa_errore("Scelta non valida o domanda ancora bloccata.")
                else:
                    stampa_errore("Input non valido.")

        elif scelta == '3':
            ore_rimaste -= 2
            stampa_sottotitolo("ARCHIVIO PROVE")
            for nome_prova, info in caso_attuale["prove"].items():
                print(f"\n{Stile.VIOLA}{Stile.GRASSETTO}Prova: {nome_prova}{Stile.RESET}")
                if info.get("cifrato"):
                    if not info.get("decifrato"):
                        print(f" {Stile.GIALLO}- Enigma:{Stile.RESET} {info['descrizione']}")
                        print(f" {Stile.ROSSO}- Codice:{Stile.RESET} {info['testo_nascosto']}")
                        tentativo = input(f"\n{Stile.GRASSETTO}Password (Usa parole/numeri corti): {Stile.RESET}").lower().strip()
                       
                        if tentativo == info["parola_sblocco"]:
                            stampa_successo("Codice violato!")
                            info["decifrato"] = True
                            print(f" {Stile.VERDE}- Messaggio:{Stile.RESET} {info['descrizione_sbloccata']}")
                           
                            # --- NOTIFICA SBLOCCO DIALOGO DIRETTO ---
                            if "sblocca_dialogo" in info:
                                sos, id_d = info["sblocca_dialogo"]
                                caso_attuale["sospettati"][sos]["dialoghi"][id_d]["visibile"] = True
                                print(f"{Stile.VIOLA}{Stile.GRASSETTO}\n[NUOVA DOMANDA SBLOCCATA] Un indizio nel codice ti permette di fare una nuova domanda a {sos}!{Stile.RESET}")
                        else:
                            stampa_errore("Password errata. Perdi 1 ora.")
                            ore_rimaste -= 1
                    else:
                        print(f" {Stile.VERDE}- Messaggio Decifrato:{Stile.RESET} {info['descrizione_sbloccata']}")
                else:
                    for chiave, valore in info.items():
                        print(f" {Stile.GRASSETTO}-{Stile.RESET} {chiave.replace('_', ' ').capitalize()}: {valore}")

        elif scelta == '4':
            stampa_sottotitolo("LAVAGNA DELLE DEDUZIONI")
            elementi_disponibili = list(caso_attuale["sospettati"].keys()) + list(caso_attuale["prove"].keys())
            for i, elemento in enumerate(elementi_disponibili):
                print(f"{Stile.CIANO}{i+1}.{Stile.RESET} {elemento}")
           
            scelta_1 = input(f"\n{Stile.GRASSETTO}Primo elemento (numero): {Stile.RESET}")
            scelta_2 = input(f"{Stile.GRASSETTO}Secondo elemento (numero): {Stile.RESET}")
           
            if scelta_1.isdigit() and scelta_2.isdigit():
                idx1, idx2 = int(scelta_1) - 1, int(scelta_2) - 1
                if 0 <= idx1 < len(elementi_disponibili) and 0 <= idx2 < len(elementi_disponibili) and idx1 != idx2:
                    el1, el2 = elementi_disponibili[idx1], elementi_disponibili[idx2]
                   
                    combinazione_trovata = False
                    for chiave_comb, dati_comb in caso_attuale.get("combinazioni", {}).items():
                        richiesti = dati_comb["elementi_richiesti"]
                        if (el1 in richiesti) and (el2 in richiesti):
                            combinazione_trovata = True
                            if not dati_comb.get("sbloccato", False):
                                ore_rimaste -= 1
                                dati_comb["sbloccato"] = True
                                stampa_successo("COLLEGAMENTO LOGICO EFFETTUATO!")
                                print(f"{Stile.GIALLO}{dati_comb['scoperta']}{Stile.RESET}")
                               
                                caso_attuale["prove"][dati_comb["nome_nuova_prova"]] = {
                                    "luogo_ritrovamento": "Lavagna", "descrizione": dati_comb["scoperta"]
                                }
                                # --- NOTIFICA SBLOCCO DIALOGO DA CRAFTING ---
                                if "sblocca_dialogo" in dati_comb:
                                    sos, id_d = dati_comb["sblocca_dialogo"]
                                    caso_attuale["sospettati"][sos]["dialoghi"][id_d]["visibile"] = True
                                    print(f"{Stile.VIOLA}{Stile.GRASSETTO}\n[NUOVA DOMANDA SBLOCCATA] Mettendo insieme i pezzi hai sbloccato una nuova pista per interrogare {sos}!{Stile.RESET}")
                            else:
                                print("Indizi già collegati.")
                            break
                    if not combinazione_trovata:
                        stampa_errore("Nessun legame. Perdi 1 ora.")
                        ore_rimaste -= 1

        elif scelta == '5':
            stampa_sottotitolo("ACCUSA FINALE")
            accusa_colpevole = input(f"Chi è il colpevole?: {Stile.RESET}")
            accusa_arma = input(f"Arma/Oggetto usato?: {Stile.RESET}")
           
            if accusa_colpevole.lower().strip() == caso_attuale["soluzione"]["vero_colpevole"] and accusa_arma.lower().strip() == caso_attuale["soluzione"]["arma_del_delitto"]:
                stampa_titolo("CASO RISOLTO!")
                print(f"{Stile.GIALLO}Spiegazione:{Stile.RESET} {caso_attuale['soluzione']['spiegazione_finale']}")
                risolto = True
            else:
                stampa_errore("Accusa respinta. Perdi 3 ore.")
                ore_rimaste -= 3

        elif scelta == '6': break

if __name__ == "__main__":
    gioca()