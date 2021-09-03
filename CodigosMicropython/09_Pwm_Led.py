#https://randomnerdtutorials.com/esp8266-pwm-arduino-ide/
from machine import Pin, PWM
import time

frecuencia = 5000 #valor entre 0 y 78125

led_D1 = Pin(5, Pin.OUT)#D1/IO5
led_D3 = PWM(Pin(0), frecuencia)#D3/IO0


def delay(miliSegundos):
    time.sleep_ms(miliSegundos)

def ledTestigo():
    
    for i in range(3):
        led_D1.on()
        delay(200)
        led_D1.off()
        delay(200)
        
        

while True:
    
  ledTestigo()  
    
  for cicloDuty in range(0, 1024):
    
    led_D3.duty(cicloDuty)
    
    delay(5)
  
  delay(200)