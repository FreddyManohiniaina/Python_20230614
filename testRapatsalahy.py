import mysql.connector

config = {"host":"localhost", "port":3308, "user":"root", "password":"", "database":"new_tp_sgbdr", "raise_on_warnings" : True}

try :
    connexion = mysql.connector.connect(**config)
    print("Yoh brada, you're connected!")
    connexion.close()

except mysql.connector.Error as error:
    print(f"Mysql error connexion : {error}, you should fix this code.")
