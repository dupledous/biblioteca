import bcrypt
class Usuario:
    def __init__(self):
        pass
    def encryptar(password):
        password_byte = password.encode('utf-8')
        salt = bcrypt.gensalt()
        password_cifrada = bcrypt.hashpw(password_byte, salt)
        return password_cifrada
    def verificacion(password_cifrada, contrasena):
        contrasena_byte = contrasena.encode('utf-8')
        return bcrypt.checkpw(contrasena_byte,password_cifrada)


