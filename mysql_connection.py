import mysql.connector

class Person:
    def __init__(self, id, nom, prenom, age, nationalite, sexe, date_de_naissance):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.nationalite = nationalite
        self.sexe = sexe
        self.date_de_naissance = date_de_naissance

# Establish the connection
connection = mysql.connector.connect(host="localhost", port=3308, user="root", password="", database="new_tp_sgbdr")

# Create a cursor
cursor = connection.cursor()

data = [
    (1, "John", "Doe", 25, "USA", "Male", "1998-01-01"),
    (2, "Johny", "DoeT", 27, "USA", "Male", "1996-01-01"),
    (3, "John", "Doe", 25, "USA", "Male", "1998-01-01"),
    (4, "Johny", "DoeT", 27, "USA", "Male", "1996-01-01"),
    (6, "John", "Doe", 25, "USA", "Male", "1998-01-01"),
    (7, "Johny", "DoeT", 27, "USA", "Male", "1996-01-01"),
]

# Create an instance of the Person class for each item in data and insert into the database
for item in data:
    person = Person(*item)
    query = "INSERT INTO personne(Id, Nom, Prenom, Age, Nationalite, Sexe, Date_de_naissance) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (person.id, person.nom, person.prenom, person.age, person.nationalite, person.sexe, person.date_de_naissance)
    cursor.execute(query, values)

# Commit the changes
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()
