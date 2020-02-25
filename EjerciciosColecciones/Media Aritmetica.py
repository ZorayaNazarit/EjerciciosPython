numeros = []
for i in range(0,5):
    numero_ingresado= float(input("Ingresa un numero "))
    numeros.append(numero_ingresado)

print(numeros)

suma=0
for i in numeros:
    suma=suma+i
media_aritmetica= suma/len(numeros)
print("La media aritmetica es: ", media_aritmetica)
