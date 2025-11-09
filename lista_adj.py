def criar_grafo():
    """
    Retorna um novo grafo vazio.
    Passos:
    1. Criar um dicionário vazio: {}
    2. Retornar o dicionário (representa o grafo)
    """
    return {}
    

def inserir_vertice(grafo, vertice):
    if vertice in grafo:
        return
    grafo[vertice] = []
    """
    Insere um vértice no grafo, sem arestas iniciais.
    Passos:
    1. Verificar se 'vertice' já é chave em grafo.
    2. Se não for, criar entrada grafo[vertice] = []
    3. Se já existir, não fazer nada (ou avisar)
    """



def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)
    grafo[origem].append(destino)
    if nao_direcionado:
        grafo[destino].append(origem)
    """
    Adiciona aresta entre origem e destino.
    Passos:
    1. Garantir que 'origem' e 'destino' existam no grafo (inserir se necessário).
    2. adicionar destino como vizinho de origem (append).
    3. Se for Nâo Direcionado, também:
         - adicionar origem como vizinho de destino
    """

    
def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    return []
    """
    Retorna a lista de vizinhos de 'vertice'.
    Passos:
    1. Se 'vertice' estiver em grafo, retornar grafo[vertice] (lista).
    2. Se não existir, retornar lista vazia ou sinalizar erro.
    """

def listar_vizinhos(grafo, vertice):
    """
    Função semântica: imprimir/retornar os vizinhos de 'vertice'.
    Passos:
    1. Obter lista = vizinhos(grafo, vertice)
    2. Retornar/imprimir essa lista (ou informar que o vértice não existe)
    """
    lista = vizinhos(grafo, vertice)
    if lista == []:
        print("nao existe vizinho")
        return
    
    print(f"vizinhos de {vertice}: {str(lista)}")

        

def exibir_grafo(grafo):
    """
    Exibe o grafo em forma legível (lista de adjacência).
    Passos:
    1. Para cada vertice em ordem
         - imprimir: vertice -> vizinhos
    """
    for vertice in grafo:
        print(f"{vertice} -> {str(grafo[vertice])}")

def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    """
    Remove a aresta entre origem e destino.
    Passos:
    1. Verificar se 'origem' existe; se não, terminar.
    2. Se destino estiver em grafo[origem], remover essa ocorrência.
    3. Se for não direcionado, também:
         - verificar se 'destino' existe e remover 'origem' de grafo[destino] se presente.
    """
    if origem in grafo:
        grafo[origem].remove(destino)
    if destino in grafo and nao_direcionado:
        grafo[destino].remove(origem)


def remover_vertice(grafo, vertice, nao_direcionado=True):
    """
    Remove um vértice e todas as arestas que o tocam.
    Passos:
    1. Verificar se 'vertice' existe em grafo; se não, terminar.
    2. Para cada outro vertice no grafo:
         - se 'vertice' estiver na lista de vizinhos, remover essa aresta.
    3. Remover o vertice do grafo
    4. Opcional: retornar confirmação/erro.
    """
    grafo.remove(vertice)
    for v in grafo:
        lista_adj = grafo[v]
        for adjacente in lista_adj:
            if adjacente == vertice:
                grafo[v].remove(adjacente)

    
def existe_aresta(grafo, origem, destino):
    """
    Verifica se existe aresta direta origem -> destino.
    Passos:
    1. Verificar se 'origem' é chave no grafo.
    2. Retornar True se 'destino' estiver em grafo[origem], caso contrário False.
    """
    if origem in grafo:
        return destino in grafo[origem]
    
    # {
    #     "A": ["B", "C"]
    #     "B"> ["A"]
    # }

def grau_vertices(grafo):
    """
    Calcula e retorna o grau (out, in, total) de cada vértice.
    Passos:
    1. Inicializar um dict de graus vazia
    2. Para cada vertice, colocar no dict uma estrutura com in, out e total zerado
    3. Para cada u em grafo:
         - out_degree[u] = tamanho de vizinhos
         - para cada v em grafo:
            - verificar se u está na lista de vizinho de v,
            - caso esteja, adicionar +1 para o grau de entrada de u
    4. Calcular o grau total somando entrada + saida
    5. Retornar uma estrutura contendo out,in,total por vértice (ex: dict de tuplas).
    """
    degrees = {}
    for vertice in grafo:
        out = len(grafo[vertice])
        in_d = 0
        for v in grafo:
            for chegando_em in grafo[v]:
                if chegando_em == vertice:
                    in_d+=1
        total = in_d + out
        degrees[vertice] = (in_d, out, total)
        return degrees


def percurso_valido(grafo, caminho):
    """
    Verifica se uma sequência específica de vértices (caminho) é válida:
    i.e., se existem arestas consecutivas entre os nós do caminho.
    Passos:
    1. Se caminho tiver tamanho < 2, retornar True (trivial).
    2. Para i de 0 até len(caminho)-2:
         - origem = caminho[i], destino = caminho[i+1]
         - se não existe_aresta(grafo, origem, destino): retornar False
    3. Se todas as arestas existirem, retornar True.
    """
    if len(caminho) <2: return True
    for i in range(caminho-2):
        origem = caminho[i], destino = caminho[i+1]
        if not existe_aresta(grafo, origem, destino):
            return False
    return True

def pedir_vertice(complemento: str = "") -> str:
    t = "insira a aresta desejada"
    if len(complemento) > 0: t+= " (" + complemento +")"
    t += ": "
    aresta = input(t).split()
    if len(aresta) == 0:
        return ""
    return aresta[0]


def main():
    """
    Crie um menu onde seja possível escolher qual ação deseja realizar
    ex:
        1 - Mostrar o Grafo
        2 - inserir vertice
        3 - inserir aresta
        4 - remover vértice.
        ....
    """
    grafo = criar_grafo()
    while True:
        print("\n\n\n=================================")
        resp = int(input("\n1 - Mostrar o Grafo\n2 - inserir vertice\n3 - inserir aresta\n4 - remover vértice\ninsira a opcao desejada: "))
        if resp >4 or resp<1:
            print("Fim")
            break
        if resp == 1:
            exibir_grafo(grafo)
        elif resp == 2:
            vertice= pedir_vertice()
            if vertice == "":
                print("valor invalido")
                continue
            inserir_vertice(grafo, vertice)
        elif resp == 3:
            v1 = pedir_vertice("origem")
            if v1 == "":
                print("valor invalido")
                continue
            v2 = pedir_vertice("destino")
            if v2 == "":
                print("valor invalido")
                continue
            inserir_aresta(grafo, v1, v2)
            print("aresta inserida com sucesso")
        elif resp == 4:
            v1 = pedir_vertice("origem")
            if v1 == "":
                print("valor invalido")
                continue
            v2 = pedir_vertice("destino")
            if v2 == "":
                print("valor invalido")
                continue
            remover_aresta(grafo, v1, v2)

if __name__ == "__main__":
    main()