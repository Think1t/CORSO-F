#il programmino organizza in una lista tot elementi finquando non si inserisce la parola basta, poi li stampa
# utilizzando una funzione for;
lista=[] #quando mettiamo "lista=[]" equivale a dichiarare una lista con 0 elementi, che andremo a riempire poi;
i=0      #contatore
while True:
    a=input("inserisci un elemento in lista, oppure scrivi basta: ")
    if a.upper()!="BASTA":   #a.upper() serve per ingrandire i caratteri di una parola, per confrontare meglio con BASTA
        lista.append(a)      #lista.append() inserisce un nuovo elemento in lista
    else:
        break
for i in lista:
    print(i)
