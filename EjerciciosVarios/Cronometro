import time
horas=int(input("ingrese las horas: "))
while horas<0 or horas>24:
    horas=int(input("ingrese las horas: "))

minutos=int(input("ingrese los minutos: "))
while minutos<0 or minutos>60:
    minutos=int(input("ingrese los minutos: "))

segundos=int(input("ingrese los segundos: "))
while segundos<0 or segundos>60:
    segundos=int(input("ingrese los minutos: "))
#para las horas
for hora in range(0,horas):
    for minuto in range(0,60) :
        for segundo in range(0,60):
            print(hora,":",minuto,":",segundo)
            time.sleep(1)

#para los minutos
for minuto in range(0,minutos):
    for segundo in range(0,60):
        print(horas,":",minuto,":",segundo)
        time.sleep(1)

#para los segundos

for segundo in range(0,segundos+1):
    print(horas,":",minutos,":",segundo)
    time.sleep(1)
