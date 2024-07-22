from json import load
from os import path, getcwd
from flask import Flask, jsonify, request
from cantinaUtils.Database import DataBase


app = Flask(__name__)

file_path = path.abspath(path.join(getcwd(), "config.json"))  # Trouver le chemin complet du fichier config.json

# Lecture du fichier JSON
with open(file_path, 'r') as file:
    config_data = load(file)  # Ouverture du fichier config.json

database = DataBase(
    user=config_data['database'][0]['username'],
    password=config_data['database'][0]['password'],
    host=config_data['database'][0]['address'],
    port=config_data['database'][0]['port'],
    database='cantina_administration'
)  # Création de l'objet pour se connecter à la base de données via le module cantina
database.connection()  # Connexion à la base de données


@app.route('/', methods=['GET', 'POST'])
def home():  # put application's code here
    if request.method == "POST":
        print('POST')
        print(request.json)
        return jsonify(message="receive your data bb")
    else:
        return jsonify(message="Hello World!")


@app.route('/', methods='POST')
def login():
    pass


if __name__ == '__main__':
    app.run()
