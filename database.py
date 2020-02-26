import sqlite3
import datetime

class Database:

    def __init__(self):
        self.connection = None


    def get_connection(self):
        self.connection = sqlite3.connect('db/articles.db')
        self.connection.row_factory = sqlite3.Row
        return self.connection


    def disconnect(self):
        if self.connection is not None:
            self.connection.close()



    def add_article(self,titre,identifiant,auteur,date_publication,paragraphe):
        connection = self.get_connection()
        #date_valide = valider_date(date_publication)
        #if(date_valide is 1):
        connection.execute(("insert into article(titre,identifiant,auteur,date_publication,paragraphe)"
                            "values(?,?,?,?,?)"),(titre,identifiant,auteur,date_publication,paragraphe))
        connection.commit()


    def get_article_complet(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select id,titre,identifiant,auteur,date_publication,paragraphe from article where date_publication <= date('now')"
                        " order by datetime(date_publication) DESC limit 5")
        article = [dict(row) for row in cursor.fetchall()]
        return article


    def get_article_texte(self,expression):
        cursor = self.get_connection().cursor()
        cursor.execute("select * from article where titre or paragraphe like ?", ('%'+expression+'%',))
        article = [dict(row) for row in cursor.fetchall()]
        return article



    def get_liste_complete(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select * from article")
        article = [dict(row) for row in cursor.fetchall()]
        return article


    def modifier_article(self,nouv_titre,nouv_paragraphe,target_id):
        connection = self.get_connection()
        connection.execute(("update article set titre = ?, paragraphe = ? where id = ?"),(nouv_titre,nouv_paragraphe,target_id))
        connection.commit()
