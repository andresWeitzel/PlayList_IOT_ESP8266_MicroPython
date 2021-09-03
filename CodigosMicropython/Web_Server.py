#Referencia-->https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/

#------------------Librerias----------------

#Podriamos importar directamente socket, pero usocket es una api mas completa
import usocket as socket

#Importamos la api de red, para conectarnos a una red WIFI
import network

from machine import Pin

import time

#Desactivamos los msj de depuracion del Sist. Op del proveedor, menos procesamiento, mas rapido
import esp
esp.osdebug(None)

#Recolector de elementos, limpieza de objetos no utilizados mas en memoria, por
#ende ahorro de espacio en memoria flash
import gc
gc.collect()

#------------------Fin Librerias----------------

#------------------Pines----------------
led=Pin(2, Pin.OUT)#D4
#------------------Fin Pines----------------

#------------------Conexion Wifi e Interfaz-----------------

ssid = 'FLIA.WEITZEL'
password = '20203030'

station = network.WLAN(network.STA_IF)

station.active(True)

station.connect(ssid, password)

#------------------Fin Conexion Wifi e Interfaz-----------------

#---------------Testeamos la conexion wifi y la Interfaz----------------


#Estado de la interface
estado_Interface = station.active()

if estado_Interface == True:
    print("Se ha establecido la Conexión con la Interface de Forma Correcta..\n")
if estado_Interface == False:
    print("No se ha establecido la Conexión con la Interface de Forma Correcta..\n")    
#while not estado_Interface == True:
    #print("Intentando establecer la Conexión con la Interface..\n")    


#Comprobamos la conexion
estado_Conexion = station.isconnected()

if estado_Conexion == True:
        
    print("Se ha establecido la Conexión a la Red de Forma Correcta..\n")

if not estado_Conexion == True:
        
    print("No se ha establecido la Conexión a la Red de Forma Correcta..\n")
    
    pass

#while not estado_Conexion == True:
        
    #print("Intentando Establecer Conexión a la Red..\n")
    
    #pass

print("Se ha establecido la Conexión a la Red de Forma Correcta\n")        
print("('IP', 'MASCARA', 'GATEWAY', 'DNS')-->",station.ifconfig())


#---------------Fin Testeo de la conexion wifi y la interfaz----------------



#------------------Creacion Socket----------------------

#Creamos un socket de escucha para escuchar las solicitudes entrantes y enviar texto html en respuesta

#Especificamos el tipo de socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#con .bind enlazamos el socket a una direccion de red y puerto, al trabajar en localhost es vacia, sino
#le pones la direc ip de tu server
s.bind(('', 80))

#con .listen le indicamoss al server que escuche conexiones, indicamos el numero maximo de conexion en cola(5)
s.listen(5)

#------------------Fin Creacion Socket----------------------

#---------------Formato de la Página Web--------------

#La página web muestra el estado GPIO actual. Por lo tanto, antes de generar el texto HTML, tenemos que
#comprobar el estado del LED. Guardamos su estado en el gpio_state variable:

def web_page():

  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
    
  html ="""
  <html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
  <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
 
  return html

#---------------Fin Formato de la Página Web--------------








while True:

  
  #---------------Conexion Socket y Manejo de datos----------------------
  
  #Cuando se establezca una conexion se guarda el nuevo objeto socket para enviar datos con la variable conn y
  #guardamos la direccion ip del cliente para la conexion en el server con la variable addr
  conn, addr = s.accept()
  
  #Imprimimos la direccion del cliente
  print('Conexión Establecida de %s' % str(addr))
  
  #Guardamos la solicitud recibida del cliente en el socket, con .recv y 1024 es el numero max de bits que se
  #puede recibir por vez
  request = conn.recv(1024)
  
  #Convertimos a cadena de texto 
  request = str(request)
  
  #Imprimimos el contenido de la solicitud
  print('Content = %s' % request)
  
  
  led_on = request.find('/?led=on')
  
  led_off = request.find('/?led=off')
  
  if led_on == 6:
    print('LED ON')
    led.value(1)
  
  if led_off == 6:
    print('LED OFF')
    led.value(0)
    
  #Almacenamos el texto html devuelto por la pagina web  
  response = web_page()
  
  #enviamos la respuesta del cliente socket mediante los siguientes metodos
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  
  #Cerramos la conexion
  conn.close()
  
  #---------------Conexion Socket y Manejo de datos----------------------


