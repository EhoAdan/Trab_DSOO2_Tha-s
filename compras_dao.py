from dao import DAO
from compra import Compra


#cada entidade terá uma classe dessa, implementação bem simples.
class ComprasDAO(DAO):
    def __init__(self):
        super().__init__('compras.pkl')

    def add(self, compra: Compra):
        if compra is not None and isinstance(compra, Compra):
            super().add(compra.num_compra, compra)

    def update(self, compra: Compra):
        if compra is not None and isinstance(compra, Compra):
            super().update(compra.num_compra, compra)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
