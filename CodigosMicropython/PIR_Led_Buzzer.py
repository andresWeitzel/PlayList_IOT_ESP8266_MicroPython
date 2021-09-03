#https://randomnerdtutorials.com/micropython-interrupts-esp32-esp8266/


#https://www.zonamaker.com/arduino/modulos-sensores-y-shields/sensor-pir-para-la-deteccion-de-presencia
#En el link anteriordiseñar lo mismo con rele y buzzer

#---------LEER ACA---------
#https://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/basics.html#beepers


from machine import Pin, PWM
import time

movimiento = False

def interrupcion(pin):
  
  global movimiento
  movimiento = True
  
  global interrupcionPin
  interrupcionPin = pin
  
  

led01 = Pin(5, Pin.OUT)#D1

sensorPIR = Pin(4, Pin.IN)#D2

buzzer=PWM(Pin(14),freq=440,duty=512)#D5



#El Metodo irq es interrupt request(pedido de interrupcion), seria la señal de un dispositivo hardware
#El trigger es la condicion que se le debe pasar para disparar el metodo

#El Pin.IRQ_FALLING el disparo se produce en el flanco de bajada(pin cambia de 1 a 0)
#El Pin.IRQ_RISING el disparo se produce en el flanco de subida(pin cambia de 0 a 1)

#--Para Interrupciones Externas---
#https://www.profetolocka.com.ar/2020/12/28/micropython-interrupciones-externas-en-el-esp8266/

sensorPIR.irq(trigger=Pin.IRQ_RISING, handler=interrupcion)

while True:
    
  if movimiento:
    
    print('Motion detected! Interrupt caused by:', interrupcionPin)
    
    led01.value(1)
    
    #buzzer.deinit()
    
    time.sleep_ms(2000)
    
    led01.value(0)
    
    buzzer.deinit()
    
    print('Motion stopped!')
    
    movimiento = False
    
