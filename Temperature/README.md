## 1. Temperature with diode/buzzer signalization and console output
Connections:     
Diode - GPIO 12     
Digital thermometer (DS18B20)- GPIO 4     
Buzzer - GPIO 18    
Program measures temperature every 5 seconds, if it's higher than 26 degrees Celsius diode and buzzer signalize it.    
Also we can see actual temperature on the console.    
### Picture
![alt text](https://github.com/michal3pol/RaspberryPi-Projects/blob/main/Temperature/images/image1.jpg) 

## 2. Temperature with exporting data to Excel workbook
Connections:    
Digital thermometer (DS18B20)- GPIO 4     
Program measures temperature every 5 minutes and saves every value to the workbook. The file is named with actual date while program is running.    
In the first column are stored values of temperatures and in the second - hours and minutes of the measure.    
