# boot.py
import network
import webrepl

def setup_network():
    # Configurar WiFi
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('tu_ssid', 'tu_password')

    # Esperar conexión
    while not sta_if.isconnected():
        pass
    print('Conectado a WiFi:', sta_if.ifconfig())

def main():
    try:
        setup_network()
        # Iniciar WebREPL directamente sin setup
        webrepl.start(password='tupassword')  # Define una contraseña directamente
        print('WebREPL iniciado')
        
        # Continuar con la instalación de paquetes
        import upip
        print('Instalando paquetes...')
        upip.install('microdot')
        upip.install('micropython-uplot')
        print('Paquetes instalados')
        
    except Exception as e:
        print('Error en setup:', e)

if __name__ == '__main__':
    main()