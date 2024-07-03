# -*- coding: utf-8 -*-
# Importa o modulo tkinter como tk
import tkinter as tk
# Importa a funcao messagebox do modulo tkinter
from tkinter import messagebox

# classe ConnectFour
class ConnectFour:
    # Define o metodo de inicializacao da classe ConnectFour
    def __init__(self, root):
        # Inicializa o atributo root da instancia
        self.root = root
        # Define o titulo da janela como "Jogo da velha"
        self.root.title("Jogo da Velha")
         # Define o jogador atual como 'X'
        self.jogador = 'X'
        # Cria uma matriz 7x7 para representar o tabuleiro do jogo
        self.tabuleiro = [['' for _ in range(7)] for _ in range(7)]
        # Inicializa uma lista vazia para armazenar os botoes do jogo
        self.botoes = []
        # Define a dificuldade inicial como 'Facil'
        self.dificuldade = 'Fácil'
        # Cria uma variavel do tipo StringVar() do tkinter
        self.variavel_dificuldade = tk.StringVar()
        # Define o valor inicial da variavel de dificuldade como 'Fácil'
        self.variavel_dificuldade.set('Fácil')
        # Chama o metodo para criar o tabuleiro do jogo
        self.criar_tabuleiro()
        # Chama o metodo para criar o seletor de dificuldade do jogo
        self.criar_seletor_dificuldade()
        # Cache para armazenar as jogadas pre-computadas
        self.precompute = {}
# Define o metodo para criar o tabuleiro do jogo
    def criar_tabuleiro(self):
        # Loop sobre as linhas do tabuleiro
        for i in range(7):
# Inicializa uma lista vazia para representar uma linha do tabuleiro
            linha = []
            # Loop sobre as colunas do tabuleiro
            for j in range(7):
# Cria um botao tkinter com texto vazio, fonte Arial de tamanho 20, largura de 3 caracteres e altura de 1 caractere
                botao = tk.Button(self.root, text='', font=('Arial', '20'), width=3, height=1,
# O parâmetro 'command' do botão Tkinter recebe uma função a ser executada quando o botão é clicado.
# A função lambda é usada aqui para criar uma função anônima que chama self.clique_botao com os argumentos 'linha' e 'coluna'.
# 'lambda linha=i, coluna=j' define uma função anônima que captura os valores de 'i' e 'j' na iteração atual do loop.
# Quando o botão é clicado, a função lambda executa self.clique_botao(linha, coluna), passando os valores capturados de 'i' e 'j'.
                                  command=lambda linha=i, coluna=j: self.clique_botao(linha, coluna))
                # Posiciona o botao na janela do tkinter
                botao.grid(row=i, column=j, padx=5, pady=5)
                # Adiciona o botao a linha atual
                linha.append(botao)
                # Adiciona a linha a lista de botoes do tabuleiro
            self.botoes.append(linha)
# Define o metodo para criar o seletor de dificuldade do jogo
    def criar_seletor_dificuldade(self):
        # Cria um rotulo para indicar o nivel de dificuldade
        label_dificuldade = tk.Label(self.root, text="Nível de Dificuldade:")
        # Posiciona o rótulo na janela tkinter
        label_dificuldade.grid(row=7, column=0, columnspan=2)
        # Cria um botão de seleção para a dificuldade fácil
        botao_facil = tk.Radiobutton(self.root, text="Fácil", variable=self.variavel_dificuldade, value='Fácil')
        # Posiciona o botão de seleção na janela tkinter
        botao_facil.grid(row=7, column=3)
        # Cria um botão de seleção para a dificuldade difícil
        botao_dificil = tk.Radiobutton(self.root, text="Difícil", variable=self.variavel_dificuldade, value='Difícil')
        # Posiciona o botão de seleção na janela tkinter
        botao_dificil.grid(row=7, column=5)
        
