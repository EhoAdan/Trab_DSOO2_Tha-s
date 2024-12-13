from tela_jogador import TelaJogador
from item import Item
from jogador import Jogador
from alteracao_exception import AlteracaoException
from personagem import Personagem
from skin import Skin
from jogador_dao import JogadorDAO
#Personagem e Skins estão aqui apenas
#Para facilitar a apresentação



class ControladorJogador:

    def __init__(self, controlador_sistema):
        self.__tela_jogador = TelaJogador()
        self.__controlador_sistema = controlador_sistema
        self.__jogador_logado = False
        self.__jogador_DAO = JogadorDAO()
        self.__jogadores = [jogador for jogador in self.__jogador_DAO.get_all()]

    @property
    def jogador_logado(self):
        return self.__jogador_logado

    @property
    def jogadores(self):
        return self.__jogadores

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def jogador_DAO(self):
        return self.__jogador_DAO

    @jogadores.setter
    def jogadores(self, jogadores):
        self.__jogadores = jogadores

    @jogador_logado.setter
    def jogador_logado(self, jogador_logado):
        self.__jogador_logado = jogador_logado

    @jogador_DAO.setter
    def jogador_DAO(self, jogador_DAO):
        self.__jogador_DAO = jogador_DAO

    def abre_tela(self):
        opcoes_tela = {0: None,
                1: self.listar, #Mexer daqui pra frente
                2: self.estats,
                3: self.alterar,
                4: self.deletar}
        
        while True:
            opcao = opcoes_tela[self.__tela_jogador.abre_tela()]
            if not opcao:
                return None
            opcao()

    def acoes_login(self):
        opcoes_jogador = {0: None,
                1: self.abre_tela,
                2: self.jogar_partida,
                3: self.historico_partidas,
                4: self.adicionar_amigo,
                5: self.excluir_amigo,
                6: self.listar_amigos
                }
        
        while True:
            opcao = opcoes_jogador[self.__tela_jogador.acoes_login()]
            if not opcao:
                return None
            opcao()

    def jogar_partida(self):
        self.__jogador_logado.partidas_jogadas += 1
        self.__tela_jogador.jogar_partida(self.__jogador_logado.partidas_jogadas)

    def historico_partidas(self):
        self.__tela_jogador.mostra_partidas_jogadas(self.__jogador_logado.partidas_jogadas)

    def eh_jogador(self, nome_jogador):
        for jogador_existe in self.__jogadores:
            if jogador_existe.nome == nome_jogador:
                return jogador_existe
        return None

    def adicionar_amigo(self):
        amigo = self.__tela_jogador.tela_adicionar_amigo()
        jogador_existe = self.eh_jogador(amigo)
        if not isinstance(jogador_existe, Jogador):
            self.__tela_jogador.exibe_mensagem("Houve uma tentativa de adicionar um não-jogador como amigo.")
        elif jogador_existe.nome == self.__jogador_logado.nome:
            self.__tela_jogador.exibe_mensagem("Você não pode se adicionar como amigo.")
        elif any(jogador_existe.nome == amigo.nome for amigo in self.__jogador_logado.amigos):
            self.__tela_jogador.exibe_mensagem(f"{jogador_existe.nome} já é seu amigo.")
        else:
            self.__jogador_logado.amigos.append(jogador_existe)
            self.__tela_jogador.exibe_mensagem(f"{jogador_existe.nome} adicionado com sucesso à sua lista de amigos.")

    def excluir_amigo(self):
        amigo = self.__tela_jogador.tela_adicionar_amigo()
        jogador_existe = self.eh_jogador(amigo)
        if not isinstance(jogador_existe, Jogador):
            self.__tela_jogador.exibe_mensagem("Você tentou excluir um amigo que não existe")
        else:
            for amigo in self.__jogador_logado.amigos:
                if jogador_existe.nome == amigo.nome:
                    self.__jogador_logado.amigos.remove(amigo)
            self.__tela_jogador.exibe_mensagem("Amigo excluído com sucesso")

    def listar_amigos(self):
        amigos = []
        if len(self.__jogador_logado.amigos) > 0:
            for amigo in self.__jogador_logado.amigos:
                amigos.append(amigo.nome)
            self.__tela_jogador.lista_amigos(amigos)
        else:
            self.__tela_jogador.lista_amigos_zero()
        
    def listar(self): #Interface Gráfica feita
        lista_jogadores = []
        for jogador in self.__jogadores:
            lista_jogadores.append(jogador.nome)

        self.__tela_jogador.mostra_lista_jogadores(lista_jogadores)

    def estats(self):
        mais_dinheiro_gasto = 0
        mais_presentes_dados = 0
        mais_partidas_jogadas = 0
        mais_itens = 0
        jog_mais_dinheiro_gasto = None
        jog_mais_presenteador = None
        jog_mais_partidas = None
        jog_mais_itens = None
        for jogador in self.__jogadores:
            if jogador.dinheiro_gasto > mais_dinheiro_gasto:
                jog_mais_dinheiro_gasto = jogador
                mais_dinheiro_gasto = jogador.dinheiro_gasto
            if jogador.presentes_dados > mais_presentes_dados:
                jog_mais_presenteador = jogador
                mais_presentes_dados = jogador.presentes_dados
            if jogador.partidas_jogadas > mais_partidas_jogadas:
                jog_mais_partidas = jogador
                mais_partidas_jogadas = jogador.partidas_jogadas
            if len(jogador.lista_itens_jogador) > mais_itens:
                jog_mais_itens = jogador
                mais_itens = len(jogador.lista_itens_jogador)
        
        self.__tela_jogador.tela_estats(mais_dinheiro_gasto, mais_presentes_dados, \
                                mais_partidas_jogadas, mais_itens, \
                                jog_mais_dinheiro_gasto, jog_mais_presenteador, \
                                jog_mais_partidas, jog_mais_itens)

    def alterar(self):
        while True:
            email_informado, senha_informada, novo_nome = self.__tela_jogador.tela_troca_nome()
            usuario_existe = False
            nome_ja_existe = False
            if email_informado == '':  
                # Sai do login caso o botão cancelar seja apertado, também
                # sai do login caso confirme sem nada escrito, mas não sei bem como arrumar
                # de qualquer jeito, acho que não tem muito problema deixar assim
                break
            for jogador in self.__jogadores:
                if novo_nome == jogador.nome:
                    nome_ja_existe = True
                    break
            if not nome_ja_existe:
                for usuario_registrado in self.__jogadores:
                    if (usuario_registrado.email == email_informado):
                        usuario_existe = True
                        if usuario_registrado.senha == senha_informada:
                            usuario_registrado.nome = novo_nome
                            self.__tela_jogador.exibe_mensagem(f"Seu novo nome é: {usuario_registrado.nome}")
                        else:
                            self.__tela_jogador.exibe_mensagem("Senha incorreta.")
                            break # Sai do loop caso o usuário exista mas a senha esteja errada
            if not usuario_existe:
                self.__tela_jogador.exibe_mensagem("Email não encontrado.")

    def deletar(self):
            email_informado, senha_informada = self.__tela_jogador.tela_deleta_conta()
            try:
                for usuario_registrado in self.__jogadores:
                    if usuario_registrado.email == email_informado:
                        if usuario_registrado.senha == senha_informada:
                            opcao = self.__tela_jogador.confirma_deleta()
                            if opcao == 1:
                                self.__jogadores.remove(usuario_registrado)
                                self.__tela_jogador.exibe_mensagem("""Conta excluída com sucesso!
Retornando à tela anterior.""")
                                self.__controlador_sistema.abre_tela()
                            elif opcao == 2:
                                self.__tela_jogador.exibe_mensagem("Que bom que decidiu não excluir sua conta e continuar conosco!")
                                self.abre_tela()
            except ValueError:
                self.__tela_jogador.exibe_mensagem("Opção inválida! Retornando a tela anterior.")
                return self.abre_tela()

#Lista preliminar de jogadores e itens
