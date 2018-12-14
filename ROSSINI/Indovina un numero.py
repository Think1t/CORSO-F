#Versione nuova
#il programmino chiede di indovinare un numero e attraverso vari controlli ti "aiuta"
while True:
    a = int(input("Inserisci il numero da indovinare da 1 a 100: "))
    if a<1 or a>100:
        print("Numero non valido, riprova;")
    else:
        break
i=0
while i<=100:
    print("")
    i+=1
print("\n"*100)
i=0
lista=[]
while i<5:
    b=0
    while b<1 or b>100:
        b = int(input("Indovina il numero hai " + str(5 - i) + " tentativi"))
        if b < 1 or b > 100:
            print("Numero non valido, riprova;")
    lista.append(int(b))
    if b==a:
        print("Bravo, hai indovinato in "+ str(i+1)+ " tentativi")
        break
    elif b>a:
        print("Il numero da indovinare e' minore di "+ str(b))
    else:
        print("Il numero da indovinare e' maggiore di " + str(b))
    i+=1
    print("")
    print("")
if a!=b:
    print("Non hai indovinato, peccato.")
i=0
print("Questi sono i tuoi tentativi:")
for i in lista:
    print(i)


#########################################                        #######################################################
#########################################     vecchia versione   #######################################################
#########################################                        #######################################################
#a=int(input("Inserisci il numero da indovinare "))
#b=a-1
#while a!=b:
#    b = int(input("Indovina il numero : "))
#    if a==b:
#        print("E' giusto")
#    else:
#        print("E' sbagliato")