# Define o método para tratar o clique em um botão do tabuleiro
    def clique_botao(self, linha, coluna):
        # Verifica se a célula clicada está vazia
        if self.tabuleiro[linha][coluna] == '':
            # Atualiza o tabuleiro com a marca do jogador atual
            self.tabuleiro[linha][coluna] = self.jogador
            # Atualiza a representação visual do tabuleiro na interface
            self.desenhar_tabuleiro()
            # Verifica se há um vencedor após o último movimento
            vencedor = self.verificar_vencedor()
            # Se houver um vencedor
            if vencedor:
                # Exibe uma mensagem indicando o vencedor
                messagebox.showinfo("Fim do Jogo", f"{vencedor} venceu!")
                # Reinicia o jogo
                self.reiniciar_jogo()
                # Se não houver um vencedor
            else:
                # Alterna para o próximo jogador
                self.jogador = 'O' if self.jogador == 'X' else 'X'
                # Se for a vez da IA jogar
                if self.jogador == 'O':
                    # Se a dificuldade for fácil
                    if self.variavel_dificuldade.get() == 'Fácil':
                        # Executa o movimento da IA fácil
                        self.limite_profundidade = 1
                         # Chama a função alfabeta para calcular a melhor jogada da IA
                        linha, coluna = self.alfabeta()
                        # Faz a jogada da IA no tabuleiro, colocando 'O' na posição calculada (linha, coluna)
                        self.tabuleiro[linha][coluna] = 'O'
                        # Atualiza a interface gráfica para refletir a jogada feita pela IA
                        self.desenhar_tabuleiro()
                        # Verifica se há um vencedor após a jogada da IA
                        vencedor = self.verificar_vencedor()
                        # Se houver um vencedor
                        if vencedor:
                            # Exibe uma mensagem informando quem venceu
                            messagebox.showinfo("Fim do Jogo", f"{vencedor} venceu!")
                            # Reinicia o jogo, resetando o tabuleiro e definindo 'X' como o jogador inicial
                            self.reiniciar_jogo()
                        else:
                            self.jogador = 'X'
                    # Se a dificuldade for difícil
                    else:
                        self.limite_profundidade = 3
                        # Obtém a linha e coluna da jogada calculada pela função alfabeta
                        linha, coluna = self.alfabeta()
                        # Realiza a jogada da IA na posição calculada
                        self.tabuleiro[linha][coluna] = 'O'
                        # Atualiza a representação visual do tabuleiro
                        self.desenhar_tabuleiro()
                        # Verifica se há um vencedor após a jogada da IA
                        vencedor = self.verificar_vencedor()
                        # Se houver um vencedor
                        if vencedor:
                            # Exibe uma mensagem de fim de jogo com o vencedor
                            messagebox.showinfo("Fim do Jogo", f"{vencedor} venceu!")
                            # Reinicia o jogo
                            self.reiniciar_jogo()
                            # Se não houver um vencedor
                        else:
                            # Alterna para o próximo jogador (jogador humano)
                            self.jogador = 'X'
                            
#funçao desenha tabuleiro 
    def desenhar_tabuleiro(self):
        # Percorre todas as linhas do tabuleiro
        for i in range(7):
             # Percorre todas as colunas do tabuleiro
            for j in range(7):
# Atualiza o texto do botão na posição (i, j) com o conteúdo da célula correspondente do tabuleiro
                self.botoes[i][j]['text'] = self.tabuleiro[i][j]
#funçao verificar o vencedor
    def verificar_vencedor(self):
        # Loop pelas linhas do tabuleiro
        for i in range(7):
            # Loop pelas colunas do tabuleiro
            for j in range(7):
                # Verifica se a célula não está vazia
                if self.tabuleiro[i][j] != '':
                    # Verifica se há uma sequência de quatro peças iguais na horizontal
                    if j <= 3 and self.tabuleiro[i][j] == self.tabuleiro[i][j+1] == self.tabuleiro[i][j+2] == self.tabuleiro[i][j+3]:
                        # Retorna o jogador que venceu
                        return self.tabuleiro[i][j]
                    # Verifica se há uma sequência de quatro peças iguais na vertical
                    if i <= 3 and self.tabuleiro[i][j] == self.tabuleiro[i+1][j] == self.tabuleiro[i+2][j] == self.tabuleiro[i+3][j]:
                       # Retorna o jogador que venceu
                        return self.tabuleiro[i][j]
                    # Verifica se há uma sequência de quatro peças iguais na diagonal principal
                    if i <= 3 and j <= 3 and self.tabuleiro[i][j] == self.tabuleiro[i+1][j+1] == self.tabuleiro[i+2][j+2] == self.tabuleiro[i+3][j+3]:
                       # Retorna o jogador que venceu
                        return self.tabuleiro[i][j]
                    # Verifica se há uma sequência de quatro peças iguais na diagonal secundária
                    if i <= 3 and j >= 3 and self.tabuleiro[i][j] == self.tabuleiro[i+1][j-1] == self.tabuleiro[i+2][j-2] == self.tabuleiro[i+3][j-3]:
                       # Retorna o jogador que venceu
                        return self.tabuleiro[i][j]
                    # Retorna None se não houver um vencedor
        return None

    # funçao alfa beta
    def alfabeta(self):
        # Inicializa a melhor pontuação como menos infinito
        melhor_pontuacao = float('-inf')
        # Inicializa a melhor jogada como nula
        melhor_jogada = None
        # Loop pelas linhas do tabuleiro
        for i in range(7):
            # Loop pelas colunas do tabuleiro
            for j in range(7):
                # Verifica se a célula está vazia
                if self.tabuleiro[i][j] == '':
                    # Faz a jogada temporária
                    self.tabuleiro[i][j] = 'O'
                    # Chama a função minimax para obter a pontuação da jogada
                    pontuacao = self.minimax(False, 0, float('-inf'), float('inf'))
                    # Desfaz a jogada temporária
                    self.tabuleiro[i][j] = ''
                    # Atualiza a melhor pontuação e a melhor jogada, se necessário
                    if pontuacao > melhor_pontuacao:
                        # Atualiza a melhor pontuação com a pontuação atual calculada
                        melhor_pontuacao = pontuacao
                        # Atualiza a melhor jogada com a posição (linha, coluna) atual onde a pontuação foi obtida
                        melhor_jogada = (i, j)
        # Retorna a melhor jogada encontrada
        return melhor_jogada
