def descuento_cuatro(total):
    descuento=(4*total)/100
    return descuento
def descuento_diez(total):
    descuento=(10*total)/100
    return descuento

precio = float(input("Ingrese el precio del producto:"))
cantidad = float(input("Ingrese la cantidad del producto:"))

total=cantidad*precio

if cantidad>=6 and cantidad <12:
    totaldescuento=descuento_cuatro(total)
    print("Total de compra: ",total)
    print("Su descuento del 4% fue de:", totaldescuento)
    print("Total a pagar: ",total-totaldescuento)
elif cantidad>=12:
    totaldescuento=descuento_diez(total)
    print("Total de compra: ",total)
    print("Su descuento del 10% fue de:", totaldescuento)
    print("Total a pagar: ",total-totaldescuento)
else:
    print("Total de compra: ",total)
    print("No tiene descuento")
    print("Total a pagar: ",total)