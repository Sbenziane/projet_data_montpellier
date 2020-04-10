from typing import List, Dict
from flask import Flask
from flask_cors import CORS

from urllib import request
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def index() -> str:
	return "hello"
	
@app.route('/monuments-historiques')
def monuments_historiques():
	res = request.urlopen('https://data.montpellier3m.fr/sites/default/files/ressources/VilleMTP_MTP_MonumentsHist.geojson').read()
	return json.loads(res.decode('utf_8'))
	
@app.route('/aires-de-jeux')
def aires_de_jeux():
	res = request.urlopen('https://data.montpellier3m.fr/sites/default/files/ressources/VilleMTP_MTP_AiresJeux.geojson').read()
	return json.loads(res.decode('utf_8'))
	
@app.route('/lieux-enseignements')
def lieux_enseignements():
	res = request.urlopen('https://data.montpellier3m.fr/sites/default/files/ressources/VilleMTP_MTP_Enseignements.geojson').read()
	return json.loads(res.decode('utf_8'))

@app.route('/hopitaux-clinique')
def hopitaux_clinique():
	res = request.urlopen('https://data.montpellier3m.fr/sites/default/files/ressources/OSM_Montpellier_hopital_point.json').read()
	return json.loads(res.decode('utf_8'))
	

if __name__ == '__main__':
    app.run(host='0.0.0.0')