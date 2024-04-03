import tkinter as tk
import heapq
import time

class JogoZelda(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo do Zelda")

        # Criando o mapa com valores de custo
        self.mapa =([
[100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150],
[100, 10, 10, 100, 10, 100, 10, 100, 10, 10, 10, 10, 10, 10, 10, 150, 150, 150, 150, 150, 150, 150, 20, 20, 20, 20, 20, 150, 150, 150, 150, 150, 150, 20, 20, 20, 20, 150, 150, 150, 150, 150],
[100, 10, 10, 100, 10, 10, 10, 100, 10, 100, 10, 10, 10, 10, 10, 10, 150, 150, 150, 150, 150, 20, 20, 20, 20, 20, 20, 20, 150, 150, 150, 150, 20, 20, 20, 20, 20, 20, 150, 150, 150, 150],
[100, 10, 100, 100, 10, 100, 10, 100, 10, 100, 10, 10, 100, 10, 10, 10, 10, 150, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 150, 150],
[100, 10, 10, 10, 10, 100, 10, 100, 10, 100, 10, 10, 100, 10, 10, 10, 10, 150, 20, 150, 150, 20, 20, 20, 20, 20, 20, 20, 150, 150, 150, 150, 20, 20, 20, 20, 20, 20, 150, 150, 150, 150],
[100, 10, 100, 100, 10, 100, 10, 100, 10, 100, 10, 100, 100, 100, 10, 10, 10, 150, 20, 150, 150, 150, 20, 20, 20, 20, 20, 150, 150, 150, 150, 180, 150, 20, 20, 20, 20, 150, 180, 150, 150, 150],
[100, 10, 100, 100, 10, 100, 10, 10, 10, 100, 10, 10, 10, 10, 10, 10, 10, 150, 20, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 180, 150, 150, 150, 150, 150, 150, 180, 150, 150, 150],
[100, 10, 100, 100, 100, 100, 10, 100, 100, 100, 10, 10, 10, 10, 10, 10, 10, 150, 20, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 180, 150, 150, 150, 150, 150, 150, 180, 150, 10, 150],
[100, 10, 10, 100, 10, 10, 10, 10, 10, 100, 10, 10, 180, 10, 10, 10, 10, 150, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 150, 150, 180, 150, 150, 150, 150, 150, 150, 180, 150, 10, 150],
[100, 100, 100, 100, 10, 100, 100, 100, 10, 10, 10, 180, 180, 180, 10, 10, 10, 150, 20, 150, 150, 150, 150, 150, 20, 150, 150, 150, 20, 150, 150, 180, 150, 150, 150, 150, 150, 150, 180, 150, 10, 150],
[100, 10, 10, 100, 10, 10, 10, 10, 10, 10, 180, 180, 180, 180, 180, 10, 10, 150, 150, 150, 100, 100, 100, 150, 150, 150, 100, 100, 100, 100, 100, 180, 10, 10, 150, 150, 10, 10, 180, 10, 10, 150],
[100, 10, 10, 100, 10, 10, 100, 10, 10, 10, 10, 180, 180, 180, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 180, 180, 180, 180, 180, 180, 180, 180, 180, 10, 10, 150],
[100, 10, 10, 100, 10, 10, 100, 10, 10, 10, 10, 10, 180, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 180, 10, 10, 100, 10, 10, 10, 10, 10, 100, 10, 150],
[100, 10, 10, 100, 10, 10, 100, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 100, 100, 100, 10, 10, 10, 100, 100, 100, 100, 10, 10, 10, 180, 10, 10, 10, 10, 10, 10, 100, 10, 100, 10, 150],
[100, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 180, 10, 100, 10, 100, 10, 100, 100, 10, 100, 10, 150],
[100, 10, 100, 100, 100, 100, 100, 10, 100, 100, 100, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 180, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 150],
[100, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 10, 10, 10, 10, 10, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150],
[100, 10, 10, 10, 10, 10, 10, 10, 10, 180, 10, 10, 100, 10, 100, 10, 10, 180, 10, 10, 10, 10, 10, 10, 10, 10, 180, 10, 10, 10, 180, 10, 150, 20, 20, 20, 20, 20, 20, 20, 20, 150],
[100, 10, 100, 10, 10, 100, 10, 10, 10, 180, 10, 10, 10, 10, 10, 10, 10, 180, 10, 100, 10, 10, 10, 10, 100, 10, 180, 180, 180, 180, 180, 10, 150, 20, 150, 20, 20, 150, 20, 20, 20, 150],
[100, 10, 100, 10, 10, 100, 10, 10, 10, 180, 10, 10, 100, 10, 100, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 180, 10, 10, 10, 10, 10, 150, 20, 150, 150, 150, 150, 150, 150, 150, 150],
[100, 10, 100, 10, 10, 100, 10, 10, 10, 180, 10, 10, 10, 10, 10, 10, 10, 180, 10, 10, 10, 10, 10, 10, 10, 10, 180, 10, 10, 10, 150, 10, 150, 20, 20, 20, 20, 20, 20, 20, 20, 150],
[100, 10, 100, 10, 10, 100, 10, 10, 10, 180, 10, 100, 100, 100, 100, 10, 10, 180, 10, 100, 10, 10, 10, 10, 100, 10, 10, 10, 10, 10, 150, 10, 150, 20, 150, 150, 150, 150, 20, 150, 150, 150],
[100, 10, 10, 10, 10, 10, 10, 10, 10, 180, 10, 10, 10, 10, 10, 10, 10, 180, 10, 10, 10, 10, 10, 10, 10, 10, 180, 10, 150, 10, 150, 10, 150, 20, 20, 20, 20, 20, 20, 20, 20, 150],
[100, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 100, 100, 100, 100, 10, 10, 180, 180, 180, 180, 10, 10, 180, 180, 180, 180, 10, 150, 10, 150, 10, 150, 150, 150, 20, 20, 150, 150, 150, 150, 150],
[100, 100, 100, 100, 100, 100, 100, 10, 10, 100, 100, 100, 100, 100, 100, 100, 100, 100, 10, 10, 10, 10, 10, 10, 10, 10, 180, 10, 150, 10, 150, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 150],
[100, 100, 100, 100, 100, 100, 10, 10, 100, 100, 100, 100, 100, 10, 100, 100, 100, 100, 100, 10, 100, 100, 100, 10, 10, 10, 180, 10, 150, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 150],
[100, 10, 100, 10, 100, 10, 10, 10, 100, 100, 100, 100, 10, 10, 10, 100, 100, 100, 100, 10, 100, 100, 100, 10, 10, 10, 180, 10, 150, 10, 10, 10, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150],
[150, 10, 10, 10, 100, 10, 10, 10, 100, 100, 100, 10, 10, 10, 10, 10, 100, 100, 100, 10, 10, 10, 10, 10, 10, 10, 180, 10, 10, 10, 10, 10, 10, 10, 10, 150, 10, 10, 10, 10, 10, 150],
[150, 10, 10, 10, 100, 10, 10, 10, 100, 100, 100, 100, 10, 10, 10, 100, 100, 100, 100, 10, 100, 10, 10, 10, 10, 10, 180, 10, 10, 10, 10, 10, 10, 10, 10, 150, 10, 10, 10, 10, 10, 150],
[150, 10, 10, 10, 10, 10, 10, 10, 10, 100, 100, 100, 100, 10, 100, 100, 100, 100, 10, 10, 100, 10, 10, 10, 10, 10, 180, 180, 180, 10, 180, 180, 180, 180, 10, 150, 10, 150, 150, 150, 150, 150],
[150, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 180, 10, 10, 10, 10, 10, 10, 10, 150],
[150, 150, 150, 150, 150, 150, 150, 150, 150, 10, 10, 10, 10, 150, 150, 150, 150, 150, 150, 150, 10, 10, 150, 150, 150, 150, 10, 10, 10, 10, 10, 10, 10, 180, 150, 150, 150, 150, 150, 150, 10, 150],
[150, 20, 20, 20, 20, 20, 20, 20, 150, 10, 10, 10, 10, 150, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 150, 10, 10, 10, 10, 10, 10, 10, 180, 150, 150, 150, 150, 150, 150, 150, 150],
[150, 20, 150, 150, 20, 20, 20, 20, 150, 10, 10, 10, 10, 150, 10, 10, 10, 10, 10, 10, 10, 10, 100, 10, 10, 150, 10, 10, 180, 180, 180, 180, 180, 180, 180, 180, 150, 150, 180, 180, 150, 150],
[150, 20, 150, 150, 20, 20, 20, 20, 150, 10, 10, 10, 10, 150, 10, 100, 10, 10, 180, 180, 10, 10, 100, 10, 10, 150, 10, 10, 180, 180, 150, 180, 180, 180, 180, 180, 150, 150, 180, 180, 150, 150],
[150, 20, 20, 20, 20, 20, 20, 20, 150, 10, 10, 150, 10, 150, 10, 10, 10, 10, 180, 180, 10, 10, 100, 10, 10, 150, 10, 10, 180, 180, 180, 180, 150, 150, 180, 180, 150, 150, 180, 180, 150, 150],
[150, 20, 20, 20, 20, 20, 20, 20, 150, 10, 10, 150, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 150, 10, 10, 180, 180, 180, 180, 150, 150, 180, 180, 150, 150, 180, 180, 150, 150],
[150, 20, 20, 20, 20, 20, 20, 150, 150, 150, 150, 150, 10, 10, 100, 10, 10, 10, 10, 10, 100, 100, 100, 10, 10, 150, 10, 10, 180, 180, 180, 180, 180, 180, 180, 180, 150, 150, 180, 180, 150, 150],
[150, 20, 20, 20, 20, 20, 20, 20, 20, 150, 150, 150, 10, 10, 100, 10, 180, 180, 180, 10, 10, 100, 10, 10, 10, 150, 10, 10, 180, 180, 180, 180, 180, 180, 180, 180, 150, 150, 180, 180, 150, 150],
[150, 20, 20, 20, 20, 20, 20, 20, 20, 150, 150, 150, 10, 10, 100, 10, 10, 10, 10, 10, 10, 100, 10, 10, 10, 150, 10, 10, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 150, 150],
[150, 20, 20, 20, 20, 20, 20, 20, 20, 20, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 150, 150, 150, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 150, 150],
[150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150],
 ])

        # Posição inicial do jogador
        self.jogador = (23, 27)

        # Metas para o personagem alcançar
        self.metas = [(5,32), (24,1), (39,17), (6,5)]  # Exemplo: quatro metas em posições diferentes

        # Lista para armazenar o caminho percorrido
        self.caminho_percorrido = []

        # Tamanho dos blocos
        self.block_size = 10  # Metade do tamanho original

        # Criando a tela
        self.canvas = tk.Canvas(self, width=len(self.mapa[0])*self.block_size, height=len(self.mapa)*self.block_size)
        self.canvas.pack()

        # Desenhar o mapa
        self.desenhar_mapa()

        # Iniciar o movimento automático do jogador
        self.movimento_automatico()

    def desenhar_mapa(self):
        for y, linha in enumerate(self.mapa):
            for x, custo in enumerate(linha):
                cor = self.obter_cor_celula(custo)
                self.canvas.create_rectangle(x*self.block_size, y*self.block_size, (x+1)*self.block_size, (y+1)*self.block_size, fill=cor)

        # Desenhar jogador
        x, y = self.jogador
        self.canvas.create_oval(x*self.block_size+1, y*self.block_size+1, (x+1)*self.block_size-1, (y+1)*self.block_size-1, fill="red", tags="jogador")

        # Desenhar metas
        for meta in self.metas:
            x, y = meta
            self.canvas.create_rectangle(x*self.block_size+3, y*self.block_size+3, (x+1)*self.block_size-3, (y+1)*self.block_size-3, fill="blue")

    def obter_cor_celula(self, custo):
        if custo <= 10:
            return "yellow"
        elif custo <= 20:
            return "brown"  # Células com custo até 175
        elif custo <= 100:
            return "green"  # Células com custo até 175
        elif custo <= 150:
            return "gray"  # Células com custo até 175
        elif custo <= 180:
            return "blue"  # Células com custo acima de 175

    def movimento_automatico(self):
        metas_perseguir = self.metas.copy()
        metas_perseguir.pop()  # Removendo a última meta
        inicio_tempo = time.time()
        while metas_perseguir:
            meta_mais_proxima = self.encontrar_meta_mais_proxima(metas_perseguir)
            caminho = self.a_estrela(self.jogador, meta_mais_proxima)

            if caminho:
                self.caminho_percorrido.extend(caminho)
                self.movimento_ate_meta(meta_mais_proxima)
                self.canvas.update()
                time.sleep(0.5)
                if meta_mais_proxima in metas_perseguir:
                    metas_perseguir.remove(meta_mais_proxima)
                self.desenhar_caminho_percorrido()
        fim_tempo = time.time()
        print("Tempo gasto para percorrer todas as metas, exceto a última:", fim_tempo - inicio_tempo)

        # Movimento para a última meta
        self.movimento_ate_meta(self.metas[-1])
        fim_tempo = time.time()
        print("Tempo gasto para percorrer a última meta:", fim_tempo - inicio_tempo)

    def movimento_ate_meta(self, meta):
        caminho = self.a_estrela(self.jogador, meta)
        custo_total = sum(self.mapa[pos[1]][pos[0]] for pos in caminho)
        print("Custo total para percorrer a meta:", custo_total)
        print("Células percorridas:")
        for posicao in caminho:
            x, y = posicao
            print(f"Célula ({x}, {y})")
            self.jogador = posicao
            self.canvas.delete("jogador")
            self.canvas.create_oval(self.jogador[0]*self.block_size+1, self.jogador[1]*self.block_size+1, (self.jogador[0]+1)*self.block_size-1, (self.jogador[1]+1)*self.block_size-1, fill="red", tags="jogador")
            self.canvas.update()
            time.sleep(0.1)

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
        return 0 <= x < len(self.mapa[0]) and 0 <= y < len(self.mapa) and self.mapa[y][x] <= 250

    def distancia(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def desenhar_caminho_percorrido(self):
        for posicao in self.caminho_percorrido:
            x, y = posicao
            self.canvas.create_rectangle(x*self.block_size+3, y*self.block_size+3, (x+1)*self.block_size-3, (y+1)*self.block_size-3, fill="orange")

    def encontrar_meta_mais_proxima(self, metas):
        return min(metas, key=lambda meta: self.distancia(self.jogador, meta))

    def desenhar_retangulo_preto(self, x, y):
        self.canvas.create_rectangle(x*self.block_size+3, y*self.block_size+3, (x+1)*self.block_size-3, (y+1)*self.block_size-3, fill="black")

if __name__ == "__main__":
    app = JogoZelda()
    app.desenhar_retangulo_preto(2, 1)  # Desenhar retângulo preto na posição (2, 1)
    app.mainloop()
