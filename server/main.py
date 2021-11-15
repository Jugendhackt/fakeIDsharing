import sqlite3
import random
import names
import createMails
import itertools
from collections import defaultdict


class Processe:
    def __init__(self) -> None:
        try:
            self.db = sqlite3.connect('data.db')
            self.conn = self.db.cursor()
            print("Succesfull")

        except Exception as e:
            print(e)

    def login_check(self, user, password) -> bool:  # Fertig (ohne Verschlüsselung)
        sql = """SELECT password FROM Accounts WHERE username = '{}'""".format(
            user)
        self.conn.execute(sql)
        rows = self.conn.fetchall()
        if len(rows) == 1 and rows[0][0] == password:
            return True
        else:
            return False

    def registrieren(self, user, password):  # Fertig (nicht Verschlüsselt)
        sql = """SELECT count(*) FROM Accounts WHERE username = '{}'""".format(user)
        self.conn.execute(sql)
        rows = self.conn.fetchone()[0]
        print(rows)
        if rows != 0:
            return False
        else:
            sql = """INSERT INTO Accounts VALUES('{}', '{}')""".format(
                user, password)
            print(sql)
            self.conn.execute(sql)
            self.db.commit()
            Processe.random_choose_profile(self, user)
            Processe.create_profile(self)
            Processe.create_profile(self)
            Processe.create_profile(self)
            return True

    def create_profile(self):
        Addressliste = ["Friedrich-Eberg-Straße 105, 19827 Wieseerrrnb", "Ebert-Straße 599, 39119 Kusel", "Schulstraße 170, 00442 Zwenkauenen",
                        "Hauptstraße 450, 09957 Langenwitzendorf", "Isarwuenstraßr 107, 92481 Mittenwalde", "Fehrenbachallee 360, 99106 Freiburg in Breißgauent", "Friedrich-Eberg-Straße 195, 19829 Wiewseerrrnb",
                        "Friedrich-Ebergen-Straße 195, 19825 Wierrrnsb", "Friedrichss 99, 19800 Hiele", "Frieichss 98, 19800 Hile", "Fririchss 990, 19800 Hile"]
        Addresse = random.choice(Addressliste)
        nummer = "017139200"
        nummerrandom = str(random.randrange(10, 99))
        Telefon = nummer+nummerrandom
        Geschlecht = ['Male', 'Female']
        Geschlecht = random.choice(Geschlecht)
        Name = names.get_full_name(gender=Geschlecht)
        Geburtsdatum = (random.choice(["01", "02", "03", "04", "05", "06", "07", "08", "09",
                                       "10", "11", "12"]) + "/" + random.choice(["01", "02", "03", "04", "05", "06",
                                                                                 "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
                                                                                 "20", "21", "22", "23", "24", "25", "26", "27", "28"]) + "/" +
                        random.choice(["1980", "1981", "1982", "1983", "1984", "1985", "1986",
                                       "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1996",
                                       "1997", "1998", "1999", "2000"]))
        Email = createMails.getMail.createMail(self)[0]

        print(Email, self.get_link[0], Name,
              Geburtsdatum, Addresse, Geschlecht, Telefon)

        sql = f"INSERT INTO anonymprofile (Email, Email_Webaddresse, Name, Geburtsdatum, Addresse, Geschlecht, Telefon) VALUES('{Email}','{self.get_link[0]}', '{Name}','{Geburtsdatum}', '{Addresse}','{Geschlecht}', '{Telefon}')"
        print(sql)
        self.conn.execute(sql)
        self.db.commit()

    def random_choose_profile(self, username) -> dict:  # Fertig
        sql = """SELECT * FROM anonymprofile"""
        self.conn.execute(sql)
        rows = self.conn.fetchall()
        row = random.choice(rows)
        print(row)
        sql = "INSERT INTO connect (username, ID) VALUES('{}', '{}')".format(
            username, row[0])
        print(sql)
        self.conn.execute(sql)
        self.db.commit()
        return self.profilelist_to_dic(row)

    def profilelist_to_dic(self, row):
        return {"id": row[0],
                "Email": row[1],
                "Email_Webaddresse": row[2],
                "name": row[3],
                "Geburtsdatum": row[4],
                "Addresse": row[5],
                "Geschlecht": row[6],
                "Telefon": row[7]}

    def get_profile_from_ID(self, id):
        sql = """SELECT * FROM anonymprofile WHERE ID = '{}'""".format(id)
        print(sql)
        self.conn.execute(sql)
        row = self.conn.fetchall()[0]
        print(row)
        return self.profilelist_to_dic(row)

    def get_ID_from_username(self, username):
        sql = """SELECT ID FROM connect WHERE username = '{}'""".format(
            username)
        print(sql)
        self.conn.execute(sql)
        row = self.conn.fetchone()[0]
        print(row)
        return row

    def get_all_profiles(self, username):
        # id_list = []
        # sql = """SELECT ID FROM connect WHERE username = '{}'""".format(username)
        # print(sql)
        # self.conn.execute(sql)
        # row = self.conn.fetchone()[0]
        # print(row)
        # return row

        def dict_factory(cursor, row):
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d
        qu = 'select * from connect'
        self.conn.row_factory = dict_factory
        self.conn.execute(qu)
        row = self.conn.fetchall()
        print(row)

        key1 = 'username'
        username_list = [a_dict[key1] for a_dict in row]
        print(username_list)

        key2 = 'ID'
        id_list = [a_dict[key2] for a_dict in row]
        print(id_list)

        i = 0
        id_list_return = []
        for name in username_list:
            if(name == username):
                id_list_return.append(id_list[i])
                i += 1
            else:
                i += 1
        print(id_list_return)
        return id_list_return

    def set_ID_to_username(self, username, ID):
        print(username + " --> " + ID)

# x = Processe()
# x.create_profile()

# print(x.login_check("A", "1234"))
#d = x.registrieren("ww","passwort")
# print(x.random_choose_profile())
