import time  # Zeit modul um eine bestimmte Zeit den Code zu stoppen.
import board  # Board modul von "adafruit_dht" um auf die RaspberryPi Pins zuzugreifen.
import adafruit_dht  # Modul "adafruit_dht" um auf die Luftfeuchtigkeitssensoren zuzugreifen.
from datetime import \
    datetime  # Zeit modul um auf aktuelle Zeit in der Datenbank mit den Feuchtigkeitswerten abzuspeichern.

sensor1 = adafruit_dht.DHT11(board.D23)  # Auf Sensor 1 zugreifen der an dem Pin 23 hängt.
sensor2 = adafruit_dht.DHT11(board.D24)  # Auf Sensor 2 zugreifen der an dem Pin 24 hängt.


def is_time():  # Alle 5 Minuten die Daten auslesen.
    current_minute = datetime.now().strftime("%M")
    if "0" in current_minute or "5" in current_minute:
        print("It is time")
        return True
    else:
        return False


while True:
    if is_time():
        humidity1 = sensor1.humidity  # Die Feuchtigkeit mit dem adafruit modul ablesen
        humidity2 = sensor2.humidity
        print(" Humidity Sensor1: {}% ".format(humidity1))
        print(" Humidity Sensor2: {}% ".format(humidity2))
        with open("Sensor1.txt", "a") as f:
            f.write("\n")  # Neue Zeile
            current_minute = datetime.now().strftime("%H:%M")
            f.write(current_minute + " ," + str(humidity1) + "," + str(humidity2))

        time.sleep(120)
    time.sleep(20)
