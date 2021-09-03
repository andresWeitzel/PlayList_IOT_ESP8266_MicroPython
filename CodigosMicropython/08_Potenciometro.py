#https://randomnerdtutorials.com/esp32-esp8266-analog-readings-micropython/
#https://www.profetolocka.com.ar/2020/12/23/micropython-leyendo-el-conversor-a-d-del-esp8266/
from machine import ADC, Pin
import time


pot = ADC(0)

#Probando con el Led Interno me surgieron algunos errores
#decidi trbajar con uno fisico, no logico
led_D1 = Pin(5, Pin.OUT)#D1/IO5



def delay(miliSegundos):
    time.sleep_ms(miliSegundos)

def ledTestigo():
    
    for i in range(3):
        led_D1.off()
        delay(500)
        led_D1.on()
        delay(500)



while True:
    
  ledTestigo()  
    
  pot_valor = pot.read()
  
  tension = (pot_valor/1023)*(320/100)
  
  print("Valor Potenciometro:",pot_valor," | Tensión:",tension)
  
  delay(200)