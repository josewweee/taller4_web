import importlib

importlib.reload(sys.modules['azure'])

from flask import Flask, jsonify, request, render_template
import requests
 
app = Flask(__name__, template_folder='templates')
 
variables_list = ['Sensor en terreno', 'Imagen satelital', 'Imagen dron', 'Dato derivado']


@app.route('/crearSensor', methods=['GET'])
def crearSensor():
    return render_template('crearSensor.html', variables=variables_list) 

@app.route('/listarSensores', methods=['GET'])
def listarSensores():
    sensores_list = requests.get('https://api-evergreen-535.azurewebsites.net/mediciones').json()
    return render_template('listarSensores.html', mediciones=sensores_list)


@app.route('/guardarSensor', methods=['POST'])
def guardarSensor():
        medicion = dict(request.values)
        medicion['valor'] = int(medicion['valor'])
        requests.post('https://api-evergreen-535.azurewebsites.net/mediciones',json=medicion)
        return (listarSensores())
        
        
#PUERTO Y AUTORUN
''' quitamos el app run para que la app corra en azure '''
''' app.run(port=8000,debug=True) '''