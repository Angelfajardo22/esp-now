# esp-now
# emisor
import network
import espnow
import utime

# Configuración del dispositivo como estación
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()

# Inicialización de ESP-NOW
esp = espnow.ESPNow()
esp.active(True)

# Dirección MAC del receptor (debes reemplazar esto con la dirección MAC real del dispositivo receptor)
peer_mac = b'\xcc\xdb\xa7hd\xa8'  # Reemplaza con la MAC del receptor

# Agregar al receptor como peer
esp.add_peer(peer_mac)

# Función para enviar mensajes
def send_message(message):
    esp.send(peer_mac, message)
    print(f"Mensaje enviado: {message}")

# Ejemplo: alternar mensajes de encender y apagar el LED
while True:
    send_message("ledOn")
    utime.sleep(2)  # Espera 2 segundos
    send_message("ledOff")
    utime.sleep(2)  # Espera 2 segundos
# receptor
import network
import espnow
from machine import Pin
import utime

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()

esp = espnow.ESPNow()
esp.active(True)


led_pin = Pin(2, Pin.OUT)  


print("Esperando mensajes...")

while True:
    host, msg = esp.recv() 
    
    if msg:
        
        message = msg.decode()
        
        if message == "ledOn":
            print("Recibido: encender LED")
            led_pin.value(1)  
        elif message == "ledOff":
            print("Recibido: apagar LED")
            led_pin.value(0)  
    
    utime.sleep(0.1)  
