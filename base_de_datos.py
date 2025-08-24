import sqlite3
class base_de_datos:
    def __init__(self):
        pass
    def crear_tabla(self):
        connexion = sqlite3.connect('biblioteca.db')
        cursor = connexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS libros  (isbn INTERGER PRIMARY KEY NOT NULL , titulo TEXT NOT NULL, autor TEXT NOT NULL, fecha_de_publicacion DATE NOT NULL, editoria TEXT NOT NULL, numero_de_copias INTERGER NOT NULL) ''')
        connexion.commit()
        cursor.close()
        connexion.close()