import mysql.connector
connection = mysql.connector.connect(host='localhost', user='root', password='', port=3308, database='new_tp_sgbdr')
cursor = connection.cursor()

class personne:
    def __init__(self):
        self.id = i
        self.nom = input("Nom : ")
        self.prenom = input("Prenom : ")
        self.age = input("Age : ")
        self.nationalite = input("Nationalite : ")
        self.sexe = input("Sexe : ")
        self.date_de_naissance = input("Date_de_naissance : ")

    def fill_table(self):
        query = "INSERT INTO personne (Id, Nom, Prenom, Age, Nationalite, Sexe, Date_de_naissance) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values = (pers.id, pers.nom, pers.prenom, pers.age, pers.nationalite, pers.sexe, pers.date_de_naissance)
        cursor.execute(query, values)
        connection.commit()

effective = int(input("How many personne you have : "))
for i in range (effective):
    pers = personne()
    pers.fill_table()
cursor.close()
connection.close()