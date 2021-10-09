from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def index():
    return str(request.form.get('fname'))

@app.route('/login')
@cross_origin()
def login():
    return "Test"

@app.route('/registrieren')
def registrieren():
    return ""

@app.route('/info')
def info():
    return ""

if __name__ == "__main__":
    app.run(debug=True)