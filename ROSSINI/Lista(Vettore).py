c=0
lista=[]
while True:
    a=input("inserisci un numero, oppure scrivi basta: ")
    if a.upper()!="BASTA":
        c = c + int(a)
        lista.append(int(a))
    else:
        break
print(f"La somma e' {c}")
print("i valori inseriti sono: ")
i=0
while i<len(lista):
    lista[i]=lista[i]*2
    i+=1
i=0
while i<len(lista):
    print(lista[i])
    i+=1
