# Questo programma legge 3 numeri interi e stampa il maggiore, il minore ed esegue la media

import math
import os

input_1 = input('Inserisci il primo valore intero: ')   # Inserimento del primo valore
try:
    N1 = int(input_1)
except ValueError:
    print("Il valore non è intero") # Errore che indica che il valore non è intero
    os._exit(1)

input_2 = input('Inserisci il secondo valore intero: ') # Inserimento del secondo valore
try:
    N2 = int(input_2)
except ValueError:
    print("Il valore non è intero")
    os._exit(1)

input_3 = input('Inserisci il terzo valore intero: ')   # Inserimento del terzo valore
try:
    N3 = int(input_3)
except ValueError:
    print("Il valore non è intero")
    os._exit(1)

print('Il maggiore tra i valori è: ')
if N1>N2:   # Controlli per trovare il maggiore tra i valori
    if N1>N3:
            print (str(N1)) # Restituisce il primo valore
    else:
            print (str(N3)) # Restituisce il terzo valore
else:
    if N2>N3:
            print (str(N2)) # Restituisce il secondo valore
    else:
            print (str(N3)) # Restituisce il terzo valore
print('Il minore tra i valori è: ')
if N1<N2:
    if N1<N3:
        print (str(N1))
    else:
        print (str(N3))
else:
    if N2<N3:
        print (str(N2))
    else:
        print (str(N3))
print('La media è: ')
media= (N1+N2+N3)/3 # Calcolo della media
print (str(media))  # Restituisce la media