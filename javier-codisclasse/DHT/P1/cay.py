import cayenne.client
MQTT_USERNAME = "47ad72e0-7c78-11e9-beb3-736c9e4bf7d0"
MQTT_PASSWORD = "9587f4901efd855c64484e9fc554e78c9755917f"
MQTT_CLIENT_ID = "908732d0-7c78-11e9-be3b-372b0d2759ae"
client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)


def cayen(valores):

    #enviar datos a cayenne. no necesita return
    print('\nConectando con CAYENNE\n',"VALORES SUBIDOS:",valores,"\n")
    client.virtualWrite(1,valores[0])
    client.virtualWrite(2,valores[1])
