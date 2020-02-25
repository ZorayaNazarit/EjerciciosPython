#Inicio del modulo
def suma(numero1, numero2):
    resultado = numero1+numero2
    return resultado

def resta(numero1, numero2):
    resultado = numero1-numero2
    return resultado

def multiplicacion(numero1, numero2):
    resultado = numero1*numero2
    return resultado


def division(numero1, numero2):
    if numero2==0:
        return "No se puede dividir por cero"
    else:
        resultado = numero1/numero2
    return resultado

def potencia(base, exponente):
    if(exponente ==0):
        return 1
    else:
        return base*  potencia(base,exponente-1)
#Fin del modelo

import aritmetica


numero1 = float(input("Ingrese el numero 1:"))
numero2 = float(input("Ingrese el numero 2:"))

resultado1 = aritmetica.suma(numero1,numero2)
resultado2 = aritmetica.resta(numero1,numero2)
resultado3 = aritmetica.multiplicacion(numero1,numero2)
resultado4 = aritmetica.division(numero1,numero2)
resultado5 = aritmetica.potencia(numero1,numero2)
print("suma: ",resultado1)
print("resta: ",resultado2)
print("multiplicacion: ",resultado3)
print("division: ",resultado4)
print("potencia: ",resultado5)