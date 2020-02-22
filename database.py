import sqlite3


class Database:

    def __init__(self):
        self.connection = None


    def get_connection(self):
        self.connection = sqlite3.connect('db/articles.db')
        return self.connection


    def disconnect(self):
        if self.connection is not None:
            self.connection.close()


    def add_article(self,id,titre,identifiant,auteur,date_publication,paragraphe):
        connection = self.get_connection()
        connection.execute(("insert into article(id,titre,identifiant,auteur,date_publication,paragraphe)"
                            "values(?,?,?,?,?,?)"),(id,titre,identifiant,auteur,date_publication,paragraphe))
        connection.commit()


    def get_article_complet(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select id,titre,identifiant,auteur,date_publication,paragraphe from article")
        article = cursor.fetchall()
        return [{"id": article[0] ,"titre": article[1],"identifiant": article[2],"auteur": article[3],"date_publication": article[4],"paragraphe": article[5]} for each_line in article]
