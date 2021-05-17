import RPi.GPIO as GPIO
import time
import random

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#diodes
GPIO.setup (20, GPIO.OUT) #redDIODE
GPIO.setup (21, GPIO.OUT) #blueDIODE
GPIO.setup (22, GPIO.OUT) #yellowDIODE
GPIO.output(20, GPIO.LOW)
GPIO.output(21, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
#buttons
GPIO.setup (18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #redBUTTON
GPIO.setup (15, GPIO.IN, pull_up_down=GPIO.PUD_UP) #blueBUTTON
GPIO.setup (14, GPIO.IN, pull_up_down=GPIO.PUD_UP) #yellowBUTTON

round = 1
diodes_in_round = 0
game = True
tab_random = []

while game:
#wyswietlic dotychczasowe:
    tab_gracz = []
    for i in range(0, diodes_in_round):
        GPIO.output(tab_random[i], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(tab_random[i], GPIO.LOW)
        time.sleep(1)
#wylosowac jedna nowa
    losGraWPokera = random.randint(20,22)
    tab_random.append(losGraWPokera)
    diodes_in_round = diodes_in_round + 1
    GPIO.output(losGraWPokera, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(losGraWPokera, GPIO.LOW)
    time.sleep(1)
    
    #for x in tab_losowe:
        #print(x)
    
#gracz
    ilosc_odp_gracza = 0
    while ilosc_odp_gracza < diodes_in_round:
        
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
    for i in range(0, diodes_in_round):
        if(tab_random[i] != tab_gracz[i]):
            game = False 
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(21, GPIO.HIGH)
            GPIO.output(22, GPIO.HIGH)
            print("GAME OVER! Your result: ", round)
            time.sleep(3)
            GPIO.cleanup()
            
    #for x in tab_gracz:
        #print(x)
    if( game == True):
        del tab_gracz
        round = round + 1
        print("Next round: ", round)
        time.sleep(2)
    
GPIO.cleanup()