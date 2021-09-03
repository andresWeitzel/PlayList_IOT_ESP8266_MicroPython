from machine import Pin
import time

led_D0 = Pin(16, Pin.OUT)#D0
led_D1 = Pin(5, Pin.OUT)#D1
led_D2 = Pin(4, Pin.OUT)#D2
led_D5 = Pin(14, Pin.OUT)#D5
led_D6 = Pin(12, Pin.OUT)#D6


'''
En arduino podemos utilizar la funcion sleep en una variables,
en micropython que yo conozca no se puede, entonces creamos
funciones.
'''

def unCuartoDeSegundo():
    
    time.sleep_ms(250)
    
def medioSegundo():
    
    time.sleep_ms(500)
    
def unSegundo():
    
    time.sleep_ms(1000)
    
def dosSegundos():
    
    time.sleep_ms(2000)
    



def encenderApagarTodos():
    
    led_D0.on()
    led_D1.on()
    led_D2.on()
    led_D5.on()
    led_D6.on()
    
    medioSegundo()
    
    led_D0.off()
    led_D1.off()
    led_D2.off()
    led_D5.off()
    led_D6.off()
    
    unCuartoDeSegundo()
    
def encenderApagarSucesivos():
    
    led_D0.on()
    medioSegundo()
    led_D1.on()
    medioSegundo()
    led_D2.on()
    medioSegundo()
    led_D5.on()
    medioSegundo()
    led_D6.on()
    
    dosSegundos()
    
    led_D6.off()
    medioSegundo()
    led_D5.off()
    medioSegundo()
    led_D2.off()
    medioSegundo()
    led_D1.off()
    medioSegundo()
    led_D0.off()
    
    unSegundo()




def encenderApagarSucesivosRapido():
    
    led_D0.on()
    unCuartoDeSegundo()
    led_D1.on()
    unCuartoDeSegundo()
    led_D2.on()
    unCuartoDeSegundo()
    led_D5.on()
    unCuartoDeSegundo()
    led_D6.on()
    
    unSegundo()
    
    led_D6.off()
    unCuartoDeSegundo()
    led_D5.off()
    unCuartoDeSegundo()
    led_D2.off()
    unCuartoDeSegundo()
    led_D1.off()
    unCuartoDeSegundo()
    led_D0.off()
    
    medioSegundo()






while True:
    
    #encenderApagarTodos()
    #encenderApagarSucesivos()
    encenderApagarSucesivosRapido()
    
    