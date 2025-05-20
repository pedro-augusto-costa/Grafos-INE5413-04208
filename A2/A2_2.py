# Trabalho 2 - INE5413
# Leonardo Luiz Gambalonga Alves de Oliveira (21201250)
# Lucas Gusmão Valduga (21103505)
# Questão 2

from A1_1 import Graph
import sys

def OrdenacaoTopologica(graph: Graph) -> list:
    C = []  # Vértices visitados
    T = []  # Tempo inicial do vertice
    F = []  # Tempo final do vertice

    for _ in range(graph.GetVerticesQuantity()):
        C.append(False)
        T.append(float('inf'))
        F.append(float('inf'))

    time = 0  # Tempo inicial
    O = []  # Vetor de ordenação topológica

    for u in range(graph.GetVerticesQuantity()):
        if C[u] == False:
            dfsVisitOT(graph, u, C, T, F, time, O)

    return O


def dfsVisitOT(graph: Graph, v: int, C: list, T: list, F: list, time: int, O: list) -> None:
    C[v] = True  # Marca vértice como visitado
    time += 1  # Incrementa o tempo
    T[v] = time  # Salva o tempo inicial do vértice atual

    for neighbor in graph.GetNeighborhood(graph.GetLabel(v + 1)):
        if C[graph.GetIndex(neighbor) - 1] == False:
            dfsVisitOT(graph, (graph.GetIndex(neighbor)-1), C, T, F, time, O)

    time += 1  # Incrementa o tempo
    F[v] = time # Salva o tempo final do vértice atual
    O.insert(0, graph.GetLabel(v + 1)) # Insere o vértice atual no inicio da ordenação


if __name__ == "__main__":
    g = Graph()
    terminalEntry = sys.argv
    g.Read(terminalEntry[1])
    O = OrdenacaoTopologica(g)

    for vertex in range(len(O)):
        print(f'{O[vertex]}', end='')
        if vertex < len(O) - 1:
            print(' , ', end='')
