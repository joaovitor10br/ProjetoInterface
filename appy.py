from PySimpleGUI import PySimpleGUI as sg
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario', size=(20, 0))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,0))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entar')]
]
janela = sg.Window('Tela de login', layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'João Vitor' and valores['senha'] == '12345':
            print('Bem vindo :D')
