abecedario = "abcdefghijklmnopqrstuvwxyz"
frase = input("Ingese una frase: ")

for i in abecedario:
    contar=0
    for j in frase:
        if i==j:
            contar=contar+1
    if contar == 0:
         print(i, "no esta en la frase")
    else:
        print(i," esta ",contar, "veces")
