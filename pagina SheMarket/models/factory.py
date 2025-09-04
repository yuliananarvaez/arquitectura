from .usuario import Administrador, Cliente, Emprendedor

class UsuarioFactory:
    @staticmethod
    def crear_usuario(tipo, nombre, email):
        if tipo == "admin":
            return Administrador(nombre, email)
        elif tipo == "cliente":
            return Cliente(nombre, email)
        elif tipo == "emprendedor":
            return Emprendedor(nombre, email)
        else:
            raise ValueError(f"Tipo de usuario '{tipo}' no válido")
