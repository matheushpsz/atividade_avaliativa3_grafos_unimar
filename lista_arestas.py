from typing import List, Tuple

class Grafo:
    def __init__(self, direcionado:bool) -> None: #criar grafo
    # Cria e retorna uma matriz de adjacência vazia e uma lista de vértices.

    # Passos:
    # 1. Criar uma lista vazia chamada matriz (para armazenar as conexões).
    # 2. Criar uma lista vazia chamada vertices (para armazenar os nomes dos vértices).
    # 3. Retornar (matriz, vertices).
        self.arestas = []
        self.vertices = []
        self.direcionado = direcionado

    def inserir_vertice(self,  vertice:str):
        """
        Adiciona um novo vértice ao grafo.

        Passos:
        1. Verificar se o vértice já existe em 'vertices'.
        2. Caso não exista:
            - Adicionar o vértice à lista 'vertices'.
            - Aumentar o tamanho da matriz:
                a) Para cada linha existente, adicionar um valor 0 no final (nova coluna).
                b) Adicionar uma nova linha com zeros do tamanho atualizado.
        """
        if vertice in self.vertices:
          return
        
        self.vertices.append(vertice)

    def inserir_aresta(self, origem, destino):
        """
        Adiciona uma aresta entre dois vértices.

        Passos:
        1. Garantir que 'origem' e 'destino' existam em 'vertices':
            - Se não existirem, chamar 'inserir_vertice' para adicioná-los.
        2. Localizar o índice da origem (i) e do destino (j).
        3. Marcar a conexão na matriz: matriz[i][j] = 1.
        4. Se nao_direcionado=True, também marcar a conexão inversa matriz[j][i] = 1.
        """
        if origem not in self.vertices:
            self.inserir_vertice(origem)
        if destino not in self.vertices:
            self.inserir_vertice(destino)
        
        self.arestas.append([origem, destino])
        if not self.direcionado:
            self.arestas.append([destino, origem])



    def remover_vertice(self, vertice):
        """
        Remove um vértice e todas as arestas associadas.

        Passos:
        1. Verificar se o vértice existe em 'vertices'.
        2. Caso exista:
            - Descobrir o índice correspondente (usando vertices.index(vertice)).
            - Remover a linha da matriz na posição desse índice.
            - Remover a coluna (mesmo índice) de todas as outras linhas.
            - Remover o vértice da lista 'vertices'.
        """
        self.vertices.remove(vertice)
        for i in range(len(self.arestas)):
            if vertice in self.arestas[i]:
                del(self.arestas[i])

    def remover_aresta(self,origem, destino):
        """
        Remove uma aresta entre dois vértices.

        Passos:
        1. Verificar se ambos os vértices existem.
        2. Localizar os índices (i e j).
        3. Remover a aresta: matriz[i][j] = 0.
        4. Se nao_direcionado=True, também remover a inversa: matriz[j][i] = 0.
        """
        if origem not in self.vertices or destino not in self.vertices:
            return

        self.arestas.remove([origem, destino])
        if not self.direcionado:
            self.arestas.remove([destino, origem])



    def existe_aresta(self, origem, destino) -> bool:
        """
        Verifica se existe uma aresta direta entre dois vértices.

        Passos:
        1. Verificar se ambos os vértices existem em 'vertices'.
        2. Obter os índices (i, j).
        3. Retornar True se matriz[i][j] == 1, caso contrário False.
        """
        if [origem, destino] in self.arestas:
            return True
        

    def vizinhos(self, vertice):
                # [       A  B  C
                #     A: [0, 0, 0]
                #     C: [0, 0, 0]
                #     B: [0, 0, 0]
                # ]
        """
        Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

        Passos:
        1. Verificar se 'vertice' existe em 'vertices'.
        2. Obter o índice 'i' correspondente.
        3. Criar uma lista de vizinhos vazia
        4. Para cada item da linha matriz[i], verificar se == 1
            - Adicionar o vértice correspondente na lista de vizinhos
        5. Retornar essa lista.
        """
        return [aresta[1] for aresta in self.arestas if aresta[0] == vertice]


    def grau_vertices(self):
        """
        Calcula o grau de entrada, saída e total de cada vértice.

        Passos:
        1. Criar um dicionário vazio 'graus'.
        2. Para cada vértice i:
            - Se o grafo for direcionado:
                - Grau de saída: somar os valores da linha i.
                - Grau de entrada: somar os valores da coluna i.
                - Grau total = entrada + saída.
            - Se não:
                - calcular apenas o grau de saida ou entrada
        3. Armazenar no dicionário no formato:
            graus[vértice] = {"saida": x, "entrada": y, "total": z} ou graus[vértice] = x.
        4. Retornar 'graus'.
        """
        graus = {}
        for v in self.vertices:
            saida = 0
            entrada = 0
            for aresta in self.arestas:
                if aresta[0] == v:
                    saida+= 1
                if aresta[1] == v:
                    entrada+= 1
            if self.direcionado:
                graus[v] = {"saida": saida, "entrada": entrada, "total": entrada +saida}
            else: 
                graus[v] = saida
        return graus



    def percurso_valido(self, caminho):
        """
        Verifica se um percurso (sequência de vértices) é possível no grafo.

        Passos:
        1. Percorrer a lista 'caminho' de forma sequencial (de 0 até len-2).
        2. Para cada par consecutivo (u, v):
            - Verificar se existe_aresta(matriz, vertices, u, v) é True.
            - Se alguma não existir, retornar False.
        3. Se todas existirem, retornar True.
        """
        for i in range(len(caminho)-2):
            if not self.existe_aresta(caminho[i], caminho[i+1]):
                return False
        return True


    def listar_vizinhos(self, vertice):
        """
        Exibe (ou retorna) os vizinhos de um vértice.

        Passos:
        1. Verificar se o vértice existe.
        2. Chamar a função vizinhos() para obter a lista.
        3. Exibir a lista formatada (ex: print(f"Vizinhos de {v}: {lista}")).
        """
        if vertice not in self.vertices:
            return []
        print(f"Vizinhos de {vertice}: {self.vizinhos(vertice)}")


    def exibir_grafo(self):
        """
        Exibe o grafo em formato de matriz de adjacência.

        Passos:
        1. Exibir cabeçalho com o nome dos vértices.
        2. Para cada linha i:
            - Mostrar o nome do vértice.
            - Mostrar os valores da linha (0 ou 1) separados por espaço.
        """
        print("entrada | saida")
        for a in self.arestas:
            print(a[0] + " "*9 + a[1])

def main():

    pass


if __name__ == "__main__":
    main()
