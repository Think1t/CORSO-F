lista = []
import sys
import os
import pickle
def stampa_scelte():
    print('Operazioni su lista:')
    print('1.Stampa Lista')
    print('2.Aggiungi elemento alla lista')
    print('3.Elimina elemento dalla lista')
    print('4.Stampa lista su file')
def menu():
    scelta = 0
    while scelta != 5:
       
        stampa_scelte()
        scelta = input('Operazione da eseguire: ')
        if scelta == 1:
            for n in lista:
                print(lista[n])
        if scelta == 2:
            elemento = input('Inserisci elemento da inserire nella lista: ')
            list.append(elemento)
        if scelta == 3:
            elemento_da_eliminare = input('Inserisci elemento da eliminare nella lista: ')
            if elemento_da_eliminare in lista:
                    numero_elemento = list.index(elemento_da_eliminare)
                    del lista[numero_elemento]
            else:
                    print(elemento_da_eliminare, 'non è stato trovato')
        if scelta == 4:
            # Apre il file C:\binary.dat in scrittura. La lettera r
            # prima del nome file serve a evitare l'escaping
            # del backslash.
            file_lista = file(r"C:\binary.dat", "w")
            pickle.dump(lista, file_lista)
            file_lista.close()
            file_lista = file(r"C:\lista_cepparulo_giacomo.txt", "w")
            for n in lista:
                file_lista.write(lista[n])
            file_lista.close()
            print('Lista stampata su file(lista_cepparulo_giacomo.txt)')
    sys.exit()

menu()