from dao import DAO
from jogador import Jogador
from typing import List

#cada entidade terá uma classe dessa, implementação bem simples.
class JogadorDAO(DAO):
    def __init__(self):
        super().__init__('jogadores.pkl')

    def add(self, jogador):
        if jogador is not None and (isinstance(jogador, Jogador)):
            super().add(jogador.nome, jogador)

    def update(self, jogador):
        if jogador is not None and (isinstance(jogador, Jogador)):
            super().update(jogador.nome, jogador)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)