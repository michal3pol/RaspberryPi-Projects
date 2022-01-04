import dht11 #source: https://pypi.org/project/dht11/
from rpi_lcd import LCD #source https://pypi.org/project/rpi-lcd/
import RPi.GPIO as GPIO
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

device = dht11.DHT11(pin = 4)
lcd = LCD()

try:
    while True:
        result = device.read()
        if result.is_valid():
            temperature = str(result.temperature)
            humidity = str(result.humidity)
            lcd.text("Temp: " + temperature + " C", 1);
            lcd.text("Humidity: " + humidity + " %", 2);
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
        else:
            print("Error: %d" % result.error_code)
        time.sleep(10)

except KeyboardInterrupt:
    pass

finally:       
    GPIO.cleanup()
    lcd.clear()
