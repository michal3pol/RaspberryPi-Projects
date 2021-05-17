import RPi.GPIO as GPIO
import time
import random

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#diody
GPIO.setup (20, GPIO.OUT) #redDIODE
GPIO.setup (21, GPIO.OUT) #blueDIODE
GPIO.setup (22, GPIO.OUT) #yellowDIODE
GPIO.output(20, GPIO.LOW)
GPIO.output(21, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
#przyciski
GPIO.setup (18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #redBUTTON
GPIO.setup (15, GPIO.IN, pull_up_down=GPIO.PUD_UP) #blueBUTTON
GPIO.setup (14, GPIO.IN, pull_up_down=GPIO.PUD_UP) #yellowBUTTON

runda = 1
diodWRundzie = 0
nieprzegrales = True
tab_losowe = []

while nieprzegrales:
#wyswietlic dotychczasowe:
    tab_gracz = []
    for i in range(0, diodWRundzie):
        GPIO.output(tab_losowe[i], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(tab_losowe[i], GPIO.LOW)
        time.sleep(1)
#wylosowac jedna nowa
    losGraWPokera = random.randint(20,22)
    tab_losowe.append(losGraWPokera)
    diodWRundzie = diodWRundzie + 1
    GPIO.output(losGraWPokera, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(losGraWPokera, GPIO.LOW)
    time.sleep(1)
    
    #for x in tab_losowe:
        #print(x)
    
#gracz
    ilosc_odp_gracza = 0
    while ilosc_odp_gracza < diodWRundzie:
        
        buttonREDState = GPIO.input(18)
        if buttonREDState == False:
            GPIO.output(20, GPIO.HIGH)
            ilosc_odp_gracza = ilosc_odp_gracza + 1
            tab_gracz.append(20)
            time.sleep(0.5)
            GPIO.output(20, GPIO.LOW)
        else:
            GPIO.output(20, GPIO.LOW)
        
        buttonBLUEState = GPIO.input(15)
        if buttonBLUEState == False:
            GPIO.output(21, GPIO.HIGH)
            ilosc_odp_gracza = ilosc_odp_gracza + 1
            tab_gracz.append(21)
            time.sleep(0.5)
            GPIO.output(21, GPIO.LOW)
        else:
            GPIO.output(21, GPIO.LOW)
        
        buttonYELLOWState = GPIO.input(14)
        if buttonYELLOWState == False:
            GPIO.output(22, GPIO.HIGH)
            ilosc_odp_gracza = ilosc_odp_gracza + 1
            tab_gracz.append(22)
            time.sleep(0.5)
            GPIO.output(22, GPIO.LOW)
        else:
            GPIO.output(22, GPIO.LOW)

#sprawdzenie odpowiedzi
    for i in range(0, diodWRundzie):
        if(tab_losowe[i] != tab_gracz[i]):
            nieprzegrales = False 
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(21, GPIO.HIGH)
            GPIO.output(22, GPIO.HIGH)
            print("Przegrales! Rundy: ", runda)
            time.sleep(3)
            GPIO.cleanup()
            
    #for x in tab_gracz:
        #print(x)
    if( nieprzegrales == True):
        del tab_gracz
        runda = runda + 1
        print("Przed toba runda: ", runda)
        time.sleep(2)
    
GPIO.cleanup()