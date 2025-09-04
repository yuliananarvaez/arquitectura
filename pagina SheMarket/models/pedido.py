from .item_pedido import ItemPedido

class Pedido(ItemPedido):
    def __init__(self):
        self.items = []

    def add_item(self, item: ItemPedido):
        self.items.append(item)

    def get_precio(self):
        return sum(item.get_precio() for item in self.items)

    def get_nombre(self):
        return f"Pedido con {len(self.items)} productos"

    def get_items(self):
        return self.items
