import  Adafruit_DHT as ADA

def lectura():
    #codi del del sensor dht11 velleman temperatura i humitat
    #print("entro en lectura de sensor....\n")
    sensor = ADA.DHT11
    pin = '4'
    humitat,temperatura =  ADA.read_retry(sensor,pin)
    return temperatura,humitat
