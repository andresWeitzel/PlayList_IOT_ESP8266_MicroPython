'''
Info-->
https://www.profetolocka.com.ar/2020/12/15/micropython-conectar-con-una-red-wifi/
https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html
'''
import network, time, urequests, socket

#Instanciamos el objeto de la clase wlan
#Para la interfaz de tipo Station->network.STA_IF
#Para la interfaz de tipo Acces Point->network.AP_IF

conexion_LAN = network.WLAN(network.STA_IF)

#Activamos la interface implementada
conexion_LAN.active(True)

#Estado de la interface
estado_Interface = conexion_LAN.active()

if estado_Interface == True:
    print("Se ha establecido la Conexión con la Interface de Forma Correcta\n")
if estado_Interface == False:
    print("No se ha establecido la Conexión con la Interface de Forma Correcta\n")    



#Nos conectamos a la Red
conexion_LAN.connect("FLIA.WEITZEL","20203030")

#Comprobamos la conexion
estado_Conexion = conexion_LAN.isconnected()

if estado_Conexion == True:
    
   print("Se ha establecido la Conexión a la Red de Forma Correcta\n")

if not estado_Conexion == True:

   print("Intentando Establecer Conexión a la Red..\n")
        
   pass
    
'''
Nos vamos a conectar a un server publico a traves de sockets para traernos datos.
En windows hay que activar el cliente telnet si usamos el puerto 23, en el buscador del sistema
entramos al panel de control--> programas-->programas  y caracteristicas-->Activar o desactivar las
carac. de windows-->marcar cliente telnet-->aceptar
Hay que esperar que se instalen los complementos y listo.
'''

#obtenemos la primera direccion ip valida en el puerto 23 del servidor.
addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)

#cambio de variable
addr = addr_info[0][-1]

#resultado
print(addr)

#Creamos un socket y nos conectamos al server
s=socket.socket()
s.connect(addr)

#Descargamos y mostramos los datos
while True:
     data = s.recv(500)
     print(str(data, 'utf8'), end='')

