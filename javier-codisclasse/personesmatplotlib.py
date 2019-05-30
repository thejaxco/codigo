from funcauxi import grafic,lectura,sleep

llistapersones = []
minuts = 0
while minuts  < 10:
    persones = 0
    for segons in range(60):
        persones += lectura()
        sleep(1)
        print("personas:",persones)
    llistapersones.append(persones)
    minuts +=1
print("total:",llistapersones)
grafic(llistapersones)
