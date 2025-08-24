import base_de_datos
import sqlite3
import report
class Libro:
    def __init__(self,isbn,titulo,autor,fecha_de_publicacion,editoria,numero_de_copias):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.fecha_de_publicacion = fecha_de_publicacion
        self.editoria = editoria
        self.numero_de_copias = numero_de_copias
class Menu:
    def __init__(self):
        self.connexion = sqlite3.connect('biblioteca.db')
        self.cursor = self.connexion.cursor()
    def agregar(self,libro):
        self.cursor.execute(''' INSERT INTO libros (isbn,titulo,autor,fecha_de_publicacion,editoria,numero_de_copias)VALUES(?, ?, ?, ?, ?, ? )''',(libro.isbn,libro.titulo,libro.autor,libro.fecha_de_publicacion,libro.editoria,libro.numero_de_copias))
        self.connexion.commit()
    def modificar(self,isbn,n_titulo,n_autor,n_fecha,n_editoria,n_numeroC):
        self.cursor.execute('''UPDATE libros SET titulo = ? , autor = ?, fecha_de_publicacion = ?, editoria = ?, numero_de_copias = ? WHERE isbn = ? ''',(n_titulo,n_autor,n_fecha,n_editoria,n_numeroC,isbn))
        self.connexion.commit()
    def eliminar(self,isbn):
        self.cursor.execute('DELETE FROM libros WHERE isbn = ? ',(isbn,))
        self.connexion.commit()
    def cerrar(self):
        self.connexion.close()
    def inicia_menu(self):
        control = int(input('entra 1 si queres ingresar un libro , 2 por modificar , 3 por eliminar , 4  para ver :  '))
        if control == 1 :
            isbn = int(input('ingresar isbn '))
            titulo = input('ingresar titulo ')
            autor = input('ingresar autor ')
            fecha_de_publicacion = input('ingresar fecha de publicacion ')
            editoria = input('ingresar editoria ')
            numero_de_copias = int(input('ingresar numero de copias '))
            libro = Libro(isbn,titulo,autor,fecha_de_publicacion,editoria,numero_de_copias)
            self.agregar(libro)
        elif control == 2:
            isbn = int(input('ingresar el isbn del libro que quiere modificar '))
            n_titulo = input('ingresar el nuevo titulo ')
            n_autor = input('ingresar el nuevo autor ')
            n_fecha = input('ingresar el nuevo fecha de publicacion ')
            n_editoria = input('ingresar el nuevo editoria ')
            n_numeroC = int(input('ingresa el nuevo numero de copias '))
            self.modificar(isbn,n_titulo,n_autor,n_fecha,n_editoria,n_numeroC)
        elif control == 3 :
            isbn = int(input('ingresar el isbn del libro que qiere eliminar '))
            self.eliminar(isbn)
        elif control == 4:
            report.Report().mostrar()
