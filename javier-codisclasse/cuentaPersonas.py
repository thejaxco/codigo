from funcauxi import lectura,sleep
import cayenne.client





def cayen(valores):
    #enviar datos a cayenne. no necesita return
    #print('\ntotal\n',valores)
    client.virtualWrite(1,valores)


#esta funcion retorna 0 o 1 en funcion que pase o no una persona
#hacemos la suposicion que en 1 segundo solo pasa una persona


#Autenticacion en cayenne
MQTT_USERNAME = "47ad72e0-7c78-11e9-beb3-736c9e4bf7d0"
MQTT_PASSWORD = "9587f4901efd855c64484e9fc554e78c9755917f"
MQTT_CLIENT_ID = "55e45d60-7c78-11e9-9636-f9904f7b864b"
client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)




#El programa enviara datos a cayenne cada minuto

while True:
    client.loop()
    personas = 0
    for segundos in range(60):
<<<<<<< HEAD
        personas += distancia()
        #print('Segundo:',segundo,'personas:',personas)
        sleep(1)

    cayen(personas)

=======
        personas += lectura()
        print('Segundo:',segundos,'personas:',personas)
        sleep(1)

    cayen(personas)
    #sleep(5)#este es para pruebas
>>>>>>> 6a11b55d7573dc04c5d2385e7a0dc2105fb12047
