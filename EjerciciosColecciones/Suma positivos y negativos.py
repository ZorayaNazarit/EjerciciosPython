suma_negativos=0
suma_positivos=0
numeros = [2,3,-1,-4,6,-8,6,7,-9,12,6]
for i in numeros:
    if(i>=0):
        suma_positivos= suma_positivos+i
    else:
        suma_negativos= suma_negativos+i


print("Suma positivos: ", suma_positivos)
print("Suma negativos: ", suma_negativos)