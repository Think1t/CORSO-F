import sys
import os# import librerie definizioni
import pickle
lista = []# definizione lista
def stampa_scelte():# funzione per la stampa menu operazioni possibili
    print('Operazioni su lista:')
    print('1.Stampa Lista')
    print('2.Aggiungi elemento alla lista')
    print('3.Elimina elemento dalla lista')
    print('4.Stampa lista su file')
def menu():# funzione che contiene la switch per la scelta delle operazioni da eseguire sulla lista
    scelta = 0
    while scelta != 5:
        os.system('cls')
        stampa_scelte()
        scelta = input('Operazione da eseguire: ')
        if scelta == "1":# stampa menu
            for i in range(len(lista)):
                print(lista[i])
        elif scelta == "2":	# aggiungi elemento alla lista
            elemento = input('Inserisci elemento da inserire nella lista: ')
            lista.append(elemento)# inserisci elemento in fondo alla lista
            lista.sort()# ordina lista

        elif scelta == "3":
            elemento_da_eliminare = input('Inserisci elemento da eliminare nella lista: ')# richiedi in input elemento da eliminare dalla lista
            if elemento_da_eliminare in lista:
                    numero_elemento = lista.index(elemento_da_eliminare)# list index, indice degli elementi della lista
                    del lista[numero_elemento]
            else:
                    print(elemento_da_eliminare, 'non è stato trovato')
        elif scelta == "4":
            # Apre il file C:\binary.dat in scrittura. La lettera r
            # prima del nome file serve a evitare l'escaping
            # del backslash.
            # file_lista = file(r"C:\binary.dat", "w") scrittura list ain binary.dat
            # pickle.dump(lista, file_lista)
            # file_lista.close()
            file_lista = open(r"C:\lista_cepparulo_giacomo.txt", "w")# scrittura lista nel file lista_cepparulo_giacomo.txt
            for n in lista:
                file_lista.write(lista[n])
            file_lista.close()
            print('Lista stampata su file(lista_cepparulo_giacomo.txt)')
        else:
            sys.exit()


menu()
