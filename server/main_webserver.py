from os import name
from flask import Flask, request
from flask_cors import CORS, cross_origin
from main import Processe
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def index():
    return str(request.form.get('fname'))

@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    password = request.form.get('password')
    user = request.form.get('username')
    if Processe().login_check(str(user),str(password)):
        return json.dumps({"token":str(user)}, indent = 4)
    else:
        return json.dumps({"token":""}, indent = 4)


@app.route('/registrieren', methods=['POST'])
@cross_origin()
def registrieren():
    password = request.form.get('password')
    user = request.form.get('username')
    print(user, password)
    if Processe().registrieren(user,password):
        return "Registriert"
    else:
        return "ERROR"

@app.route('/<name>/new', methods = ['GET']) #fast fertig
@cross_origin()
def new(name):
        if request.method == 'GET':
            print(name)
            datei = Processe().random_choose_profile(str(name))
            
            datei.update({"token":name})
            return json.dumps(datei, indent = 4)


@app.route('/<name>/all', methods = ['GET']) #fast fertig
@cross_origin()
def all(name):
    datei = Processe().get_all_profiles(str(name))
    return json.dumps(datei, indent = 4)



@app.route('/<name>/info', methods = ['POST', 'GET']) #fast fertig
@cross_origin()
def info(name):
    if str(name) == "default":
        print("default")
        datei = Processe().random_choose_profile(str(name))
        datei.update({"token":name})
        return json.dumps(datei, indent = 4)
    elif request.method == 'GET':
        print(name)
        datei = Processe().get_profile_from_ID(Processe().get_ID_from_username(str(name)))
        datei.update({"token":name})
        return json.dumps(datei, indent = 4)
    else:
        datei = Processe().random_choose_profile()
        print(datei)
        Processe().set_ID_to_username(str(name),datei["ID"])
        datei = Processe().get_profile_from_ID(Processe().get_ID_from_username(str(name)))
        datei.update({"token":name})
        return json.dumps(datei, indent = 4)

@app.route('/<name>/<id>/profile', methods = ['GET']) #fast fertig
@cross_origin()
def profile(name, id):
    if request.method == 'GET':
        print(name)
        print(id)
        datei = Processe().get_profile_from_ID(str(id))
        datei.update({"token":name})
        return json.dumps(datei, indent = 4)


if __name__ == "__main__":
    app.run(debug=True)