file= "C:/Users/win10/Documents/CodigoASCII.txt"
archivo = open(file,'r')
archivo.seek(1)
for linea in archivo.readlines():
    print(linea)
archivo.close()
