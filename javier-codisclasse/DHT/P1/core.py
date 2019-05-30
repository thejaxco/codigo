from graficar import grafic
from time import sleep
from sensordht11 import lectura
import cay
import hlocal




print("Iniciando el programa...\n")
comptador  = 1
temperatura=[]
humitat=[]



while True:
    cay.client.loop()
    sleep(1)
    data = hlocal.namehora()
    print("Realizando Lectura:",comptador)
    valors =lectura()
    temperatura.append(valors[0])
    humitat.append(valors[1])
    print("Temperatura:",valors[0],"Humedad",valors[1],"\n","\n")
    comptador += 1 # comptador = comptador +  1
    #print("data:",data,"\n")


    if (comptador == 11):
        grafic(temperatura, humitat,data) # ara mateix te 10 valors
        cay.cayen(valors)
        comptador = 1
        temperatura=[]
        humitat=[]
sleep(1)
