import sqlite3 as sq

def inserisciUtente():

    userName = input("Inserisci il nome utente che si vuole inserire: ")
    password = input("Inserire la password che si vuole inserire: ")

    conn = sq.connect("Utenti.db")  #aprire il DB
    curs = conn.cursor()    #ottenere un cursore (permette lo scorrimento dei dati)
    curs.execute("INSERT into UTENTI (username, password) values (?,?)", (userName, password))  #cosa voglio inserire, eseguo la query
    conn.commit()   #confermo per l'eseguzione
    conn.close()

if __name__=="__main__":
    inserisciUtente()