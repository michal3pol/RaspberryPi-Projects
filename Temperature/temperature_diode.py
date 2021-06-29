import RPi.GPIO as GPIO
import time
import w1thermsensor
import pandas

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

print('Wykonywanie pomiarow temperatury')
#czujnik_temp
sensor = w1thermsensor.W1ThermSensor()
#dioda
GPIO.setup (12, GPIO.OUT)
#buzzer
GPIO.setup(18, GPIO.OUT, initial=GPIO.HIGH)

try:
    while True:
        temperatura = sensor.get_temperature()
        if(temperatura <26):
            print(temperatura)
            GPIO.output(12, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(12, GPIO.LOW)
            time.sleep(4.8)
        if(temperatura >26):
            print(temperatura)
            for i in range(1,6):
                GPIO.output(12, GPIO.HIGH)
                GPIO.output(18, GPIO.LOW)
                time.sleep(0.2)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(18, GPIO.HIGH)
                time.sleep(0.2)
            print('Zbyt wysoka temperatura!')
            time.sleep(3)

except KeyboardInterrupt:
    print('Koniec')
    GPIO.cleanup()
            
            
