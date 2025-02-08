# main.py
from microdot import Microdot
import json
import random

app = Microdot()

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
   # Simular datos de presión
   def generate_pressure_data():
       return [random.randint(0,100) for _ in range(100)]
       
   data = {
       'left': {
           'talon': generate_pressure_data(),
           'medio': generate_pressure_data(),
           'punta': generate_pressure_data()
       },
       'right': {
           'talon': generate_pressure_data(),
           'medio': generate_pressure_data(), 
           'punta': generate_pressure_data()
       }
   }
   return json.dumps(data)

app.run(host='0.0.0.0', port=8082)
