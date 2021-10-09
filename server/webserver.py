from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return str(request.form.get('fname'))

@app.route('/login')
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