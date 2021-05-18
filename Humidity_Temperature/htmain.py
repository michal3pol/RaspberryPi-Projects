import dht11 #source: https://pypi.org/project/dht11/
import RPi.GPIO as GPIO
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

device = dht11.DHT11(pin = 4)

while True:
    result = device.read()
    if result.is_valid():
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
    else:
        print("Error: %d" % result.error_code)
    time.sleep(3)
    
GPIO.cleanup()