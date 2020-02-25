numero1 = float(input ("Ingrese el primer numero: "))
numero2 = float(input ("Ingrese el segundo numero: "))

if numero2 == pow(numero1,2):
    print("El seguno es el cuadrado exacto del primero")
elif  numero2 < pow(numero1,2):
    print("El segundo es menor que el cuadrado del primero")
elif  numero2 > pow(numero1,2):
    print("El segundo es mayor que el cuadrado del primero")