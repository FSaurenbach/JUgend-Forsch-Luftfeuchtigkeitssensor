import time
import board
import adafruit_dht
from datetime import datetime
sensor1 = adafruit_dht.DHT11(board.D23)
sensor2 = adafruit_dht.DHT11(board.D24)


def is_time(): # Alle x Minuten die Daten auslesen.
	now = datetime.now()
	current_minute = now.strftime("%M")
	print(current_minute)
	if "0" in current_minute or "5" in current_minute:
		print("It is time")
		return True
	else:
		return False


while True:
    if is_time():
        humidity1 = sensor1.humidity
        humidity2 = sensor2.humidity
        print(" Humidity Sensor1: {}% ".format(humidity1))
        print(" Humidity Sensor2: {}% ".format(humidity2))
        with open("Sensor1.txt", "a") as f:
            f.write("\n")
            now = datetime.now()
            current_minute = now.strftime("%H:%M")
            f.write(current_minute + " ," + str(humidity1) + "," + str(humidity2))
        
        time.sleep(120)
    time.sleep(20)
