from abc import ABC, abstractmethod

class ItemPedido(ABC):
    @abstractmethod
    def get_precio(self):
        pass

    @abstractmethod
    def get_nombre(self):
        pass
