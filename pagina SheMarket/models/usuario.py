from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    @abstractmethod
    def permisos(self):
        pass


class Administrador(Usuario):
    def permisos(self):
        return "Puede gestionar usuarios y productos."


class Cliente(Usuario):
    def permisos(self):
        return "Puede navegar y comprar productos."


class Emprendedor(Usuario):
    def permisos(self):
        return "Puede vender productos en la plataforma."
