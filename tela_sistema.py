import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def menu_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao O Jogo!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Jogar',"RD1", key='1')],
            [sg.Radio('Loja',"RD1", key='2')],
            [sg.Radio('Criar conta',"RD1", key='3')],
            [sg.Radio('Fazer Login',"RD1", key='4')],
            [sg.Radio('Fechar o Jogo',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('O jogo').Layout(layout)

    def exibe_mensagem(self, mensagem):
        layout = [
            [sg.Text(mensagem)],
            [sg.Button('Ok')]
        ]
        self.__window = sg.Window('O jogo').Layout(layout)
        self.__window.Read()
        self.close()

    def login(self):
        layout = [
                  [sg.Text('Digite seus dados de login '
'(Senha deve ter ao menos 8 caracteres, uma letra e um número):')],
                  [sg.Text('Usuário ou email:'), sg.InputText('', key='usuario')],
                  [sg.Text('Digite sua senha:'), sg.InputText('', key='senha', password_char='●')],
                  [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Login').Layout(layout)

        button, values = self.__window.Read()
        usuario = values['usuario']
        senha = values['senha']
        self.close()
        return usuario, senha

    def criar_conta(self):
        layout = [
                  [sg.Text('Digite os dados desejados'
'(Senha deve ter ao menos 8 caracteres, uma letra e um número):')],
                  [sg.Text('Digite seu usuário:'), sg.InputText('', key='usuario')],
                  [sg.Text('Digite seu email:'), sg.InputText('', key='email')],
                  [sg.Text('Digite sua senha:'), sg.InputText('', key='senha', password_char='●')],
                  [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Login').Layout(layout)

        """ Tava tentando fazer um código que desabilitasse o botão de confirmar enquanto não tivesse
        uma senha e um email válidos, mas não tava conseguindo, então por enquanto deixa com pop-up
        while True:  # Como cancel deixa o que tiver no input, se eu escrever um nome já existente
                     # e der cancel, vai aparecer que o nome já existe e só depois vai me deixar sair
                     # não faço ideia de como
            button, values = self.__window.Read()
            usuario = values['usuario']
            email = values['email']
            senha = values['senha']
            email_valido = True
            senha_valida = True
            # Verifica email e senha e só habilita o botão de confirmar se estiverem corretos
            if (any(char.isdigit() for char in senha) and 
                any(char.isalpha() for char in senha) and len(senha) >= 8):
                senha_valida = True
            if (any(char == '@' for char in email) and not email[0] == '@'
                and not email[-1] == '@'):
                email_valido = True
            if senha_valida and email_valido:
                self.__window['confirmar'].update(disabled=False)
            elif usuario == '':
                break
        self.close()
        return usuario, email, senha"""
        button, values = self.__window.Read()
        usuario = values['usuario']
        email = values['email']
        senha = values['senha']
        self.close()
        return usuario, email, senha
