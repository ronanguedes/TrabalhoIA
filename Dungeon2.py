import tkinter as tk
import heapq
import random

class JogoZelda(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo do Zelda")

        # Criando o mapa com valores de custo
        self.mapa =[
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 0, 0, 0, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0],
[0, 0, 10, 10, 10, 10, 10, 0, 0, 10, 0, 0, 10, 10, 10, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 10, 0, 0, 0, 0, 10, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 10, 0, 10, 10, 10, 10, 0],
[0, 0, 0, 0, 10, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 0],
[0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 10, 0, 0, 0, 0, 10, 10, 10, 10, 0],
[0, 0, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 10, 10, 10, 10, 0],
[0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 10, 0, 0],
[0, 0, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
[0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 10, 0, 0],
[0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 10, 0, 0],
[0, 0, 0, 0, 10, 0, 0, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 10, 0, 0],
[0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 10, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 10, 0, 0],
[0, 0, 0, 0, 10, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 0, 0, 0, 0, 10, 0, 0],
[0, 0, 0, 0, 10, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0],
[0, 0, 0, 0, 10, 0, 0, 0, 0, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 0, 0, 0, 0, 10, 0, 0],
[0, 0, 10, 10, 10, 10, 0, 0, 0, 10, 0, 0, 0, 10, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 10, 0, 0],
[0, 0, 10, 0, 0, 10, 0, 0, 0, 10, 0, 0, 0, 10, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 10, 0, 0],
[0, 0, 10, 0, 0, 10, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0],
[0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 10, 0, 0, 0, 0],
[0, 0, 10, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 10, 0, 0, 0, 0],
[0, 0, 10, 0, 0, 10, 10, 10, 0, 0, 10, 0, 0, 10, 0, 0, 0, 0, 10, 0, 0, 0, 0, 10, 0, 0, 0, 0],
[0, 0, 10, 0, 0, 10, 10, 10, 0, 0, 10, 0, 0, 10, 0, 0, 0, 0, 10, 0, 0, 10, 10, 10, 10, 10, 0, 0],
[0, 0, 10, 0, 0, 10, 10, 10, 10, 10, 10, 0, 10, 10, 10, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]

        # Posição inicial do jogador
        self.jogador = (15, 26)

        # Metas para o personagem alcançar
        self.metas = [(13, 3)]  # Exemplo: quatro metas em posições diferentes

        # Criando a tela
        self.canvas = tk.Canvas(self, width=1024, height=720)
        #Canvas na janela principal ou no contêiner ao qual ele pertence.
        self.canvas.pack()

        # Desenhar o mapa
        self.desenhar_mapa()

        # Iniciar o movimento automático do jogador
        self.movimento_automatico()

    def desenhar_mapa(self):
        for y, linha in enumerate(self.mapa):
            for x, custo in enumerate(linha):
                cor = self.obter_cor_celula(custo)
                #Canvas na janela principal ou no contêiner ao qual ele pertence.
                self.canvas.create_rectangle(x*25, y*25, (x+1)*25, (y+1)*25, fill=cor)

        # Desenhar jogador
        x, y = self.jogador
        self.canvas.create_oval(x*25+5, y*25+5, (x+1)*25-5, (y+1)*25-5, fill="red")

        # Desenhar metas
        for meta in self.metas:
            x, y = meta
            self.canvas.create_rectangle(x*25+10, y*25+10, (x+1)*25-10, (y+1)*25-10, fill="blue")

    def obter_cor_celula(self, custo):
        if custo == 0:
            return "gray"  # Bloqueio
        elif custo <= 10:
            return "white"
        

    def movimento_automatico(self):
        # Algoritmo A* para encontrar o caminho até a meta mais próxima
        caminho = self.a_estrela(self.jogador, self.encontrar_meta_mais_proxima())

        if caminho:
            # Atualizar a posição do jogador para o próximo nó no caminho
            self.jogador = caminho[1]
            # Atualizar a tela
            self.canvas.delete("all")
            self.desenhar_mapa()
            # Agendar o próximo movimento
            self.after(100, self.movimento_automatico)

    def a_estrela(self, inicio, fim):
        fronteira = [(0, inicio)]
        heapq.heapify(fronteira)
        custo_so_far = {inicio: 0}
        came_from = {inicio: None}

        while fronteira:
            _, atual = heapq.heappop(fronteira)

            if atual == fim:
                caminho = []
                while atual:
                    caminho.append(atual)
                    atual = came_from[atual]
                return caminho[::-1]

            for vizinho in self.vizinhos_validos(atual):
                novo_custo = custo_so_far[atual] + self.mapa[vizinho[1]][vizinho[0]]
                if vizinho not in custo_so_far or novo_custo < custo_so_far[vizinho]:
                    custo_so_far[vizinho] = novo_custo
                    prioridade = novo_custo + self.distancia(vizinho, fim)
                    heapq.heappush(fronteira, (prioridade, vizinho))
                    came_from[vizinho] = atual

    def vizinhos_validos(self, posicao):
        x, y = posicao
        vizinhos = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [vizinho for vizinho in vizinhos if self.validar_posicao(vizinho)]

    def validar_posicao(self, posicao):
        x, y = posicao
        return 0 <= x < len(self.mapa[0]) and 0 <= y < len(self.mapa) and self.mapa[y][x] > 0

    def distancia(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def encontrar_meta_mais_proxima(self):
        return min(self.metas, key=lambda meta: self.distancia(self.jogador, meta))

if __name__ == "__main__":
    app = JogoZelda()
    app.mainloop()
