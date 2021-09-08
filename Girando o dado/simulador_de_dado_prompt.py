################################################################################
## ATENÇÃO: Este é um código livre feito com o 
## intuito de ajudar e está liberado para modificações 
##
## PPI - Projeto Python para Iniciantes    
## Simulador de dados PROMPT
## Criado por: CelestialDev
##
## AVISOS:
## LEMBRE-SE DE INSTALAR TODAS AS BIBLIOTECAS USADAS NO CÓDIGO
## A EXECUÇÃO DO CÓDIGO ESTÁ DIVIDIDA EM ETAPAS PARA MELHOR ENTENDIMENTO
################################################################################


# Importações
import keyboard # Módulo para verificação do pressionamento de teclas
import random # Módulo para gerar números aleatórios
import sys # Módulo para fechar o programa
import os # Módulo para limpar o prompt
from time import sleep # Comando para aplicar espera no código

class Jogo():
    def __init__(self):
        self.menu() # Etapa 1: É iniciado o menu

    # Menu com escolhas para o usuário
    def menu(self):
        self.menu_escolha = int(input('Simulador de Dados\n[1] Jogar\n[2] Ajuda\n[3] Sair\nSua opção: '))
        self.verificar_menu_escolha() # Etapa 2: É verificado as escolhas do usuário 

    def verificar_atalhos(self):
        if keyboard.is_pressed('c') or keyboard.is_pressed('C'): # No caso de 'C', o usuário será direcionado para a função de setar números minímos e máximos
            os.system('cls' if os.name == 'nt' else 'clear')
            print('ATALHO C SELECIONADO!')
            self.setar_minmax()

        if keyboard.is_pressed('m') or keyboard.is_pressed('Q'): # No caso de 'M', o usuário será direcionado para o menu
            os.system('cls' if os.name == 'nt' else 'clear')
            print('ATALHO M SELECIONADO!')
            self.menu()

        if keyboard.is_pressed('q') or keyboard.is_pressed('Q'): # No caso de 'Q', o jogo fechará
            print('ATALHO Q SELECIONADO!')
            self.sair()

    def verificar_menu_escolha(self): # Etapa 3: Redireciona para as funções
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.menu_escolha == 1:
            self.jogar() # Etapa 3.1

        elif self.menu_escolha == 2:
            self.ajuda() # Etapa 3.2
        
        elif self.menu_escolha == 3:
            self.sair() # Etapa 3.3
    
    def gerar_numero(self,aux):
        # Gerar número aleatório
        num_aleatorio = random.randrange(self.min,self.max)
        # Mostrar o número aleatório 
        print(f'Seu número #{aux} aleatório é: {num_aleatorio}')

    def loop_jogo(self):
        n = 1
        while True: 
            # Etapa 3.1.4: Verificação de pressionamento de teclas
            self.verificar_atalhos()

            # Etapa 3.1.5: Gerar número
            self.gerar_numero(n)
            sleep(1)
            n+=1
    
    def setar_minmax(self):
        # Setar os números mínimos e máximos
        self.min = int(input('Insira um número mínimo: '))
        self.max = int(input('Insira um número máximo: '))
    
    # Simulação de dados
    def jogar(self): # Etapa 3.1.1: Começar a simulação para o jogador
        self.setar_minmax() # Etapa 3.1.2: Verifica números
        sleep(2) 

         # Etapa 3.1.3: Inicia o loop de jogo
        self.loop_jogo()
    
    def ajuda(self):
        print('Dentro do jogo, poderá ser usado alguns atalhos\nPara fazer o uso destes atalhos,'
        'basta presionar, DURANTE O JOGO INICIADO, algumas das teclas a seguir:\n'
        'C: Mudar os números mínimos ou máximos.\n'
        'M: Voltar ao menu\n'
        'Q: Sair do Jogo\n')
        voltar = input('Deseja voltar ao menu? [S | N]\nSua opção: ').upper()
        if voltar == 'S': 
            os.system('cls' if os.name == 'nt' else 'clear')
            self.menu()
        else:
            self.sair() 

    def sair(self):
        sys.exit()
            
app = Jogo()