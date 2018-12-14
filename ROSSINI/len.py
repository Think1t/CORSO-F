#il programmino sfrutta la funzione len, ovvero una specie di contatore di caratteri di una parola o elemento
a="paradossale"
i=0
while i<len(a):  #la while sarà vera finchè la i non raggioungerà il numero len
    print(a[i])  #stamperemo quidi la parola paradossale carattere per carattere
    i+=1
