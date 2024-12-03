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
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Lista de Jogadores", font=("Helvica", 25))],
            [sg.PopupScrolled(*lista_jogadores, title="Lista de Jogadores")]
                ]
        self.__window.close()

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
        sg.ChangeLookAndFeel('DarkTeal4')
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
        sg.ChangeLookAndFeel('DarkTeal4')
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
