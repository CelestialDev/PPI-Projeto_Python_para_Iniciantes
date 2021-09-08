################################################################################
## ATENÇÃO: Este é um código livre feito com o 
## intuito de ajudar e está liberado para modificações 
##
## PPI - Projeto Python para Iniciantes    
## Simulador de dados GRÁFICO 
## Criado por: CelestialDev
##
## AVISOS:
## LEMBRE-SE DE INSTALAR TODAS AS BIBLIOTECAS USADAS NO CÓDIGO
################################################################################


# Importações
import PySimpleGUI as sg
import random

# Criação do Layout
def janela_principal():
    sg.theme('DarkBlue')
    layout = [
        # Set do Range do número gerado
        [sg.Text('Variação do número',text_color='white',size=(20))],
        [sg.Text('Minímo',size=(6)),sg.Input(key='min',size=(5))],
        [sg.Text('Máximo',size=(6)),sg.Input(key='max',size=(5))],

        # Ação de gerar número
        [sg.Button('Gerar número',key='gerar')],
        
        # Output
        [sg.Output()]
    ]
    return sg.Window('Simulador de Dados', layout=layout, margins=(0,0),finalize=True)

def janela_erro():
    sg.theme('DarkBlue')
    layout = [
        [sg.Text('Ocorreu um erro.')],
        [sg.Text('Possíveis motivos:\n1. Inserção de nenhum número\n2. Inserção de letras')]
    ]
    return sg.Window('Impossível continuar com a simulação', layout=layout, margins=(0,0),finalize=True)

janela1, janela2 = janela_principal(), None

# Variável global 
reg = 1

while True:
    # Carrega o layout e lê os eventos e os itens
    window, event,values = sg.read_all_windows()

    # Caso o usuário aperte o botão
    if window == janela1 and event == 'gerar':
        min = values['min']
        max = values['max']
        try:
            print(f'O seu número #{reg} gerado é: {random.randrange(int(float(min)),int(float(max)))}')
            reg+=1 
        except:
            janela2 = janela_erro()
    
    # Se a janela de erro for fechada, esconde-la 
    if window == janela2 and event == sg.WIN_CLOSED:
        janela2.hide()

    # Se a janela principal for fechada, fechar o programa
    if window == janela1 and event == sg.WIN_CLOSED:
        break