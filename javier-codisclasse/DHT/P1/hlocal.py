from datetime import datetime
# Esta funcion se encarga de enviaar la hora con el formato:
# 12-37-49_29-05-2019

def hora():
    ahora = datetime.now()
    salida = "{:%H-%M-%S_%d-%m-%Y}".format(ahora)
    #print(salida)
    return salida


def minuto():
    ahora = hora()
    salida = ahora[3:5]
    #print(salida)
    return salida


def segundo():
    ahora = hora()
    salida = ahora[6:8]
    #print(salida)
    return salida


def namehora():
    ahora = datetime.now()
    salida = "{:%H-%M-%S_%d-%m-%Y}".format(ahora)
    salida = salida +'-dht11.png'
    return salida
