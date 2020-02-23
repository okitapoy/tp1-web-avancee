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


    def add_article(self,id,titre,identifiant,auteur,date_publication,paragraphe):
        connection = self.get_connection()
        if(valider_date(date_publication) is 1):
            connection.execute(("insert into article(id,titre,identifiant,auteur,date_publication,paragraphe)"
                                "values(?,?,?,?,?,?)"),(id,titre,identifiant,auteur,date_publication,paragraphe))
            connection.commit()


    def get_article_complet(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select id,titre,identifiant,auteur,date_publication,paragraphe from article")
        article = [dict(row) for row in cursor.fetchall()]
        return article



    def valider_date(la_date):
        valide = 1
        try:
            datetime.datetime.strptime(la_date,'%Y-%m-%d')
        except ValueError:
            valide = 0
           # raise ValueError("data non valideeeeee")
        finally:
            return valide
