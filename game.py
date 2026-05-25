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
                        "1": {"domanda": "Dov'eri tra le 02:00 e le 04:00?", "risposta": "Stavo facendo la ronda nel lato opposto dell'edificio."},
                        "2": {"domanda": "Sappiamo che hai molti debiti...", "risposta": "Non ruberei mai un'opera d'arte per questo."}
                    }
                },
                "Giulia": {
                    "ruolo": "Restauratrice",
                    "dialoghi": {
                        "1": {"domanda": "Dov'eri stanotte?", "risposta": "Ero a casa a dormire."},
                        "2": {"domanda": "Hai accesso agli attrezzi di restauro?", "risposta": "Certo, ma tengo la mia cassetta chiusa a chiave."}
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
                    "descrizione_sbloccata": "Cronologia ricerche: 'Come rimuovere una tela antica senza danneggiare i bordi'."
                },
                "Strumento": {"luogo_ritrovamento": "Nascosto dietro un vaso", "descrizione": "Un bisturi di altissima precisione con tracce di pittura a olio."}
            },
            "combinazioni": {
                "giulia_bisturi": {
                    "elementi_richiesti": ["Giulia", "Strumento"],
                    "scoperta": "Il bisturi ritrovato è un attrezzo specifico per restauratori. Smentisce la dichiarazione di Giulia secondo cui i suoi attrezzi erano al sicuro e chiusi a chiave!",
                    "sbloccato": False,
                    "nome_nuova_prova": "Deduzione: La bugia di Giulia"
                }
            },
            "soluzione": {
                "vero_colpevole": "giulia",
                "arma_del_delitto": "bisturi",
                "spiegazione_finale": "Giulia ha estratto la tela col bisturi e rotto la finestra dall'interno."
            }
        },
        "caso_002": {
            "titolo": "Il Sabotaggio della Honda CB125R",
            "info_crimine": {
                "vittima": "Pilota amatoriale",
                "luogo": "Paddock del circuito",
                "ora_stimata": "Poco prima delle qualifiche"
            },
            "sospettati": {
                "Luca": {
                    "ruolo": "Pilota rivale",
                    "dialoghi": {
                        "1": {"domanda": "Dov'eri prima delle qualifiche?", "risposta": "Ero nel mio box. Mi stavo già preparando per la pista."},
                        "2": {"domanda": "Volevi vincere a tutti i costi?", "risposta": "Voglio vincere pulito in pista!"}
                    }
                },
                "Anna": {
                    "ruolo": "Meccanico licenziato",
                    "dialoghi": {
                        "1": {"domanda": "Cercavi vendetta?", "risposta": "Ero furiosa, ma non sono un'assassina."},
                        "2": {"domanda": "Dov'eri al momento del sabotaggio?", "risposta": "Ero alla tavola calda del circuito."}
                    }
                }
            },
            "prove": {
                "Orma": {"luogo_ritrovamento": "Pozza d'olio", "descrizione": "Impronta di uno stivale da corsa con saponette."},
                "Lucchetto a combinazione": {
                    "cifrato": True,
                    "decifrato": False,
                    "luogo_ritrovamento": "Armadietto degli attrezzi di Luca",
                    "descrizione": "Un lucchetto a parola di 9 lettere. Sopra c'è scritto: 'Serve a tagliare cavi spessi'.",
                    "testo_nascosto": "_ _ _ _ _ _ _ S I",
                    "parola_sblocco": "tronchesi",
                    "descrizione_sbloccata": "All'interno dell'armadietto di Luca ci sono delle tronchesi sporche di liquido freni."
                }
            },
            "combinazioni": {
                "orma_luca": {
                    "elementi_richiesti": ["Orma", "Luca"],
                    "scoperta": "L'impronta di stivale con saponette non può appartenere al meccanico (Anna). L'unico vestito con attrezzatura da pista al momento del sabotaggio era Luca!",
                    "sbloccato": False,
                    "nome_nuova_prova": "Deduzione: Stivali Incastranti"
                }
            },
            "soluzione": {
                "vero_colpevole": "luca",
                "arma_del_delitto": "tronchesi",
                "spiegazione_finale": "Luca ha reciso il tubo dei freni con le tronchesi."
            }
        },
        "caso_003": {
            "titolo": "Il Caffè Letale",
            "info_crimine": {
                "vittima": "Amministratore Delegato",
                "luogo": "Ufficio direzionale",
                "ora_stimata": "08:30 del mattino"
            },
            "sospettati": {
                "Elena": {
                    "ruolo": "Segretaria",
                    "dialoghi": {
                        "1": {"domanda": "Hai portato tu il caffè?", "risposta": "Sì, come ogni mattina."},
                        "2": {"domanda": "Ti maltrattava?", "risposta": "Era un tiranno. Ma stavo per licenziarmi."}
                    }
                },
                "Roberto": {
                    "ruolo": "Socio in affari",
                    "dialoghi": {
                        "1": {"domanda": "Quando ha scoperto il corpo?", "risposta": "Sono arrivato alle 08:45 e l'ho trovato accasciato."},
                        "2": {"domanda": "Problemi per la vendita dell'azienda?", "risposta": "Stava svendendo il lavoro di una vita."}
                    }
                }
            },
            "prove": {
                "Contratto": {"luogo_ritrovamento": "Cestino", "descrizione": "Contratto strappato con impronta digitale fresca di Roberto."},
                "Appunto Cifrato": {
                    "cifrato": True,
                    "decifrato": False,
                    "luogo_ritrovamento": "Tasca della vittima",
                    "descrizione": "La vittima ha scritto un promemoria usando il Cifrario di Cesare con spostamento di +3 (A=D, B=E).",
                    "testo_nascosto": "Y H O H Q R",
                    "parola_sblocco": "veleno",
                    "descrizione_sbloccata": "Promemoria: 'Roberto ha comprato un veleno letale al mercato nero. Devo affrontarlo stamattina'."
                }
            },
            "combinazioni": {
                "roberto_contratto": {
                    "elementi_richiesti": ["Roberto", "Contratto"],
                    "scoperta": "Se Roberto è arrivato alle 08:45 a omicidio già avvenuto, come fa ad esserci la sua impronta FRESCA sul contratto cestinato? Mente sull'orario di arrivo!",
                    "sbloccato": False,
                    "nome_nuova_prova": "Deduzione: Il finto alibi"
                }
            },
            "soluzione": {
                "vero_colpevole": "roberto",
                "arma_del_delitto": "veleno",
                "spiegazione_finale": "Roberto è arrivato prima, ha litigato e avvelenato il caffè."
            }
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
                        "1": {"domanda": "Dov'eri questa notte?", "risposta": "Facevo l'inventario nell'ala est dell'archivio, lontano dalle teche."},
                        "2": {"domanda": "Perché l'allarme era disattivato?", "risposta": "C'è stato un calo di tensione documentato. Nessun sabotaggio."}
                    }
                },
                "Virgilio": {
                    "ruolo": "Professore Universitario",
                    "dialoghi": {
                        "1": {"domanda": "Cosa ci faceva qui fino a tardi?", "risposta": "Studiavo il Canto 26 dell'Inferno per una mia nuova pubblicazione."},
                        "2": {"domanda": "Le serviva il De Monarchia, per caso?", "risposta": "No, i miei studi sono puramente poetici, non mi occupo di scritti politici."}
                    }
                }
            },
            "prove": {
                "Teca": {"luogo_ritrovamento": "Centro della sala", "descrizione": "Una teca in vetro forzata. Al suo interno mancava una rara trascrizione commentata del trattato di Dante Alighieri."},
                "Serratura Elettronica": {
                    "cifrato": True,
                    "decifrato": False,
                    "luogo_ritrovamento": "Porta dello studio di Virgilio",
                    "descrizione": "Il professore ha lasciato un promemoria cifrato sulla scrivania. È un anagramma: 'ACILITOP'.",
                    "testo_nascosto": "A C I L I T O P",
                    "parola_sblocco": "politica",
                    "descrizione_sbloccata": "Appunto rivelato: 'Appunti per saggio sulla politica dantesca'."
                },
                "Strumento": {"luogo_ritrovamento": "Tappeto vicino alla teca", "descrizione": "Una spessa graffetta di metallo piegata ad arte per far scattare le vecchie serrature."}
            },
            "combinazioni": {
                "virgilio_serratura": {
                    "elementi_richiesti": ["Virgilio", "Serratura Elettronica"],
                    "scoperta": "Virgilio ha affermato di non essere minimamente interessato alle opere politiche, ma i suoi appunti privati dimostrano l'esatto contrario. Ha mentito sul suo movente!",
                    "sbloccato": False,
                    "nome_nuova_prova": "Deduzione: La finta ignoranza"
                }
            },
            "soluzione": {
                "vero_colpevole": "virgilio",
                "arma_del_delitto": "graffetta",
                "spiegazione_finale": "Virgilio voleva accaparrarsi il De Monarchia per pubblicare una ricerca inedita a suo nome. Ha usato una graffetta per forzare la teca, approfittando del calo di tensione."
            }
        },
        "caso_005": {
            "titolo": "Il Sabotaggio Biologico",
            "info_crimine": {
                "vittima": "Progetto Scolastico",
                "luogo": "Laboratorio di Chimica e Scienze",
                "ora_stimata": "Pausa pranzo"
            },
            "sospettati": {
                "Leo": {
                    "ruolo": "Studente modello",
                    "dialoghi": {
                        "1": {"domanda": "Eri in laboratorio durante la pausa?", "risposta": "Sì, ripassavo chimica inorganica e le reazioni base in silenzio."},
                        "2": {"domanda": "Invidioso del progetto altrui?", "risposta": "Io ho sempre i voti più alti della classe, non ho bisogno di sabotare gli altri."}
                    }
                },
                "Sofia": {
                    "ruolo": "Rappresentante d'istituto",
                    "dialoghi": {
                        "1": {"domanda": "Cosa facevi nei corridoi del laboratorio?", "risposta": "Cercavo dei gessetti di scorta per la nostra lavagna di classe."},
                        "2": {"domanda": "Hai accesso ai reagenti?", "risposta": "No, gli armadietti della chimica sono chiusi a chiave dai professori."}
                    }
                }
            },
            "prove": {
                "Preparato": {"luogo_ritrovamento": "Bancone da lavoro", "descrizione": "Il reperto biologico (un cervello di vitello da analizzare) è stato completamente corroso, distruggendo il lavoro di un mese."},
                "Registro Digitale": {
                    "cifrato": True,
                    "decifrato": False,
                    "luogo_ritrovamento": "Armadietto dei reagenti chimici",
                    "descrizione": "Il log di accesso all'armadietto è protetto da un indovinello del prof: 'Indica il numero atomico del carbonio (usa la cifra numerica)'.",
                    "testo_nascosto": "X",
                    "parola_sblocco": "6",
                    "descrizione_sbloccata": "Il registro elettronico mostra un log di apertura recente effettuato con le credenziali personali di Leo."
                },
                "Flacone": {"luogo_ritrovamento": "Lavandino del laboratorio", "descrizione": "Un becher contenente tracce di un potente acido corrosivo."}
            },
            "combinazioni": {
                "leo_registro": {
                    "elementi_richiesti": ["Leo", "Registro Digitale"],
                    "scoperta": "Leo sostiene di aver passato il tempo a studiare al suo banco, ma il suo codice personale ha aperto l'armadietto dei reagenti altamente pericolosi!",
                    "sbloccato": False,
                    "nome_nuova_prova": "Deduzione: L'accesso non autorizzato"
                }
            },
            "soluzione": {
                "vero_colpevole": "leo",
                "arma_del_delitto": "acido",
                "spiegazione_finale": "Leo temeva che l'eccellente dissezione del cervello di vitello garantisse ai compagni un voto superiore al suo, minacciando il suo primato. Ha usato il suo account per prendere l'acido e distruggere la prova."
            }
        }
    }

