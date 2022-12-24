from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../tuto.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Estudiantes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    documento = db.Column(db.Integer)

    def __str__(self):
        return f"{self.nombre}"


@app.route('/')
def index():  # put application's code here
    nombre = Estudiantes.query.all()
    return render_template('firstpage.html', nombre=nombre)


@app.route('/second')
def secondpage():  # put application's code here
    nombre = Estudiantes.query.all()
    return render_template('secondpage.html', nombre=nombre)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
