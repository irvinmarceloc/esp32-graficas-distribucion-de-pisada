# boot.py
import network
import upip

def setup():
    # Instalar librerías
    upip.install('microdot')
    upip.install('micropython-uplot')
    
    # Configurar WiFi
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect('SSID', 'PASSWORD')

setup()
