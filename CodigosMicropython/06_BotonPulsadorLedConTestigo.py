'''
Info Adicional-->
    https://www.esploradores.com/onebutton/
    https://controlautomaticoeducacion.com/micropython/gpio/
'''

from machine import Pin
import time



botonPulsador = Pin(16, Pin.IN)#D0

led_D1=Pin(5,Pin.OUT)#D1
led_D2=Pin(4,Pin.OUT)#D2


def delay(miliSegundos):
    
    time.sleep_ms(miliSegundos)



def ledTestigo():
     
     for i in range(2):
         
         led_D2.on()
         delay(100)
         led_D2.off()
         delay(100)
 
 
def logica():
    
    flagBotonPulsador=False
      
        
    if botonPulsador.value() == 1:
        
        flagBotonPulsador=True
    
        led_D1.on()
        
    
    if flagBotonPulsador == False:
        
        led_D1.off()
        
        


while True:
    
    ledTestigo()

    logica()
    
