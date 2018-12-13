#importo i moduli
import sqlite3
import string
import sys
import itertools as it
import operator
from functools import partial
from datetime import date

MESI = "ABCDEHLMPRST"
DISPARI = [1, 0, 5, 7, 9, 13, 15, 17, 19, 21, 2, 4, 18,
           20, 11, 3, 6, 8, 12, 14, 16, 10, 22, 25, 24, 23]
ORD_0 = ord("0")
ORD_A = ord("A")

vocale_pred = partial(operator.contains, set("AEIOUÀÈÉÌÒÙ"))

#calcolo del carattere di controllo (16 carattere)
#calcolo della somma per i valori pari
def pari(char):
    return ord(char) - (ORD_0 if char.isdigit() else ORD_A)
#calcolo della somma per i valori dispari
def dispari(char):
    return DISPARI[ord(char) - (ORD_0 if char.isdigit() else ORD_A)]
#somma con il resto
def calcola_ultimo_carattere(resto):
    return chr(ORD_A + resto)


def suddivisione(pred, iterable):
    suddivisioni = [], []
    for element in iterable:
        suddivisioni[int(pred(element))].append(element)
    return suddivisioni
#funzione che raccoglie i dati in ingresso e ne verifica la validità
def leggi_dati():
    if 1 < len(sys.argv) < 6:
        exit("Numero di parametri insufficiente")
    elif len(sys.argv) == 1:
        nome = input("Inserisci il tuo Nome: ")
        cognome = input("Ora il tuo Cognome: ")
        sesso = input("Sesso (M/F)> ")
        data = input("Data di nascita nel formato (gg/mm/aaaa)> ")
        comune = input("Comune di nascita> ")
    else:
        nome, cognome, sesso, data, comune = sys.argv[1:]
    try:
        giorno, mese, anno = map(int, data.split("/"))
        data = date(anno, mese, giorno)
    #gestione dell'ecccezione
    except ValueError:
        pass
    #riporto cognome, nome, data, sesso, comune
    return cognome, nome, data, sesso, comune

#codifica del nome
def codifica_nome(nome, is_cognome=True):
	#rende il nome maiuscolo e toglie gli spazi
    nome = nome.upper().replace(" ", "")

    consonanti, vocali = suddivisione(vocale_pred, nome)
    #gestisce l'eccezione dell'input con consonanti maggiori di 3
    if not is_cognome and len(consonanti) > 3:
        del consonanti[1]

    nome = "".join(consonanti + vocali)[:3]
    return nome.ljust(3, "X")

#codifica della data di nascita
def codifica_data(data, sesso):
    offset = 40 if sesso in "fF" else 0
    return "{:>02}{}{:>02}".format(data.year % 100,
                                   MESI[data.month - 1],
                                   data.day + offset)

#codifica del comune
def codifica_comune(nome_comune):
    try:
        nome_comune = nome_comune.upper()
        #Connessione al database attraverso il modulo sqlite3
        conn = sqlite3.connect("Database_Comuni.db")
        #imposto la query dove seleziona il codice del comune
        result_set = conn.execute("select code from comuni where name = ?", [nome_comune])
        #Inserisce il codice del comune nella variabile result
        result = result_set.fetchone()
        return result[0]
    except:  # gestione dell'eccezione nel caso in cui il comune non è stato trovato o non sia stata possibile la connessione al database
        print("Connessione al Database non riuscita / Comune Inesistente")

#calcolo del codice di controllo (l'ultima lettera del codice fiscale)
def calcola_codice_controllo(code):
	#Convertire in numeri i caratteri di posizione dispari
    acc_d = sum(dispari(x) for x in code[::2])
    #Conversione in numeri i caratteri di posizioni pari
    acc_p = sum(pari(x) for x in code[1::2])
    #divisione per 26
    return calcola_ultimo_carattere((acc_d + acc_p) % 26)

#calcolo del codice fiscale finale
def calcola_cf(cognome, nome, data, sesso, comune):
    codice = "{}{}{}{}".format(codifica_nome(cognome),
                               codifica_nome(nome, is_cognome=False),
                               codifica_data(data, sesso),
                               codifica_comune(comune))
    return "".join([codice, calcola_codice_controllo(codice)])



#definisco il main e richiamo le funzioni
def main():
    print("Benvenuti nel programma Calcolo Codice Fiscale \nInserisci Nome, Cognome, Sesso, Data e Comune di Nascita")
    #richiamo la funzione leggi_dati che popola un array con i dati dell'utente
    dati = leggi_dati()
    #stampa codice fiscale
    fmt = "{} {}, il tuo codice fiscale e'..."
    print(fmt.format(dati[1].capitalize(),
                     dati[0].capitalize()))
    print(calcola_cf(*dati))
    input()


if __name__ == "__main__":
    main()
