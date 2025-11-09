from typing import List, Tuple

class Grafo:
    def __init__(self, direcionado:bool) -> None: #criar grafo
        """
        Cria um grafo vazio baseado em Lista de Arestas.
        
        Passos:
        1. Criar uma lista vazia chamada 'arestas'.
        2. Criar uma lista vazia chamada 'vertices'.
        """
        self.arestas = []
        self.vertices = []
        self.direcionado = direcionado

    def inserir_vertice(self,  vertice:str):
        """
        Adiciona um novo vértice ao grafo (apenas à lista de vértices).

        Passos:
        1. Verificar se o vértice já existe em 'vertices'.
        2. Caso não exista, adicionar o vértice à lista 'vertices'.
        """
        if vertice in self.vertices:
          return
        
        self.vertices.append(vertice)

    def inserir_aresta(self, origem, destino):
        """
        Adiciona uma aresta (um par) à lista de arestas.

        Passos:
        1. Garantir que 'origem' e 'destino' existam em 'vertices' (chama 'inserir_vertice').
        2. Adicionar o par [origem, destino] à lista 'self.arestas'.
        3. Se nao_direcionado=True, também adicionar [destino, origem].
        """
        if origem not in self.vertices:
            self.inserir_vertice(origem)
        if destino not in self.vertices:
            self.inserir_vertice(destino)
        
        # Evita duplicatas simples
        if [origem, destino] not in self.arestas:
            self.arestas.append([origem, destino])
            
        if not self.direcionado and [destino, origem] not in self.arestas:
            self.arestas.append([destino, origem])


    def remover_vertice(self, vertice):
        """
        Remove um vértice e todas as arestas associadas a ele.

        Passos:
        1. Verificar se o vértice existe em 'vertices'.
        2. Caso exista:
            - Remover o vértice da lista 'vertices'.
            - Recriar a 'self.arestas' (com list comprehension) 
              mantendo apenas as arestas que NÃO contêm o 'vertice'.
        """
        if vertice not in self.vertices:
            return
            
        self.vertices.remove(vertice)
        
        # Esta é a forma segura de remover itens
        # Recria a lista mantendo apenas arestas que não tocam o vértice
        self.arestas = [
            aresta for aresta in self.arestas 
            if vertice not in aresta
        ]

    def remover_aresta(self,origem, destino):
        """
        Remove uma aresta entre dois vértices.

        Passos:
        1. Define o par [origem, destino].
        2. Verifica se o par existe em 'self.arestas' e o remove.
        3. Se nao_direcionado=True, faz o mesmo para [destino, origem].
        """
        aresta_direta = [origem, destino]
        aresta_inversa = [destino, origem]

        # Verificar antes de remover para evitar ValueError
        if aresta_direta in self.arestas:
            self.arestas.remove(aresta_direta)
            
        if not self.direcionado and aresta_inversa in self.arestas:
            self.arestas.remove(aresta_inversa)


    def existe_aresta(self, origem, destino) -> bool:
        """
        Verifica se existe uma aresta direta entre dois vértices.

        Passos:
        1. Retornar True se [origem, destino] estiver em 'self.arestas'.
        2. Caso contrário, retornar False.
        """
        if [origem, destino] in self.arestas:
            return True
        # Retornar False se não encontrar
        return False
        

    def vizinhos(self, vertice):
        """
        Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

        Passos:
        1. Criar uma lista de vizinhos vazia.
        2. Varre 'self.arestas':
           - Se aresta[0] == vertice, adiciona aresta[1] aos vizinhos.
        3. Retornar essa lista.
        """
        # A implementação original com list comprehension estava correta
        return [aresta[1] for aresta in self.arestas if aresta[0] == vertice]


    def grau_vertices(self):
        """
        Calcula o grau de entrada, saída e total de cada vértice.

        Passos:
        1. Criar um dicionário vazio 'graus'.
        2. Para cada vértice v:
            - Varre 'self.arestas' inteira (O(E)):
                - Se aresta[0] == v, incrementa 'saida'.
                - Se aresta[1] == v, incrementa 'entrada'.
        3. Armazenar no dicionário e retornar.
        """
        graus = {}
        for v in self.vertices:
            saida = 0
            entrada = 0
            for aresta in self.arestas:
                if aresta[0] == v:
                    saida += 1
                if aresta[1] == v:
                    entrada += 1
            
            if self.direcionado:
                graus[v] = {"saida": saida, "entrada": entrada, "total": entrada + saida}
            else: 
                # Em grafos não direcionados, entrada e saída são iguais
                graus[v] = saida 
        return graus


    def percurso_valido(self, caminho):
        """
        Verifica se um percurso (sequência de vértices) é possível no grafo.

        Passos:
        1. Percorrer a lista 'caminho' de forma sequencial (de 0 até len-2).
        2. Para cada par consecutivo (u, v):
            - Verificar se existe_aresta(u, v) é True.
            - Se alguma não existir, retornar False.
        3. Se todas existirem, retornar True.
        """
        # O loop deve ser range(len(caminho) - 1)
        for i in range(len(caminho) - 1):
            if not self.existe_aresta(caminho[i], caminho[i+1]):
                return False
        return True


    def listar_vizinhos(self, vertice):
        """
        Exibe (ou retorna) os vizinhos de um vértice.
        """
        if vertice not in self.vertices:
            print(f"Vértice {vertice} não existe.")
            return
        
        print(f"Vizinhos de {vertice}: {self.vizinhos(vertice)}")


    def exibir_grafo(self):
        """
        Exibe o grafo em formato de lista de arestas.
        """
        if not self.arestas:
            print("Grafo vazio.")
            return
            
        print("Origem   -> Destino")
        print("-------------------")
        for a in self.arestas:
            print(f"{a[0]:<8} -> {a[1]}") # Formatação para alinhar

def main():
    # Você pode adicionar testes aqui para esta versão
    g = Grafo(direcionado=False)
    g.inserir_aresta("A", "B")
    g.inserir_aresta("B", "C")
    g.inserir_aresta("A", "C")
    
    print("--- Grafo Não-Direcionado (Lista de Arestas) ---")
    g.exibir_grafo()
    
    print("\nVizinhos de A:", g.vizinhos("A"))
    print("Graus:", g.grau_vertices())
    
    print("\nRemovendo vértice 'B'")
    g.remover_vertice("B")
    g.exibir_grafo()
    
    print("\n--- Teste de Percurso ---")
    gd = Grafo(direcionado=True)
    gd.inserir_aresta("X", "Y")
    gd.inserir_aresta("Y", "Z")
    
    print("Percurso X->Y->Z (Válido):", gd.percurso_valido(["X", "Y", "Z"]))
    print("Percurso X->Z (Inválido):", gd.percurso_valido(["X", "Z"]))


if __name__ == "__main__":
    main()