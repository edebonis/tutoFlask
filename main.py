from flask import render_template as render, flash
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from app.migrate import init_db

app = create_app()


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../tuto.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    return render('errors/error404.html',error=error)


@app.errorhandler(500)
def internal_server_error():
    return render('errors/error500.html')


@app.route('/')
def index():  # put application's code here
    flash("index message flash", category='error')
    return render('index.html')


@app.route('/database')
def database():  # put application's code here
    init_db()
    return "base de datos creada correctamente"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
