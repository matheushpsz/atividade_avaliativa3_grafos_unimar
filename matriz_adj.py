from typing import List, Tuple

class Grafo:
    def __init__(self, direcionado:bool) -> None:
        self.direcionado = direcionado
        self.matriz = []
        self.vertices = []

    def inserir_vertice(self,  vertice:str):
        if vertice in self.vertices:
            # Já existe, não faz nada
            return
        
        self.vertices.append(vertice)
        for linha in self.matriz:
            linha.append(0)

        # Cria a nova linha (tamanho = número de vértices)
        nova_linha = [0] * len(self.vertices)
        self.matriz.append(nova_linha)

    def inserir_aresta(self, origem, destino):
        if origem not in self.vertices:
            self.inserir_vertice(origem)
        if destino not in self.vertices:
            self.inserir_vertice(destino)
        
        i_origem = self.vertices.index(origem)
        i_destino = self.vertices.index(destino)

        self.matriz[i_origem][i_destino] = 1

        if not self.direcionado:
            self.matriz[i_destino][i_origem] = 1

    def remover_vertice(self, vertice):
        # Verificar se o vértice existe
        if vertice not in self.vertices:
            print(f"Erro: Vértice '{vertice}' não encontrado.")
            return

        i = self.vertices.index(vertice)
        
        # Remover a linha
        del self.matriz[i]
        
        # Remover a coluna de todas as linhas restantes
        for linha in self.matriz:
            del linha[i]
        
        # Remover da lista de vértices
        del self.vertices[i]

    def remover_aresta(self,origem, destino):
        if origem not in self.vertices or destino not in self.vertices:
            return

        i_origem = self.vertices.index(origem)
        i_destino = self.vertices.index(destino)
        self.matriz[i_origem][i_destino] = 0

        if not self.direcionado:
            self.matriz[i_destino][i_origem] = 0

    def existe_aresta(self, origem, destino) -> bool:
        if origem not in self.vertices or destino not in self.vertices:
            return False
        
        i_origem = self.vertices.index(origem)
        i_destino = self.vertices.index(destino)

        existe = self.matriz[i_origem][i_destino] == 1 
        return existe

    def vizinhos(self, vertice):
        if vertice not in self.vertices:
            return []
        
        vizinhos = []
        i = self.vertices.index(vertice)
        
        # Pega a linha do vértice 'i'
        linha_do_vertice = self.matriz[i]
        
        # Itera pelas colunas (j) dessa linha
        for j in range(len(linha_do_vertice)):
            if linha_do_vertice[j] == 1:
                # Se self.matriz[i][j] == 1, então 'j' é vizinho
                vizinhos.append(self.vertices[j])
        
        return vizinhos

    def entradas(self, vertice): 
        if vertice not in self.vertices:
            return []
        j = self.vertices.index(vertice)
        coluna = []
        for v in self.matriz:
            coluna.append(v[j])
        return coluna

    def grau_vertices(self):
        graus = {}
        if self.direcionado:
            for index_vertice in range(len(self.vertices)):
                v = self.vertices[index_vertice]
                saida = sum(self.matriz[index_vertice])
                entrada = sum(self.entradas(v))
                graus[v] = {
                    "saida": saida,
                    "entrada": entrada,
                    "total": saida + entrada,
                }
        else: #nao direcionado
            for index_vertice in range(len(self.vertices)):
                v = self.vertices[index_vertice]
                saida = sum(self.matriz[index_vertice])
                graus[v] = saida

        return graus

    def percurso_valido(self, caminho):
        for i in range(len(caminho) - 1):
            if not self.existe_aresta(caminho[i], caminho[i+1]):
                return False
        return True

    def listar_vizinhos(self, vertice):
        if vertice not in self.vertices:
            print(f"Vértice {vertice} não existe.")
            return
        print(f"Vizinhos de {vertice}: {self.vizinhos(vertice)}")

    def exibir_grafo(self):
        if not self.vertices:
            print("Grafo vazio.")
            return

        # Imprime o cabeçalho
        print("  " + " ".join(self.vertices))
        
        # Iterar com índice seguro
        for i in range(len(self.matriz)):
            nome_vertice = self.vertices[i]
            # Converte cada item da linha para string
            linha_str = " ".join([str(x) for x in self.matriz[i]])
            print(f"{nome_vertice} {linha_str}")

def main():
    print("--- Testando Grafo Não-Direcionado ---")
    g = Grafo(direcionado=False)
    g.inserir_aresta("A", "B")
    g.inserir_aresta("B", "C")
    g.inserir_aresta("A", "C")
    g.exibir_grafo()
    
    print("\nVizinhos de A:", g.vizinhos("A")) # Esperado: ['B', 'C']
    print("Vizinhos de B:", g.vizinhos("B")) # Esperado: ['A', 'C']
    
    print("\nRemovendo vértice 'B'")
    g.remover_vertice("B")
    g.exibir_grafo()
    # Matriz deve ser 2x2 com A e C
    
    print("\nVizinhos de A (após remoção):", g.vizinhos("A")) # Esperado: ['C']

    print("\n--- Testando Grafo Direcionado ---")
    gd = Grafo(direcionado=True)
    gd.inserir_aresta("X", "Y") # X -> Y
    gd.inserir_aresta("Y", "Z") # Y -> Z
    gd.inserir_aresta("Z", "X") # Z -> X
    gd.exibir_grafo()

    print("\nVizinhos de Y (Saídas):", gd.vizinhos("Y")) # Esperado: ['Z']
    print("Graus:", gd.grau_vertices())
    # Esperado: X(S:1, E:1), Y(S:1, E:1), Z(S:1, E:1)

    print("\nPercurso X->Y->Z (Válido):", gd.percurso_valido(["X", "Y", "Z"])) # Esperado: True
    print("Percurso X->Z (Inválido):", gd.percurso_valido(["X", "Z"])) # Esperado: False

if __name__ == "__main__":
    main()