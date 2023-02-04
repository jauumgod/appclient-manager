from flask import Flask, url_for, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)