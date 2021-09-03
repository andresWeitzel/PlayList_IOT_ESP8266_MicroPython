'''
Info-->
https://www.profetolocka.com.ar/2020/12/15/micropython-conectar-con-una-red-wifi/
https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html
'''
import network
import time as time

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
    
    print("Se ha establecido la Conexión a la Red de Forma Correcta..\n")
    

if not estado_Conexion == True:
    
    print("Intentando Establecer Conexión..\n")
        
    pass


print("Conexión establecida de forma correcta..\n")     
print("('IP', 'MASCARA', 'GATEWAY', 'DNS')-->",conexion_LAN.ifconfig())
