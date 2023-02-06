from flask import Flask, url_for, request, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager, login_user, logout_user,UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ford.db"
app.config["SQLALCHEMY_TRACKMODIFICATIONS"] = False
app.config['SECRET_KEY']='uzumymw' #trpaça do gta kkkk
db = SQLAlchemy()
login_manager = LoginManager(app)
db.init_app(app)


@login_manager.user_loader
def current_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
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


@app.route("/config/user/<int:id>")
def unique(id):
    user = User.query.get(id)
    return render_template("config", user=user)

@app.route("/config/delete/<int:id>")
def deleteUser(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("config"))

@app.route("/login", methods=['GET', 'POST'])
def login():
    
    if request.method=='POST':
        username = request.form['usuario']
        password = request.form['senha']

        user = User.query.filter_by(username = username).first()

        if not user:
            flash("Credenciais Invalidas")
            return redirect (url_for("login"))

        if not check_password_hash(user.password, password):
            return redirect(url_for("login"))

        return redirect(url_for("index"))

    return render_template("login.html")

@app.route("/route_admin_secret")
def route_admin_secret():
    if request.method=='POST':
        username = request.form['usuario']
        password = request.form['senha']    
        #login_user(user) admin/ admin
        return redirect(url_for("index"))

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/config")
def config():
    users = User.query.all()
    return render_template("config.html", users=users)

@app.route("/resolvidos")
def resolvidos():
    return render_template("resolvidos.html")

@app.route("/registrar", methods=['GET', 'POST'])
def registrar():
    if request.method=='POST':
        user = User()
        user.username = request.form['user']
        user.password = generate_password_hash(request.form['password'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("config"))

    return render_template("registrar.html")

@app.route("/contratos")
def contratos():
    return render_template("contratos.html")

@app.route("/logout")
def logout_user():
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)