import PySimpleGUI as sg

class TelaJogador():
    def __init__(self):
        self.__window = None
        self.init_opcoes()
        self.acoes_opcoes_login()

    def close(self):
        self.__window.Close()

    def mostra_lista_jogadores(self, lista_jogadores):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('NeonYellow1')
        layout = [
            [sg.Text("Lista de Jogadores", font=("Helvica", 25))],
            [sg.PopupScrolled(*lista_jogadores, title="Lista de Jogadores")]
                ]
        self.__window.close()
    
    def jogar_partida(self, partidas_jogadas):
        sg.ChangeLookAndFeel('NeonYellow1')
        layout = [
            [sg.Text("Você jogou uma partida", font=("Helvica", 25))],
            [sg.PopupScrolled(f"Você já jogou {partidas_jogadas} partidas", title="Você jogou uma partida")]
                ]
        self.__window.close()

    def mostra_partidas_jogadas(self, partidas_jogadas):
        sg.ChangeLookAndFeel('NeonYellow1')
        layout = [
            [sg.Text("Partidas Jogadas", font=("Helvica", 25))],
            [sg.PopupScrolled(f"Você já jogou {partidas_jogadas} partidas")]
                ]
        self.__window.close()
    
    def lista_amigos(self, amigos):
        sg.ChangeLookAndFeel('NeonYellow1')
        layout = [
            [sg.Text("Esta é sua lista atual de amigos:", font=("Helvica", 25))],
            [sg.PopupScrolled(*amigos, title="Esta é sua lista atual de amigos:")]
                ]
        self.__window.close()

    def lista_amigos_zero(self):
        sg.ChangeLookAndFeel('NeonYellow1')
        layout = [
            [sg.Text("Esta é sua lista atual de amigos:", font=("Helvica", 25))],
            [sg.PopupScrolled("Você não tem nenhum amigo :(", title="Esta é sua lista atual de amigos:")]
                ]
        self.__window.close()

    def tela_estats(self, mais_dinheiro_gasto, mais_presentes_dados, \
                    mais_partidas_jogadas, mais_itens, \
                    jog_mais_dinheiro_gasto, jog_mais_presenteador, \
                    jog_mais_partidas, jog_mais_itens):

        sg.ChangeLookAndFeel('NeonYellow1')
        layout = [
            [sg.Text("Estatísticas dos Jogadores", font=("Helvetica", 16), justification='center')],
            [sg.PopupScrolled(f"""O jogador que mais investiu no jogo foi: {jog_mais_dinheiro_gasto.nome}
Com um aporte total de: {mais_dinheiro_gasto}
O jogador candidato à Papai Noel é: {jog_mais_presenteador.nome}
Presenteando um total de: {mais_presentes_dados} vezes
O jogador ProPlayer do momento é: {jog_mais_partidas.nome}
Jogando {mais_partidas_jogadas} partidas
O jogador com mais colecionáveis no momento é: {jog_mais_itens.nome}
Com um total de: {mais_itens} colecionáveis
Itens do jogador com mais colecionáveis:""")]
                ]
        self.__window.close()

    def tela_troca_nome(self):
        sg.ChangeLookAndFeel('NeonYellow1')
        layout = [
                  [sg.Text('Digite seus dados de login')],
                  [sg.Text('Digite seu e-mail:'), sg.InputText('', key='email')],
                  [sg.Text('Digite sua senha:'), sg.InputText('', key='senha')],
                  [sg.Text('Digite seu novo nome:'), sg.InputText('', key='novo_nome')],
                  [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Trocar de Nome').Layout(layout)

        button, values = self.__window.Read()
        usuario = values['usuario']
        senha = values['senha']
        novo_nome = values['novo_nome']
        self.close()
        return usuario, senha, novo_nome

    def abre_tela(self):
        self.init_opcoes()
        button, values = self.__window.Read()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('NeonYellow1')
        layout = [
            [sg.Text('O que você quer fazer?', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Ver jogadores do server', "RD1", key='1')],
            [sg.Radio('Ver top jogadores do server', "RD1", key='2')],
            [sg.Radio('Alterar nome da sua conta', "RD1", key='3')],
            [sg.Radio('Deletar sua conta', "RD1", key='4')],
            [sg.Radio('Voltar ao início', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Ações do Jogador').Layout(layout)

    def acoes_login(self):
        self.acoes_opcoes_login()
        button, values = self.__window.Read()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def acoes_opcoes_login(self):
        sg.ChangeLookAndFeel('NeonYellow1')
        layout = [
            [sg.Text('O que você quer fazer?', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Acessar estatísticas e configurações da conta', "RD1", key='1')],
            [sg.Radio('Jogar partida', "RD1", key='2')],
            [sg.Radio('Histórico de Partidas', "RD1", key='3')],
            [sg.Radio('Adicionar amigo', "RD1", key='4')],
            [sg.Radio('Excluir amigo', "RD1", key='5')],
            [sg.Radio('Listar amigos', "RD1", key='6')],
            [sg.Radio('Voltar à tela anterior', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Ações do Jogador').Layout(layout)
