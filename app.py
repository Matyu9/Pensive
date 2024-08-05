from json import load, dumps, loads
from os import path, getcwd
from flask import Flask, jsonify, request, g
from cantinaUtils.Database import DataBase
from time import time

from Cogs.Login.login import login_cogs
from Cogs.User.upload_files import upload_files_cogs

app = Flask(__name__)

UPLOAD_FOLDER = path.abspath(path.join(getcwd(), "images/"))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

file_path = path.abspath(path.join(getcwd(), "config.json"))  # Trouver le chemin complet du fichier config.json

# Lecture du fichier JSON
with open(file_path, 'r') as file:
    config_data = load(file)  # Ouverture du fichier config.json

database = DataBase(
    user=config_data['database'][0]['username'],
    password=config_data['database'][0]['password'],
    host=config_data['database'][0]['address'],
    port=config_data['database'][0]['port'],
    database='cantina_pensive'
)  # Création de l'objet pour se connecter à la base de données via le module cantina
database.connection()  # Connexion à la base de données

database.exec("""CREATE TABLE IF NOT EXISTS cantina_pensive.config(id INT PRIMARY KEY AUTO_INCREMENT, 
name TEXT, content TEXT)""", None)
database.exec("""CREATE TABLE IF NOT EXISTS cantina_pensive.log(id INT PRIMARY KEY AUTO_INCREMENT, 
    action_name TEXT, user_ip TEXT, user_token TEXT, details TEXT, log_level INT)""", None)


@app.before_request
def before_request():
    g.start_time = time()


@app.after_request
def after_request(response):
    latency = time() - g.start_time
    if response.content_type == 'application/json':
        response_json = response.get_json()
        if response_json is not None:
            response_json['latency'] = latency
            response.data = jsonify(response_json).data
            response.content_type = 'application/json'
    else:
        # In case the response is not JSON, add latency in headers
        response.headers["X-Request-Latency"] = str(latency)
    return response


@app.route('/', methods=['GET', 'POST'])
def home():  # put application's code here
    if request.method == "POST":
        print('POST')
        print(request.json)
        return jsonify(message="receive your data bb")
    else:
        return jsonify(message="Hello World!")


@app.route('/login', methods=['POST'])
def login():
    return login_cogs(database, request.args.get('error'))


@app.route('/upload', methods=['POST'])
def upload():
    return upload_files_cogs(database, app)


if __name__ == '__main__':
    app.run()
