'''
Created on Jan 10, 2017

@author: hanif
'''

import pymysql


class Database:
    def connect(self):
        # return pymysql.connect("urlshortner-mysql", "dev", "dev", "crud_flask")

        return pymysql.connect(host="urlshortner-mysql", user="dev", password="dev", database="crud_flask", charset='utf8mb4')

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM url_shortner order by code asc")
            else:
                cursor.execute(
                    "SELECT * FROM url_shortner where id = %s order by code asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def read_code(self, code):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute(
                "SELECT * FROM url_shortner where code = %s order by code asc limit 1", (code,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, url, code):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO url_shortner(code,url) VALUES(%s, %s)",
                           (code, url,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE url_shortner set code = %s, url = %s where id = %s",
                           (data['code'], data['url'],  id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM url_shortner where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
