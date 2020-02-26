#/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import render_template
from flask import make_response
from flask import g
from flask import request
from flask import redirect
from flask import Response
from flask import url_for
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


@app.route('/texte',methods=['GET','POST'])
def expression_chercher():
    db = get_db()
    recherche = db.get_article_texte(request.args['le_texte'])
    return render_template("recherche.html", resultat_recherche=recherche)


@app.route('/admin')
def page_admin():
    db = get_db()
    liste = db.get_liste_complete()
    print("page admin")
    return render_template("admin.html",liste_complete = liste)


@app.route('/modification')
def page_modification():
    id = request.args['id']

    
    

    db = get_db()
    rows = db.get_liste_complete()
    for row in rows:
        if (row['id'] is 1):
            db.modifier_article("gogogogog","chahahaha 1",1)
    return render_template("/modifier.html", target_id = id)


@app.route('/traiter_modification', methods=['GET','POST'])
def traiter_modification():
    if request.method == 'POST':
        db = get_db()
        db.modifier_article(request.form['new_titre'],
        request.form['new_paragraphe'],request.args['id'])
        liste = db.get_liste_complete()
        return redirect(url_for('page_admin'))
    else:
        return redirect(url_for('page_admin'))




@app.route('/ajouter')
def ajouter_article():

    return render_template("ajouter.html")


@app.route('/formulaire', methods=['GET','POST'])
def formualire():
    errors = []
    if request.method == 'GET':
        return render_template("ajouter.html")
    else:
        titre = request.form['titre']
        identifiant = request.form['identifiant']
        auteur = request.form['auteur']
        date_publication = request.form['date_publication']
        paragraphe = request.form['paragraphe']

    if(titre == "" or identifiant == "" or auteur == ""
    or date_publication == "" or paragraphe == ""):
        errors.append("Tous les champs sont obligatoires")

    if(valider_date(date_publication) is 0):
        errors.append("La date doit etre de format AAAA-MM-JJ")

    if(len(errors) == 0):
        print("ajout resssssssuiieiieie")
        db = get_db()
        db.add_article(titre,identifiant,auteur,
        date_publication,paragraphe)
        return redirect(url_for('page_admin',
        confirmer=titre))
    else:
        return render_template('ajouter.html',liste_errors = errors)

@app.route('/article/<identifiant>')
def afficher_un_article(identifiant):
    print(identifiant)
    return("page article en vue")


