# boot.py
import network

def setup_network():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('tu_ssid', 'tu_password')
    
    while not sta_if.isconnected():
        pass
    print('Conectado a WiFi:', sta_if.ifconfig())

if __name__ == '__main__':
    setup_network()