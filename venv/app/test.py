import sqlite3

connection = sqlite3.connect('data.db')

cursor= connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# quando eseguiamo questo programma creiamo il file data.db
# ovvero il nostro database


#creo un utente
#user = (1, "jose","asdf")
#creo una query che inserisce l' utente nel db
insert_query= "INSERT INTO users VALUES (?,?,?)"
#cursor.execute(insert_query, user)
#salvo
#connection.commit()
#chiudo
#connection.close() 

#inserisco + utenti
users = [
     (1, "ralf", "asdf"),
     (2, "anna", "kpsd")
 ]

cursor.executemany(insert_query, users)


select_query= "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)


connection.commit()
connection.close()