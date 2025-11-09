def criar_grafo():
    """
    Retorna um novo grafo vazio.
    """
    return {}
    

def inserir_vertice(grafo, vertice):
    """
    Insere um vértice no grafo, sem arestas iniciais.
    """
    if vertice in grafo:
        return
    grafo[vertice] = []


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    """
    Adiciona aresta entre origem e destino.
    """
    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)
    
    # Evita arestas duplicadas se não for um multigrafo
    if destino not in grafo[origEM]:
        grafo[origem].append(destino)
        
    if nao_direcionado:
        if origem not in grafo[destino]:
            grafo[destino].append(origem)

    
def vizinhos(grafo, vertice):
    """
    Retorna a lista de vizinhos de 'vertice'.
    """
    if vertice in grafo:
        return grafo[vertice]
    return []

def listar_vizinhos(grafo, vertice):
    """
    Função semântica: imprimir/retornar os vizinhos de 'vertice'.
    """
    lista = vizinhos(grafo, vertice)
    if not lista: # verificar se a lista está vazia
        print(f"O vértice '{vertice}' não existe ou não tem vizinhos.")
        return
    
    print(f"vizinhos de {vertice}: {str(lista)}")

        

def exibir_grafo(grafo):
    """
    Exibe o grafo em forma legível (lista de adjacência).
    """
    if not grafo:
        print("O grafo está vazio.")
        return
        
    for vertice in grafo:
        print(f"{vertice} -> {str(grafo[vertice])}")

def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    """
    Remove a aresta entre origem e destino.
    """
    #Verificar se a aresta existe antes de remover
    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)
    
    #Verificar também no sentido oposto
    if nao_direcionado and destino in grafo and origem in grafo[destino]:
        grafo[destino].remove(origem)


def remover_vertice(grafo, vertice, nao_direcionado=True): 
    """
    Remove um vértice e todas as arestas que o tocam.
    """
    # Verificar se existe
    if vertice not in grafo:
        return

    # Remover o vértice (remove arestas DE SAÍDA)
    # Usar .pop() é seguro e remove a chave
    grafo.pop(vertice, None) 

    # Remover arestas DE ENTRADA (de forma segura)
    for v in grafo:
        # Usamos list comprehension para criar uma NOVA lista sem o vértice
        grafo[v] = [adj for adj in grafo[v] if adj != vertice]

    
def existe_aresta(grafo, origem, destino):
    """
    Verifica se existe aresta direta origem -> destino.
    """
    if origem in grafo:
        return destino in grafo[origem]
    
    return False


def grau_vertices(grafo):
    """
    Calcula e retorna o grau (out, in, total) de cada vértice.
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
        degrees[vertice] = {"entrada": in_d, "saida": out, "total": total}
    
    return degrees


def percurso_valido(grafo, caminho):
    """
    Verifica se uma sequência específica de vértices (caminho) é válida.
    """
    if len(caminho) < 2: 
        return True
    
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i+1]
        
        if not existe_aresta(grafo, origem, destino):
            return False
    return True

def pedir_vertice(complemento: str = "") -> str:
    t = "insira o vertice desejado"
    if len(complemento) > 0: t+= " (" + complemento +")"
    t += ": "
    
    # .strip() remove espaços
    # e .split() pega o primeiro item
    entrada = input(t).strip() 
    if not entrada:
        return ""
    
    # Pega apenas o primeiro item se o usuário digitar "A B"
    return entrada.split()[0]


def main():
    """
    Menu para interação com o grafo.
    """
    grafo = criar_grafo()
    while True:
        print("\n\n\n=================================")
        try:
            resp = int(input("\n1 - Mostrar o Grafo\n2 - inserir vertice\n3 - inserir aresta\n4 - remover aresta\ninsira a opcao desejada (0 para Sair): "))
        except ValueError:
            print("Opção inválida. Digite um número.")
            continue
            
        if resp == 0:
            print("Fim")
            break
            
        if resp == 1:
            exibir_grafo(grafo)
            
        elif resp == 2:
            vertice = pedir_vertice()
            if vertice == "":
                print("valor invalido")
                continue
            inserir_vertice(grafo, vertice)
            print(f"Vértice '{vertice}' inserido.")
            
        elif resp == 3:
            v1 = pedir_vertice("origem")
            if v1 == "":
                print("valor invalido")
                continue
            v2 = pedir_vertice("destino")
            if v2 == "":
                print("valor invalido")
                continue
            # Vamos assumir que o grafo é direcionado por padrão no menu
            inserir_aresta(grafo, v1, v2, nao_direcionado=False) 
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
            print(f"Aresta {v1}->{v2} removida (se existia).")
        
        else:
            print("Opção não reconhecida.")


if __name__ == "__main__":
    main()