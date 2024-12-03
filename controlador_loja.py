from jogador import Jogador
from personagem import Personagem
from skin import Skin
from tela_loja import TelaLoja
from controlador_jogador import ControladorJogador
from compra import Compra


class ControladorLoja:

    def __init__(self, jogador: Jogador, controlador_sistema, itens = [], historico_compras = []):
        # Serve como o controlador de itens
        self.__tela_loja = TelaLoja()
        self.__itens = itens
        self.__controlador_sistema = controlador_sistema
        self.__controlador_jogador = ControladorJogador(controlador_sistema)
        self.__jogador = jogador
        self.__jogador_logado = 0
        self.__historico_compras = historico_compras

    @property
    def jogador(self):
        return self.__jogador

    @property
    def itens(self):
        return self.__itens

    @property
    def tela_loja(self):
        return self.__tela_loja

    @property
    def jogador_logado(self):
        return self.__jogador_logado

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador

    @jogador.setter
    def jogador(self, jogador):
        try:
            if not isinstance(jogador, Jogador):
                raise TypeError
            self.__jogador = jogador

        except TypeError:
            print("Houve um erro ao modificar o jogador.")

    @itens.setter
    def itens(self, itens):
        try:
            if not isinstance(itens, list):
                raise TypeError
            for objeto in itens:
                if not isinstance(objeto, Personagem) and not isinstance(objeto, Skin):
                    raise TypeError
            self.__itens = itens

        except TypeError:
            print("Houve um erro ao modificar a lista de itens da loja.")

    @tela_loja.setter
    def tela_loja(self, tela_loja):
        try:
            if not isinstance(tela_loja, TelaLoja):
                raise TypeError
            self.__tela_loja = tela_loja

        except TypeError:
            print("Houve um erro ao modificar a tela da loja.")

    @jogador_logado.setter
    def jogador_logado(self, jogador_logado):
        self.__jogador_logado = jogador_logado

    @controlador_jogador.setter
    def controlador_jogador(self, controlador_jogador):
        self.__controlador_jogador = controlador_jogador

    @property
    def historico_compras(self):
        return self.__historico_compras

    @historico_compras.setter
    def historico_compras(self, historico_compras):
        self.__historico_compras = historico_compras

    def abre_tela(self):
        opcoes_loja = {0: self.__controlador_sistema.abre_tela,
                1: self.buscar_todos_itens_loja,
                2: self.buscar_itens_disponiveis,
                3: self.comprar_item,
                4: self.ver_hist_compras,
                5: self.ver_hist_compras_proprio
                }

        while True:
            opcoes_loja[self.__tela_loja.abre_tela()]()

    def buscar_todos_itens_loja(self):
        i = 0
        for item in self.__itens:
            i += 1
            print(f"{i}: {item.nome}")
        return None

    def buscar_itens_disponiveis(self, comprar = False):
        i = 0
        if comprar:
            lista_itens_num = {0: None}
            print("0: Retornar")
        for item in self.__itens:
            if (item not in self.__jogador.lista_itens_jogador and
                (isinstance(item, Personagem) or item.personagem in self.__jogador.lista_itens_jogador)):
                # Basicamente, verifica se o item tá na lista de itens do jogador,
                # caso não esteja, verifica se é um personagem ou skin, caso seja skin,
                # verifica se o jogador tem o personagem ao qual a skin pertence
                i += 1
                mensagem_mostrar = f"{i}: {item.nome}"
                if comprar:
                    # Como tem que atualizar o dicionário com cada iteração
                    # acho que os prints tem que ficar aqui mesmo e não na tela
                    mensagem_mostrar += f" por {item.preco}"
                    lista_itens_num[i] = item
                print(mensagem_mostrar)
        if comprar:
            opcao_usuario = self.__tela_loja.buscar_itens(i)
            return lista_itens_num[opcao_usuario]
        return None

    def comprar_item(self):
        # Vou deixar sem presentear por enquanto, mas se puxar do controlador de jogador
        # Deve dar sem muito problema
        while True:
            print(f"Saldo atual: {self.__jogador.saldo}")
            item_comprado = self.buscar_itens_disponiveis(True)
            if not item_comprado:
                return None
            if self.__jogador.saldo >= item_comprado.preco:
                if isinstance(item_comprado, Skin):
                    tipo_item = "skin"
                else:
                    tipo_item = "personagem"
                compra = Compra(self.__jogador, item_comprado, tipo_item)
                self.__jogador.saldo -= item_comprado.preco
                self.__jogador.lista_itens_jogador.append(item_comprado)
                self.__historico_compras.append(compra)
                return None
            print("Saldo insuficiente.")

    def ver_hist_compras(self):
        for compra in self.__historico_compras:
            self.__tela_loja.historico_compras(compra.jogador.nome, compra.item.preco,
                                               compra.item.nome, compra.data, compra.tipo_item)
        return None

    def ver_hist_compras_proprio(self):
        for compra in self.__historico_compras:
            if compra.jogador.nome == self.__jogador.nome:
                self.__tela_loja.historico_compras(compra.jogador.nome, compra.item.preco,
                                                compra.item.nome, compra.data, compra.tipo_item)