def seleziona_caso_casuale(database):
    id_caso = random.choice(list(database.keys()))
    return database[id_caso]

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
    caso_attuale = seleziona_caso_casuale(database)
   
    print(f"\nÈ stato assegnato un nuovo caso: {Stile.GIALLO}{Stile.GRASSETTO}{caso_attuale['titolo']}{Stile.RESET}")
   
    ore_rimaste = 15
    risolto = False

    while not risolto:
        if ore_rimaste <= 0:
            stampa_errore("TEMPO SCADUTO!")
            print(f"{Stile.ROSSO}Il caso è rimasto irrisolto troppo a lungo. Il colpevole è fuggito.{Stile.RESET}")
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
                    ruolo = caso_attuale['sospettati'][nome]['ruolo']
                    print(f"{Stile.CIANO}{i+1}.{Stile.RESET} Interroga {Stile.GIALLO}{nome}{Stile.RESET} ({ruolo})")
                print(f"{Stile.CIANO}0.{Stile.RESET} Torna al menu principale")
               
                scelta_sos = input(f"\n{Stile.GRASSETTO}Chi vuoi interrogare? {Stile.RESET}")
               
                if scelta_sos == '0':
                    in_sala_interrogatori = False
                elif scelta_sos.isdigit() and 1 <= int(scelta_sos) <= len(nomi_sospettati):
                    indice_sos = int(scelta_sos) - 1
                    sospettato_attuale = nomi_sospettati[indice_sos]
                    dialoghi = caso_attuale["sospettati"][sospettato_attuale]["dialoghi"]
                   
                    in_interrogatorio = True
                    while in_interrogatorio and ore_rimaste > 0:
                        stampa_sottotitolo(f"INTERROGANDO: {sospettato_attuale.upper()} [Tempo: {formatta_tempo(ore_rimaste)}]")
                        for id_domanda, dati in dialoghi.items():
                            print(f"{Stile.CIANO}{id_domanda}.{Stile.RESET} Chiedi: \"{dati['domanda']}\" {Stile.ROSSO}(-1 ora){Stile.RESET}")
                        print(f"{Stile.CIANO}0.{Stile.RESET} Congeda il sospettato")
                       
                        scelta_domanda = input(f"\n{Stile.GRASSETTO}Quale domanda fai? {Stile.RESET}")
                       
                        if scelta_domanda == '0':
                            in_interrogatorio = False
                        elif scelta_domanda in dialoghi:
                            ore_rimaste -= 1
                            print(f"\n{Stile.GIALLO}[{sospettato_attuale}]:{Stile.RESET} \"{dialoghi[scelta_domanda]['risposta']}\"")
                           
                            if ore_rimaste <= 0:
                                stampa_errore("Il tempo è terminato nel bel mezzo dell'interrogatorio!")
                                break
                        else:
                            print(f"{Stile.ROSSO}Scelta non valida.{Stile.RESET}")
                else:
                    print(f"{Stile.ROSSO}Input non valido, riprova.{Stile.RESET}")

        elif scelta == '3':
            ore_rimaste -= 2
            stampa_sottotitolo("ARCHIVIO PROVE")
            for nome_prova, info in caso_attuale["prove"].items():
                print(f"\n{Stile.VIOLA}{Stile.GRASSETTO}Prova: {nome_prova}{Stile.RESET}")
               
                if info.get("cifrato"):
                    if not info.get("decifrato"):
                        print(f" {Stile.GRASSETTO}- Luogo:{Stile.RESET} {info['luogo_ritrovamento']}")
                        print(f" {Stile.GIALLO}- Enigma:{Stile.RESET} {info['descrizione']}")
                        print(f" {Stile.ROSSO}- Codice:{Stile.RESET} {info['testo_nascosto']}")
                       
                        tentativo = input(f"\n{Stile.GRASSETTO}Password (Invio per uscire) [-1 ora se sbagli]: {Stile.RESET}").lower().strip()
                       
                        if tentativo == info["parola_sblocco"]:
                            stampa_successo("Codice violato!")
                            info["decifrato"] = True
                            print(f" {Stile.VERDE}- Messaggio:{Stile.RESET} {info['descrizione_sbloccata']}")
                        elif tentativo != "":
                            stampa_errore("Password errata. Perdi 1 ora preziosa.")
                            ore_rimaste -= 1
                    else:
                        print(f" {Stile.GRASSETTO}- Luogo:{Stile.RESET} {info['luogo_ritrovamento']}")
                        print(f" {Stile.VERDE}- Messaggio:{Stile.RESET} {info['descrizione_sbloccata']}")
                else:
                    for chiave, valore in info.items():
                        if chiave not in ["cifrato", "decifrato", "parola_sblocco", "testo_nascosto", "descrizione_sbloccata"]:
                            print(f" {Stile.GRASSETTO}-{Stile.RESET} {chiave.replace('_', ' ').capitalize()}: {valore}")

        elif scelta == '4':
            stampa_sottotitolo("LAVAGNA DELLE DEDUZIONI (CRAFTING)")
            print("Scegli due elementi (Sospettati o Prove) per cercare un collegamento logico.")
           
            # Crea una lista unificata di tutti gli elementi disponibili
            elementi_disponibili = list(caso_attuale["sospettati"].keys()) + list(caso_attuale["prove"].keys())
           
            for i, elemento in enumerate(elementi_disponibili):
                print(f"{Stile.CIANO}{i+1}.{Stile.RESET} {elemento}")
            print(f"{Stile.CIANO}0.{Stile.RESET} Annulla")
           
            scelta_1 = input(f"\n{Stile.GRASSETTO}Scegli il PRIMO elemento (numero): {Stile.RESET}")
            if scelta_1 == '0': continue
           
            scelta_2 = input(f"{Stile.GRASSETTO}Scegli il SECONDO elemento (numero): {Stile.RESET}")
            if scelta_2 == '0': continue
           
            if scelta_1.isdigit() and scelta_2.isdigit():
                idx1, idx2 = int(scelta_1) - 1, int(scelta_2) - 1
               
                if (0 <= idx1 < len(elementi_disponibili)) and (0 <= idx2 < len(elementi_disponibili)):
                    el1 = elementi_disponibili[idx1]
                    el2 = elementi_disponibili[idx2]
                   
                    if el1 == el2:
                        stampa_errore("Devi scegliere due elementi DIVERSI.")
                        continue
                       
                    # Controlla se la coppia esiste nelle combinazioni previste per questo caso
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
                               
                                # Aggiungiamo la deduzione come nuova "prova" fissa nel database
                                caso_attuale["prove"][dati_comb["nome_nuova_prova"]] = {
                                    "luogo_ritrovamento": "Lavagna Investigativa",
                                    "descrizione": dati_comb["scoperta"]
                                }
                            else:
                                print(f"\n{Stile.BLU}Hai già unito questi indizi in precedenza.{Stile.RESET}")
                            break
                   
                    if not combinazione_trovata:
                        ore_rimaste -= 1
                        stampa_errore(f"Nessun collegamento logico evidente tra '{el1}' e '{el2}'. Hai perso 1 ora a pensarci su.")
                else:
                    print(f"{Stile.ROSSO}Numeri non validi.{Stile.RESET}")
            else:
                print(f"{Stile.ROSSO}Input non valido.{Stile.RESET}")

        elif scelta == '5':
            stampa_sottotitolo("ACCUSA FINALE")
            print(f"{Stile.GIALLO}(Usa una sola parola per rispondere, es. il nome esatto o l'oggetto){Stile.RESET}")
           
            accusa_colpevole = input(f"\n{Stile.GRASSETTO}Chi è il vero colpevole? {Stile.RESET}")
            accusa_arma = input(f"{Stile.GRASSETTO}Quale oggetto/arma è stato usato? {Stile.RESET}")
           
            colpevole_reale = caso_attuale["soluzione"]["vero_colpevole"].lower().strip()
            arma_reale = caso_attuale["soluzione"]["arma_del_delitto"].lower().strip()

            if accusa_colpevole.lower().strip() == colpevole_reale and accusa_arma.lower().strip() == arma_reale:
                stampa_titolo("CASO RISOLTO!")
                stampa_successo("Hai individuato il colpevole e l'arma del delitto.")
                print(f"\n{Stile.GIALLO}Spiegazione ufficiale:{Stile.RESET} {caso_attuale['soluzione']['spiegazione_finale']}")
                print(f"{Stile.VERDE}Hai chiuso il caso con ancora {ore_rimaste} ore di anticipo!{Stile.RESET}\n")
                risolto = True
            else:
                stampa_errore("Le tue deduzioni su colpevole e/o arma non sono corrette.")
                print("L'accusa sbagliata ti ha fatto perdere 3 ore di tempo prezioso.")
                ore_rimaste -= 3

        elif scelta == '6':
            print(f"\n{Stile.BLU}Chiusura dell'indagine. Arrivederci!{Stile.RESET}")
            break
        else:
            print(f"{Stile.ROSSO}Scelta non valida. Riprova.{Stile.RESET}")

if __name__ == "__main__":
    gioca()
