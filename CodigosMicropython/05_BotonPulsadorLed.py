'''
Info Adicional-->
    https://www.esploradores.com/onebutton/
    https://controlautomaticoeducacion.com/micropython/gpio/
'''

from machine import Pin
import time



botonPulsador = Pin(16, Pin.IN)#D0

led_D1=Pin(5,Pin.OUT)#D1



def delay(miliSegundos):
    
    time.sleep_ms(miliSegundos)



while True:

    if botonPulsador.value() == 0:
        
        print("Pulse el Botón")
       
        led_D1.off()
        
        
    if botonPulsador.value() == 1:
        
        print("Boton Pulsado Correctamente")
        
        led_D1.on()
        