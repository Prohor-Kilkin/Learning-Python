import sqlite3
import os.path
from flask import Flask, render_template, url_for, request, flash, session, redirect, g
from flsk.FDataBase import FDataBase


# конфигурация
DATABASE = 'flsk.db'
DEBUG = True
SECRET_KEY = '0db86ef0ec9d25d571de11184e5cb0e93725d077'

app = Flask(__name__)
app.config.from_object(__name__)
# app.config['SECRET_KEY'] = 'wettrt44gfgjfnj123hkjk454kljklgfg4564'

app.config.update(dict(DATABASE=os.path.join(app.root_path, "flsk.db")))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('databases.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


menu = [{"name": "Главная", "url": "index"},
        {"name": "Товары", "url": "goods"},
        {"name": "О нас", "url": "about"}
        ]


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
@app.route("/index")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("index.html", title="Главная", menu=dbase.get_menu())


@app.route("/goods")
def goods():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("goods.html", title="Товары", menu=dbase.get_menu(), goods=dbase.get_goods())


@app.route("/add_goods", methods=['POST', 'GET'])
def add_goods():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        if len(request.form['title']) > 2 or type(request.form['price']) == (int or float):
            res = dbase.add_goods(request.form['title'], request.form['price'])
            if not res:
                flash('Ошибка добавления продукта', category='error')
            else:
                flash('Продукт добавлен', category='success')
        else:
            flash('Ошибка добавления продукта', category='error')

    return render_template("add_goods.html", title="Добавление товара", menu=dbase.get_menu())


@app.route("/about")
def about():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("about.html", title="О нас", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)
