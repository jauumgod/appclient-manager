from flask import Flask, url_for, request, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ford.db"
app.config["SQLALCHEMY_TRACKMODIFICATIONS"] = False
app.config['SECRET_KEY']='uzumymw' #trpaça do gta kkkk
db = SQLAlchemy()
login_manager = LoginManager()
db.init_app(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(184), unique=True, nullable=False)
    password = db.Column(db.String(184),nullable=False)

    def __str__(self):
        return self.name

    with app.app_context():
        db.create_all()

class Devedores(db.Model):
    __tablename__ = 'tab_clients'
    id = db.Column(db.Integer, primary_key=True)
    clientes = db.Column(db.String(184), unique=True, nullable=False)
    valor = db.Column(db.String(184),nullable=False)
    status = db.Column(db.String(184), nullable=False)

    def __str__(self):
        return self.name

    with app.app_context():
        db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username = request.form['usuario']
        password = request.form['senha']
        
        user = User.query.filter_by(login=username).first()
        if not user:
            flash('Credenciais Inválidas')
            return redirect(url_for("login"))

        if not check_password_hash(user.password, password):
            flash('Credenciais Inválidas')
            return redirect(url_for("login"))

        #login_user(user)   
        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/settings")
def settings():

    return render_template("settings.html")

if __name__ == "__main__":
    app.run(debug=True)