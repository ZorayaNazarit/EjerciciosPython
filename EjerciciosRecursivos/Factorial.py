def factorial(numero):
    if(numero ==0):
        return 1
    else:
        return numero* factorial(numero-1)


numero  = float(input("Ingrese un número: "))

factorialResutado = factorial(numero)

print("El factorial de ",  numero, " es ",factorialResutado)
