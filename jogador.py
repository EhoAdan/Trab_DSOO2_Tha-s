from typing import List
from abc import ABC, abstractmethod

class Jogador(ABC):
    def __init__(self, nome, email, senha, saldo,
                 dinheiro_gasto = 0, presentes_dados = 0,
                 presentes_recebidos = 0, partidas_jogadas = 0,
                 lista_itens_jogador = []):
        try:
            if not isinstance(nome, str):
                raise TypeError
            if not isinstance(email, str):
                raise TypeError
            if not isinstance(senha, str):
                raise TypeError
            if not isinstance(saldo, int):
                raise TypeError
            if not isinstance(lista_itens_jogador, list):
                raise TypeError
            if not isinstance(dinheiro_gasto, int):
                raise TypeError
            if not isinstance(presentes_dados, int):
                raise TypeError
            if not isinstance(presentes_recebidos, int):
                raise TypeError
            if not isinstance(partidas_jogadas, int):
                raise TypeError
            self.__nome = nome
            self.__email = email
            self.__senha = senha
            self.__saldo = saldo
            self.__lista_itens_jogador = lista_itens_jogador
            self.__dinheiro_gasto = dinheiro_gasto
            self.__presentes_dados = presentes_dados
            self.__presentes_recebidos = presentes_recebidos
            self.__partidas_jogadas = partidas_jogadas
            self.__amigos = []
        
        except TypeError:
            print("Houve um erro ao instanciar o jogador.")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        try:
            if not isinstance(nome, str):
                raise TypeError
            self.__nome = nome

        except TypeError:
            print("Houve um erro ao mudar o nome do jogador.")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        try:
            if not isinstance(email, str):
                raise TypeError
            self.__email = email

        except TypeError:
            print("Houve um erro ao mudar o email do jogador.")

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        try:
            if not isinstance(senha, str):
                raise TypeError
            self.__senha = senha

        except TypeError:
            print("Houve um erro ao mudar a senha do jogador.")

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        try:
            if not isinstance(saldo, int):
                raise TypeError
            self.__saldo = saldo

        except TypeError:
            print("Houve um erro ao mudar o saldo do jogador.")

    @property
    def dinheiro_gasto(self):
        return self.__dinheiro_gasto

    @dinheiro_gasto.setter
    def dinheiro_gasto(self, dinheiro_gasto):
        try:
            if not isinstance(dinheiro_gasto, int):
                raise TypeError
            self.__dinheiro_gasto = dinheiro_gasto

        except TypeError:
            print("Houve um erro ao mudar o dinheiro_gasto do jogador.")

    @property
    def presentes_dados(self):
        return self.__presentes_dados

    @presentes_dados.setter
    def presentes_dados(self, presentes_dados):
        self.__presentes_dados = presentes_dados

    @property
    def presentes_recebidos(self):
        return self.__presentes_recebidos

    @presentes_recebidos.setter
    def presentes_recebidos(self, presentes_recebidos):
        self.__presentes_recebidos = presentes_recebidos

    @property
    def partidas_jogadas(self):
        return self.__partidas_jogadas

    @partidas_jogadas.setter
    def partidas_jogadas(self, partidas_jogadas):
        try:
            if not isinstance(partidas_jogadas, int):
                raise TypeError
            self.__partidas_jogadas = partidas_jogadas

        except TypeError:
            print("Houve um erro ao mudar as partidas_jogadas do jogador.")

    @property
    def amigos(self):
        return self.__amigos

    @amigos.setter
    def amigos(self, amigos):
        self.__amigos = amigos

    @property
    def lista_itens_jogador(self):
        return self.__lista_itens_jogador

    @lista_itens_jogador.setter
    def lista_itens_jogador(self, lista_itens_jogador):
        self.__lista_itens_jogador = lista_itens_jogador