# funçao minimax
    def minimax(self, maximizando, profundidade, alpha, beta):
        # Verifica se há um vencedor
        vencedor = self.verificar_vencedor()
        # Se houver um vencedor
        if vencedor:
            # Retorna 1 se a IA venceu, -1 se o jogador humano venceu
            return 1 if vencedor == 'O' else -1
        # Verifica se o tabuleiro está cheio ou se a profundidade máxima foi atingida
        if profundidade == self.limite_profundidade or all(self.tabuleiro[i][j] != '' for i in range(7) for j in range(7)):
            # Retorna 0 em caso de empate ou profundidade máxima atingida
            return 0

        # Se for a vez do jogador maximizar (IA)
        if maximizando:
            # Inicializa a melhor pontuação como menos infinito
            melhor_pontuacao = float('-inf')
            # Loop pelas linhas do tabuleiro
            for i in range(7):
                # Loop pelas colunas do tabuleiro
                for j in range(7):
                    # Verifica se a célula está vazia
                    if self.tabuleiro[i][j] == '':
                        # Faz a jogada temporária
                        self.tabuleiro[i][j] = 'O'
                        # Chama a função minimax recursivamente para o jogador minimizador
                        pontuacao = self.minimax(False, profundidade + 1, alpha, beta)
                        # Desfaz a jogada temporária
                        self.tabuleiro[i][j] = ''
                        # Atualiza a melhor pontuação
                        melhor_pontuacao = max(melhor_pontuacao, pontuacao)
                        # Atualiza o valor de alpha
                        alpha = max(alpha, pontuacao)
                        # Poda alfa-beta
                        if beta <= alpha:
                            break
            # Retorna a melhor pontuação
            return melhor_pontuacao
        # Se for a vez do jogador minimizar (humano)
        else:
            # Inicializa a melhor pontuação como mais infinito
            melhor_pontuacao = float('inf')
            # Loop pelas linhas do tabuleiro
            for i in range(7):
                # Loop pelas colunas do tabuleiro
                for j in range(7):
                    # Verifica se a célula está vazia
                    if self.tabuleiro[i][j] == '':
                        # Faz a jogada temporária
                        self.tabuleiro[i][j] = 'X'
                        # Chama a função minimax recursivamente para o jogador maximizador
                        pontuacao = self.minimax(True, profundidade + 1, alpha, beta)
                        # Desfaz a jogada temporária
                        self.tabuleiro[i][j] = ''
                        # Atualiza a melhor pontuação
                        melhor_pontuacao = min(melhor_pontuacao, pontuacao)
                        # Atualiza o valor de beta
                        beta = min(beta, pontuacao)
                        # Poda alfa-beta
                        if beta <= alpha:
                            break
            # Retorna a melhor pontuação
            return melhor_pontuacao

    # Define o método para reiniciar o jogo
    def reiniciar_jogo(self):
        # Define o jogador inicial como 'X'
        self.jogador = 'X'
        # Reinicializa o tabuleiro com células vazias
        self.tabuleiro = [['' for _ in range(7)] for _ in range(7)]
        # Atualiza a representação visual do tabuleiro
        self.desenhar_tabuleiro()

# Cria uma instância da classe Tk() do tkinter
root = tk.Tk()
# Cria uma instância da classe ConnectFour, passando a janela root como parâmetro
jogo = ConnectFour(root)
# Inicia o loop principal da interface tkinter
root.mainloop()
