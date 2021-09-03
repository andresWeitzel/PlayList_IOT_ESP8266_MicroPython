'''
Info Adicional-->
    https://www.esploradores.com/onebutton/
    https://controlautomaticoeducacion.com/micropython/gpio/
'''

from machine import Pin
import time



ledTestigo_D0=Pin(16,Pin.OUT)#D0

botonPulsador_D1 = Pin(5, Pin.IN)#D1
botonPulsador_D2 = Pin(4, Pin.IN)#D2

led_D3=Pin(0,Pin.OUT)#D3
led_D4=Pin(2,Pin.OUT)#D4


def delay(miliSegundos):
    
    time.sleep_ms(miliSegundos)



def ledTestigo():
     
     for i in range(1):
         
         ledTestigo_D0.on()
         delay(100)
         ledTestigo_D0.off()
         delay(100)
 
 
def logica():
    
    flagBotonPulsador_D1=False
    flagBotonPulsador_D2=False
      
        
    if botonPulsador_D1.value() == 1:
        
        flagBotonPulsador_D1=True
    
        led_D3.on()
        
    if botonPulsador_D2.value() == 1:
        
        flagBotonPulsador_D2=True
    
        led_D4.on()    
    
    if flagBotonPulsador_D1 == False:
        
        led_D3.off()
        
    if flagBotonPulsador_D2 == False:
        
        led_D4.off()
        
        


while True:
    
    ledTestigo()

    logica()
    
