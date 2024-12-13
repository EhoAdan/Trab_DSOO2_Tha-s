from dao import DAO
from item import Item
from personagem import Personagem
from skin import Skin

#cada entidade terá uma classe dessa, implementação bem simples.
class LojaDAO(DAO):
    def __init__(self):
        super().__init__('itens.pkl')

    def add(self, item: Item):
        if item is not None and (isinstance(item, Personagem) or isinstance(item, Skin)):
            super().add(item.nome, item)

    def update(self, item: Item):
        if item is not None and (isinstance(item, Personagem) or isinstance(item, Skin)):
            super().update(item.nome, item)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
