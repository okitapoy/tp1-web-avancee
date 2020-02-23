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
    rows = db.get_article_complet()

    for row in rows:
        #if(row['id'] is 1):
        print(row)
    return ("page acceuil")


