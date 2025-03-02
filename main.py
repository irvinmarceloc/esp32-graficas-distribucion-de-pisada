# main.py
from lib.microdot import Microdot
from sensors.pressure import PressureSensor
import json

app = Microdot()
sensor = PressureSensor()  # Inicializar los sensores

@app.route('/')
def index(request):
    with open('static/index.html', 'r') as f:
        html = f.read()
    return html, {'Content-Type': 'text/html'}

@app.route('/static/script.js')
def script(request):
    with open('static/script.js', 'r') as f:
        js = f.read()
    return js, {'Content-Type': 'application/javascript'}

@app.route('/data')
def get_data(request):
    # Leer datos reales de los sensores
    data = sensor.read_all()
    return json.dumps(data)

app.run(host='0.0.0.0', port=8082)
