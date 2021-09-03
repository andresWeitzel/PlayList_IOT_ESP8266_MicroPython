from machine import Pin
import time

led_D0 = Pin(16, Pin.OUT)#D0
led_D1 = Pin(5, Pin.OUT)#D1
led_D2 = Pin(4, Pin.OUT)#D2
led_D5 = Pin(14, Pin.OUT)#D5
led_D6 = Pin(12, Pin.OUT)#D6 TESTIGO

#Eficientizamos a una sola funcion parametrizada

def delay(miliSegundos):
    
    time.sleep_ms(miliSegundos)
    

def ledTestigo():
    
    for i in range(2):
        
        led_D6.on()
        delay(100)
        led_D6.off()
        delay(100)
        
        
        
def encenderApagarSucesivosRapido():
    
    led_D0.on()
    delay(250)
    led_D1.on()
    delay(250)
    led_D2.on()
    delay(250)
    led_D5.on()
    
    delay(1000)
    
    led_D5.off()
    delay(250)
    led_D2.off()
    delay(250)
    led_D1.off()
    delay(250)
    led_D0.off()
    
    delay(500)
        
        
while True:
    
    ledTestigo()
    
    encenderApagarSucesivosRapido()
        

