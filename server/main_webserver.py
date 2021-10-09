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
    user = request.form.get('user')
    if Processe().login_check(user,password):
        return json.dumps({"token":user}, indent = 4)
    else:
        return json.dumps({"token":""}, indent = 4)

@app.route('/registrieren', methods=['POST'])
@cross_origin()
def registrieren():
    password = request.form.get('password')
    user = request.form.get('user')
    if Processe().registrieren(user,password):
        return "Registriert"
    else:
        return "ERROR"



@app.route('/<name>/info')
@cross_origin()
def info(name):
    print(name)
    datei = Processe().random_choose_profile()
    datei.update({"token":name})
    return json.dumps(datei, indent = 4)

if __name__ == "__main__":
    app.run(debug=True)