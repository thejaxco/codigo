import leds
import cay
import hlocal
from sensordht11 import lectura
from time import sleep



contador  = 1
while True:
    cay.client.loop()
    semcay = True
    #data = hlocal.namehora()
    sleep(2)
    valors =lectura()
    print("Lectura:",contador,"Temperatura:",valors[0],"Humedad",valors[1])
    datoHumedad = valors[1]
    if (datoHumedad < 80):
        leds.verde()

    else:
        leds.rojo()
        if semcay:
            cay.cayen(valors)
            semcay = False
            sleep(5)
    contador +=1
