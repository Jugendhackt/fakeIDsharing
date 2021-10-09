from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route("/account")
def accountList():
    return "list of accounts"