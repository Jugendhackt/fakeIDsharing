from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, login_user, login_required, current_user
from Auth import auth
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.register_blueprint(auth)
login_manager = LoginManager()
login_manager.init_app(app)
@app.route('/')
@cross_origin()
def index():
    return str(request.form.get('fname'))

@auth.route('/login', methods=['GET', 'POST'])
@app.route('/login')
@cross_origin()
def login():
    if request.method == 'GET':
        return '''
                <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
                </form>
                '''
    
    email = request.form['email']
    
    if request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        login_user(user)
        return Flask.redirect(Flask.url_for('protected'))

    return 'Bad login'


@auth.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + current_user.id




@app.route('/registrieren')
def registrieren():
    return ""



@app.route('/info')
@cross_origin()
def info():
    return json.dumps(Processe().random_choose_profile(), indent = 4)

if __name__ == "__main__":
    app.run(debug=True)