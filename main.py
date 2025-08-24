import Libro
import base_de_datos
import usuario
class Inicio:
    def __init__(self):
        pass
    def execute(self):
        password = input(" crear la contrasena que vas utilizar pa ingresar en la base de datos ")
        password_cifrada = usuario.Usuario.encryptar(password)
        intentos = 0
        while True:
            contrasena = input("Ingresa la contraseña para ingresar: ")
            if usuario.Usuario.verificacion(password_cifrada,contrasena):
                print(f"¡¡Contraseña Correcta!!.  Acceso Concedido.")
                base_de_datos.base_de_datos().crear_tabla()
                Libro.Menu().inicia_menu()
            else:
                intentos +=1
                print(f"contrasena incorecta te quedas {3-intentos}")
                if intentos == 3 :
                    print("adios ")
                    break

        
if __name__== '__main__':
    inicio = Inicio()
    inicio.execute()