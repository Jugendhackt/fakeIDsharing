import sqlite3

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
        print(sql)
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

    def create_profile(self):
        pass

    def random_choose_profile(self):
        pass

    def get_profile_from_ID(self, id):
        pass

x = Processe()
print(x.login_check("Fr", "Hallo"))
d = x.registrieren("ww","passwort")