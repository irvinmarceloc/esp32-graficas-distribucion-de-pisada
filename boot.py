# boot.py
import network
import webrepl_setup

def setup_network():
   # Configurar WiFi
   sta_if = network.WLAN(network.STA_IF)
   sta_if.active(True)
   sta_if.connect('tu_ssid', 'tu_password')

   # Esperar conexión
   while not sta_if.isconnected():
       pass
   print('Conectado a WiFi:', sta_if.ifconfig())

def install_packages():
   # Una vez conectado, importar e instalar paquetes
   import upip
   print('Instalando paquetes...')
   upip.install('microdot')
   upip.install('micropython-uplot')
   print('Paquetes instalados')

def main():
   try:
       setup_network()
       install_packages()
       # Configurar WebREPL
       webrepl_setup.start()
   except Exception as e:
       print('Error en setup:', e)

if __name__ == '__main__':
   main()