#/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import render_template
from flask import make_response
from flask import g
from flask import request
from flask import redirect
from flask import Response
from .database import Database
#import uuid
import datetime

app = Flask(__name__)


def valider_date(la_date):
    valide = 1
    try:
        datetime.datetime.strptime(la_date,'%Y-%m-%d')
    except ValueError:
        valide = 0
        #print("DATE INVALIDE")
       # raise ValueError("data non valideeeeee")
    finally:
        return valide


def get_db():
    db = getattr(g,'_database',None)
    if db is None:
        g._database = Database()
    #db.row_factory = sqlite3.Row
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g,'_database',None)
    if db is not None:
        db.disconnect()


@app.route('/')
def page_acceuil():
    db = get_db()
    #rows = db.get_article_complet()
    #if(valider_date("eee2020-02-23") is 1):
        #db.add_article("ajout 1","id ajout1","aut ajout1","2020-02-23","ajout para 1")
    rows = db.get_article_complet()
    return render_template('accueil.html', articles_recent=rows)


@app.route('/texte')
def expression_chercher():
    db = get_db()
    rows = db.get_article_texte("ajout")
    for row in rows:
        print(row)
    return("pade du texte expression")


@app.route('/article/<identifiant>')
def afficher_un_article(identifiant):
    print(identifiant)
    return("page article en vue")

