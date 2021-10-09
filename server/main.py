import sqlite3
import random

class Processe:
    def __init__(self) -> None:
        try:
            self.db = sqlite3.connect('data.db')
            self.conn = self.db.cursor()
            print("Succesfull")

        except Exception as e:
            print(e)


    def login_check(self, user, password)->bool: # Fertig (ohne Verschlüsselung)
        sql = """SELECT password FROM Accounts WHERE username = '{}'""".format(user)
        self.conn.execute(sql)
        rows = self.conn.fetchall()
        if len(rows) == 1 and rows[0][0]==password:
            return True
        else:
            return False
        
    
    def registrieren(self, user, password): # Fertig (nicht Verschlüsselt)
        sql = """SELECT count(*) FROM Accounts WHERE username = '{}'""".format(user)
        self.conn.execute(sql)
        rows = self.conn.fetchone()[0]
        print(rows)
        if rows >0:
            return False
        else:
            sql = """INSERT INTO Accounts VALUES('{}', '{}')""".format(user, password)
            print(sql)
            self.conn.execute(sql)
            self.db.commit()
            return True

    def create_profile(self, data_profile):

        sql = """INSERT INTO anonymprofile VALUES('{Email}', '{Name}','{Geburtsdatum}', '{Addresse}','{Geschlecht}', '{Telefon}')""".format(data_profile)
        print(sql)
        self.conn.execute(sql)
        self.db.commit()
        

    def random_choose_profile(self)->dict: # Fertig
        sql = """SELECT * FROM anonymprofile"""
        self.conn.execute(sql)
        rows = self.conn.fetchall()
        row = random.choice(rows)
        print(row)
        return self.profilelist_to_dic(row)

    def profilelist_to_dic(self,row):
        return {"id":row[0],
                "Email":row[1],
                "name":row[2],
                "Geburtsdatum":row[3],
                "Addresse":row[4],
                "Geschlecht":row[5],
                "Telefon":row[6]}
        

    def get_profile_from_ID(self, id):
        sql = """SELECT * FROM anonymprofile WHERE ID = '{}'""".format(id)
        print(sql)
        self.conn.execute(sql)
        row = self.conn.fetchall()[0]
        print(row)
        return self.profilelist_to_dic(row)

    def get_ID_from_username(self, username):
        sql = """SELECT ID FROM connect WHERE username = '{}'""".format(username)
        print(sql)
        self.conn.execute(sql)
        row = self.conn.fetchall()[0]
        print(row)
        return row

    def set_ID_to_username(self, username, ID):
        print(username + " --> "+ ID)

x = Processe()
print(x.login_check("A", "1234"))
#d = x.registrieren("ww","passwort")
#print(x.random_choose_profile())