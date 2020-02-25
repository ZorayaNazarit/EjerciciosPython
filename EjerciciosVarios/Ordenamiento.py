from random import randint
def llenar_arreglo(tamano):
    arreglo = []
    for i in range(0,tamano):
        numero = randint(-100,100)
        arreglo.append(numero)
    return arreglo

def copiar_arreglo(arreglo):
    lista=arreglo
    return lista

def mostrar_arreglo(arreglo):
    print(arreglo)

def ordenamientoBurbuja(lista):
    for revisiones in range(len(lista)-1,0,-1):
        for i in range(revisiones):
            if lista[i]>lista[i+1]:
                auxiliar = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = auxiliar
                print(lista)

def ordenamientoSeleccion(lista):
    tamano=len(lista)
    for i in range(0,tamano-1):
        minimo=i
        for j in range(i+1,tamano):
            if lista[minimo] > lista[j]:
                minimo=j
        auxiliar=lista[minimo]
        lista[minimo]=lista[i]
        lista[i]=auxiliar
        print(lista)
    return lista

def ordenamientoInsercion(lista):
    tamano = len(lista)
    for i in range(1,tamano):
        auxiliar=lista[i]
        j=i-1
        while j >= 0 and lista[j] > auxiliar:
            lista[j+1] = lista[j]
            j=j-1
        lista[j+1]=auxiliar
        print(lista)
    return lista


def ordenamientoQuickSort(lista,izquierda,derecha):
    j = derecha
    i = izquierda
    mitad=lista[int((izquierda + derecha)/2)]
    while( i <= j ):
        while lista[i]<mitad and j<=derecha:
            i=i+1
        while mitad<lista[j] and j>izquierda:
            j=j-1
        if i<=j:
            auxiliar = lista[i]
            lista[i] = lista[j]
            lista[j] = auxiliar
            i=i+1
            j=j-1
        if izquierda < j:
            ordenamientoQuickSort( lista, izquierda, j )
    if i < derecha:
        ordenamientoQuickSort( lista, i, derecha );
        print(lista)
    return lista
def menu():
    opcion =int(input (" Ingrese la opción que desea: \n 1.Ordenamiento por burbuja\n 2.Ordenamiento por selección \n 3.Ordenamiento por inserción \n 4. Ordenamiento por quick sort\n" ))
    return opcion


tamano = int(input("De que tamaño desea el arreglo: "))
while tamano<=0:
    tamano = int(input("De que tamaño desea el arreglo: "))


arreglo = llenar_arreglo(tamano)
copia =copiar_arreglo(arreglo)
print(mostrar_arreglo(copia))

eleccion = menu()
if eleccion == 1:
    print("Ordenamiento burbuja")
    print(ordenamientoBurbuja(copia))
elif eleccion == 2:
    print("Ordenamiento por selección")
    print(ordenamientoSeleccion(copia))
elif eleccion == 3:
    print("Ordenamiento por insercion")
    print(ordenamientoInsercion(copia))
elif eleccion == 4:
    print("Ordenamiento por quick sort")
    print(ordenamientoQuickSort(copia,0,len(copia)))
