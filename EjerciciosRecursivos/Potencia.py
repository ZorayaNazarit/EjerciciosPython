def potencia_recursiva(base, exponente):
    if(exponente ==0):
        return 1
    else:
        return base*  potencia_recursiva(base,exponente-1)


base  = float(input("Ingrese la base:"))
exponente  = float(input("Ingrese el exponente:"))
potencia = potencia_recursiva(base,exponente)

print(base,"^",exponente,"=",potencia)

