import sqlite3
import base_de_datos
class Report:
    def __init__(self):
        self.connexion = sqlite3.connect('biblioteca.db')
        self.cursor = self.connexion.cursor()
    def mostrar(self):
        self.cursor.execute('SELECT * from libros')
        libros = self.cursor.fetchall()
        for l in libros:
            print(l)
        self.cursor.close()
        self.connexion.close()
        