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
                "ora_stimata": "Tra le 02:00 e le 04:00 di notte",
                "descrizione_scena": "Un inestimabile dipinto di Raffaello è stato rimosso dalla cornice. Il vetro della finestra è rotto, ma i frammenti sono sparsi sul marciapiede all'esterno."
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
                        "3": {"domanda": "Perché cercavi online come rimuovere una tela antica?", "risposta": "Oh, quello... era solo per una ricerca accademica! Non c'entra nulla col furto.", "visibile": False},
                        "4": {"domanda": "Il bisturi ritrovato è tuo. Spiega i frammenti di vetro esterni.", "risposta": "(Inizia a tremare) Va bene, ho simulato l'effrazione dall'interno! Ma l'ho fatto perché Marco mi ricattava!", "visibile": False}
                    }
                }
            },
            "prove": {
                "Vetri": {"luogo_ritrovamento": "Marciapiede sotto la finestra", "descrizione": "Frammenti colpiti dall'interno verso l'esterno."},
                "Tablet Bloccato": {
                    "cifrato": True,
                    "decifrato": False,
                    "sbloccato_da_azione": False,  # Richiede di interrogare Giulia (Domanda 2)
                    "messaggio_blocco": "Il tablet è protetto da cifratura biometrica e un suggerimento testuale. Non hai ancora indizi su come forzarlo.",
                    "luogo_ritrovamento": "Bancone del restauro",
                    "descrizione": "Il tablet di Giulia chiede una password. Dopo averla sentita parlare di attrezzi (Domanda 2), noti un'incisione sul retro: 'Anagramma di TRIBUSI'.",
                    "testo_nascosto": "T R I B U S I",
                    "parola_sblocco": "bisturi",
                    "descrizione_sbloccata": "Cronologia ricerche: 'Come rimuovere una tela antica senza danneggiare i bordi'.",
                    "sblocca_dialogo": ("Giulia", "3")
                },
                "Strumento": {"luogo_ritrovamento": "Nascosto dietro un vaso", "descrizione": "Un bisturi di altissima precisione con tracce di pittura a olio."}
            },
            "combinazioni": {
                "giulia_bisturi": {
                    "elementi_richiesti": ["Giulia", "Strumento"],
                    "scoperta": "Il bisturi ritrovato è specifico da restauro. Questo smentisce la sua versione della cassetta chiusa e sblocca il confronto finale.",
                    "sbloccato": False,
                    "nome_nuova_prova": "Deduzione: La bugia di Giulia",
                    "sblocca_dialogo": ("Giulia", "4")
                }
            },
            "soluzione": {
                "vero_colpevole": "giulia",
                "arma_del_delitto": "bisturi",
                "spiegazione_finale": "Giulia ha estratto la tela col bisturi e rotto la finestra dall'interno. Tenta di incolpare Marco, ma la cronologia del tablet dimostra la premeditazione solitaria."
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
                "Luca": {"ruolo": "Pilota rivale", "dialoghi": {"1": {"domanda": "Dov'eri prima delle qualifiche?", "risposta": "Nel mio box a concentrarmi.", "visibile": True}}},
                "Anna": {"ruolo": "Meccanico", "dialoghi": {"1": {"domanda": "Cercavi vendetta?", "risposta": "Ero furiosa, ma non sono un'assassina.", "visibile": True}}}
            },
            "prove": {
                "Orma": {"luogo_ritrovamento": "Pozza d'olio", "descrizione": "Impronta di uno stivale da corsa con saponette."},
                "Lucchetto": {
                    "cifrato": True, 
                    "decifrato": False, 
                    "sbloccato_da_azione": True, # Libero, vecchio stile
                    "luogo_ritrovamento": "Armadio Luca", 
                    "descrizione": "Lucchetto a parola.", 
                    "testo_nascosto": ".......SI", 
                    "parola_sblocco": "tronchesi", 
                    "descrizione_sbloccata": "Tronchesi sporche di liquido freni."
                }
            },
            "combinazioni": {},
            "soluzione": {"vero_colpevole": "luca", "arma_del_delitto": "tronchesi", "spiegazione_finale": "Luca ha reciso il tubo dei freni."}
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
                "Elena": {"ruolo": "Segretaria", "dialoghi": {"1": {"domanda": "Hai portato tu il caffè?", "risposta": "Sì, alle 08:30 in punto.", "visibile": True}}},
                "Roberto": {"ruolo": "Socio", "dialoghi": {"1": {"domanda": "Quando ha scoperto il corpo?", "risposta": "Sono arrivato alle 08:45.", "visibile": True}}}
            },
            "prove": {
                "Contratto": {"luogo_ritrovamento": "Cestino", "descrizione": "Contratto strappato con impronta di Roberto."}
            },
            "combinazioni": {},
            "soluzione": {"vero_colpevole": "roberto", "arma_del_delitto": "veleno", "spiegazione_finale": "Roberto ha avvelenato il caffè."}
        },
        "caso_004": {
            "titolo": "Il Manoscritto Scomparso",
            "info_crimine": {
                "vittima": "Archivio Storico",
                "luogo": "Sezione Letteratura Medievale",
                "ora_stimata": "Notte fonda",
                "descrizione_scena": "Una teca in vetro è stata forzata senza far scattare l'allarme principale. Al suo interno mancava una rara trascrizione del 'De Monarchia' di Dante Alighieri."
            },
            "sospettati": {
                "Beatrice": {
                    "ruolo": "Bibliotecaria",
                    "dialoghi": {
                        "1": {"domanda": "Dov'eri questa notte?", "risposta": "Facevo l'inventario nell'ala est, lontano dalle teche.", "visibile": True}
                    }
                },
                "Virgilio": {
                    "ruolo": "Professore Universitario",
                    "dialoghi": {
                        "1": {"domanda": "Cosa ci faceva qui fino a tardi?", "risposta": "Studiavo il Canto 26 dell'Inferno. I miei studi sono puramente poetici, non mi occupo di scritti politici.", "visibile": True},
                        "2": {"domanda": "Abbiamo trovato i suoi appunti sulla 'politica dantesca'...", "risposta": "Ah, quelli? È solo una vecchia tesina di un mio studente che stavo correggendo!", "visibile": False},
                        "3": {"domanda": "I testimoni dicono che lei sa usare i grimaldelli. E questa graffetta?", "risposta": "Va bene! Volevo consultarlo di nascosto. Ma quando sono entrato, la teca era già vuota!", "visibile": False}
                    }
                }
            },
            "prove": {
                "Teca": {"luogo_ritrovamento": "Centro della sala", "descrizione": "Una teca in vetro forzata. Manca il saggio politico di Dante."},
                "Serratura Elettronica": {
                    "cifrato": True,
                    "decifrato": False,
                    "sbloccato_da_azione": False,  # Richiede l'interrogazione di Virgilio (Domanda 1)
                    "messaggio_blocco": "Il file è protetto da un software criptato del dipartimento. Devi prima scoprire a cosa stava lavorando esattamente il Professore per intuire la chiave di volta.",
                    "luogo_ritrovamento": "Porta dello studio di Virgilio",
                    "descrizione": "Dopo aver sentito il prof parlare dei suoi studi (Domanda 1), riesci a fare un override del sistema. L'indizio rimasto è l'anagramma: 'ACILITOP'.",
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
                    "scoperta": "Un collega rivela che Virgilio ha l'hobby del lockpicking. La graffetta sul luogo del delitto combacia con i suoi attrezzi.",
                    "sbloccato": False,
                    "nome_nuova_prova": "Deduzione: Abilità sospette",
                    "sblocca_dialogo": ("Virgilio", "3")
                }
            },
            "soluzione": {
                "vero_colpevole": "virgilio",
                "arma_del_delitto": "graffetta",
                "spiegazione_finale": "Virgilio ha scassinato la teca con la graffetta per rubare il testo e usarlo nelle sue pubblicazioni segrete."
            }
        },
        "caso_005": {
            "titolo": "Il Sabotaggio Biologico",
            "info_crimine": {
                "vittima": "Progetto Scolastico di Scienze",
                "luogo": "Laboratorio di Chimica",
                "ora_stimata": "Pausa pranzo",
                "descrizione_scena": "Il bancone da lavoro della squadra Alpha è a soqquadro. Il loro reperto biologico principale (un cervello di vitello per l'analisi microscopica) è stato completamente corroso da un liquido."
            },
            "sospettati": {
                "Leo": {
                    "ruolo": "Studente modello",
                    "dialoghi": {
                        "1": {"domanda": "Eri in laboratorio durante la pausa?", "risposta": "Sì, ripassavo chimica inorganica da solo al mio banco.", "visibile": True},
                        "2": {"domanda": "Il registro dice che hai aperto l'armadietto dei reagenti.", "risposta": "L'ho aperto solo per prendere dell'acqua distillata! Non ho toccato gli acidi.", "visibile": False},
                        "3": {"domanda": "Ci sono le tue impronte sul becher dell'acido corrosivo.", "risposta": "Va bene! Ho gettato l'acido io. Volevo sabotarli perché il loro progetto era venuto meglio del mio!", "visibile": False}
                    }
                },
                "Sofia": {
                    "ruolo": "Rappresentante d'istituto",
                    "dialoghi": {
                        "1": {"domanda": "Cosa facevi nei corridoi?", "risposta": "Cercavo solo dei gessetti per la lavagna.", "visibile": True}
                    }
                }
            },
            "prove": {
                "Preparato": {"luogo_ritrovamento": "Bancone", "descrizione": "Un cervello di vitello distrutto da sostanze chimiche."},
                "Flacone": {"luogo_ritrovamento": "Lavandino", "descrizione": "Un becher con residui di acido corrosivo."},
                "Registro Digitale": {
                    "cifrato": True,
                    "decifrato": False,
                    "sbloccato_da_azione": False,  # Richiede il Crafting (Leo + Flacone)
                    "messaggio_blocco": "Il registro dei log è bloccato dal computer centrale. Serve un'autorizzazione o una prova schiacciante che colleghi qualcuno a quel laboratorio per costringere il sistema a fare il dump dei dati.",
                    "luogo_ritrovamento": "PC del laboratorio",
                    "descrizione": "Dopo aver trovato le impronte di Leo sul Flacone tramite la lavagna delle deduzioni, il PC sblocca l'accesso alle credenziali. Supera la sicurezza del prof: 'Numero atomico del carbonio (cifra)':",
                    "testo_nascosto": "C = ?",
                    "parola_sblocco": "6",
                    "descrizione_sbloccata": "Log: Armadietto reagenti aperto alle 13:15 dall'utente 'Leo'.",
                    "sblocca_dialogo": ("Leo", "2")
                }
            },
            "combinazioni": {
                "leo_flacone": {
                    "elementi_richiesti": ["Leo", "Flacone"],
                    "scoperta": "La scientifica rileva le impronte di Leo sul becher dell'acido. Questo legame ti permette di violare il PC del laboratorio!",
                    "sbloccato": False,
                    "nome_nuova_prova": "Deduzione: Impronte sull'acido",
                    "sblocca_dump_registro": True  # Sblocca la decrittazione del Registro!
                }
            },
            "soluzione": {
                "vero_colpevole": "leo",
                "arma_del_delitto": "acido",
                "spiegazione_finale": "Leo ha usato le sue credenziali per prendere l'acido e distruggere il cervello di vitello dei suoi rivali per mantenere il primato dei voti."
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
            # Controllo speciale per mostrare la descrizione della scena
            if "descrizione_scena" in caso_attuale["info_crimine"]:
                pass 

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
                            
                            # --- MECCANICA DI SBLOCCO DECRITTAZIONE DA DIALOGO ---
                            # Caso 1: Interrogare Giulia sulla Domanda 2 sblocca il suo Tablet
                            if caso_attuale["titolo"] == "Il Furto del Raffaello" and sospettato_attuale == "Giulia" and scelta_domanda == "2":
                                if not caso_attuale["prove"]["Tablet Bloccato"]["sbloccato_da_azione"]:
                                    caso_attuale["prove"]["Tablet Bloccato"]["sbloccato_da_azione"] = True
                                    print(f"{Stile.VIOLA}\n[INFO] Le parole di Giulia ti hanno fatto notare un dettaglio sul retro del suo Tablet. Ora puoi provare a decifrarlo nell'Archivio Prove!{Stile.RESET}")
                            
                            # Caso 4: Interrogare Virgilio sulla Domanda 1 sblocca la Serratura dello studio
                            if caso_attuale["titolo"] == "Il Manoscritto Scomparso" and sospettato_attuale == "Virgilio" and scelta_domanda == "1":
                                if not caso_attuale["prove"]["Serratura Elettronica"]["sbloccato_da_azione"]:
                                    caso_attuale["prove"]["Serratura Elettronica"]["sbloccato_da_azione"] = True
                                    print(f"{Stile.VIOLA}\n[INFO] Sentendo i suoi resoconti, hai capito come aggirare la Serratura Elettronica del suo studio. Ora è pronta per la decrittazione!{Stile.RESET}")
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
                        # CONTROLLO SE IL CIFRARIO È STATO SBLOCCATO DAL PERCORSO LOGICO
                        if not info.get("sbloccato_da_azione", True):
                            stampa_errore(info["messaggio_blocco"])
                            continue
                            
                        print(f" {Stile.GIALLO}- Enigma:{Stile.RESET} {info['descrizione']}")
                        print(f" {Stile.ROSSO}- Codice:{Stile.RESET} {info['testo_nascosto']}")
                        tentativo = input(f"\n{Stile.GRASSETTO}Password di sblocco: {Stile.RESET}").lower().strip()
                        
                        if tentativo == info["parola_sblocco"]:
                            stampa_successo("Codice violato!")
                            info["decifrato"] = True
                            print(f" {Stile.VERDE}- Messaggio:{Stile.RESET} {info['descrizione_sbloccata']}")
                            
                            if "sblocca_dialogo" in info:
                                sos, id_d = info["sblocca_dialogo"]
                                caso_attuale["sospettati"][sos]["dialoghi"][id_d]["visibile"] = True
                                print(f"{Stile.VIOLA}{Stile.GRASSETTO}\n[NUOVA DOMANDA SBLOCCATA] Le informazioni decifrate ti aprono una nuova pista con {sos}!{Stile.RESET}")
                        else:
                            stampa_errore("Password errata. Perdi 1 ora.")
                            ore_rimaste -= 1
                    else:
                        print(f" {Stile.VERDE}- Messaggio Decifrato:{Stile.RESET} {info['descrizione_sbloccata']}")
                else:
                    for chiave, valore in info.items():
                        if chiave != "sbloccato_da_azione":
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
                                
                                # --- MECCANICA DI SBLOCCO DECRITTAZIONE DA CRAFTING (Caso 5) ---
                                if dati_comb.get("sblocca_dump_registro"):
                                    caso_attuale["prove"]["Registro Digitale"]["sbloccato_da_azione"] = True
                                    print(f"{Stile.VIOLA}\n[INFO] Grazie alle impronte trovate, i tecnici informatici hanno isolato i log di Leo. Il Registro Digitale è ora pronto per essere forzato nell'Archivio Prove!{Stile.RESET}")

                                if "sblocca_dialogo" in dati_comb:
                                    sos, id_d = dati_comb["sblocca_dialogo"]
                                    caso_attuale["sospettati"][sos]["dialoghi"][id_d]["visibile"] = True
                                    print(f"{Stile.VIOLA}{Stile.GRASSETTO}\n[NUOVA DOMANDA SBLOCCATA] Mettendo insieme i pezzi sulla lavagna hai sbloccato un duro confronto con {sos}!{Stile.RESET}")
                            else:
                                print("Indizi già collegati.")
                            break
                    if not combinazione_trovata:
                        stampa_errore("Nessun legame logico. Perdi 1 ora.")
                        ore_rimaste -= 1

        elif scelta == '5':
            stampa_sottotitolo("ACCUSA FINALE")
            accusa_colpevole = input(f"Chi è il colpevole?: {Stile.RESET}")
            accusa_arma = input(f"Arma/Oggetto usato?: {Stile.RESET}")
            
            if accusa_colpevole.lower().strip() == caso_attuale["soluzione"]["vero_colpevole"] and accusa_arma.lower().strip() == caso_attuale["soluzione"]["arma_del_delitto"]:
                stampa_titolo("CASO RISOLTO!")
                print(f"{Stile.GIALLO}Spiegazione finale:{Stile.RESET} {caso_attuale['soluzione']['spiegazione_finale']}")
                risolto = True
            else:
                stampa_errore("Accusa respinta per incongruenze logiche nelle prove. Perdi 3 ore.")
                ore_rimaste -= 3 
                
        elif scelta == '6': break

if __name__ == "__main__":
    gioca()