from .item_pedido import ItemPedido

class Producto(ItemPedido):
    def __init__(self, nombre, precio, imagen=None):
        self.nombre = nombre
        self.precio = precio
        self.imagen = imagen

    def get_precio(self):
        return self.precio

    def get_nombre(self):
        return self.nombre
