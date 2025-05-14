# Trabalho 2 - INE5413
# Leonardo Luiz Gambalonga Alves de Oliveira (21201250)
# Lucas Gusmão Valduga (21103505)
# Questão 3

from Q_Representacao import Graph

def Prim(graph: Graph):
    vertices = graph.GetVerticesQuantity()
    Qv = []
    Av = []
    Kv = []
    Ev = []

    for _ in range(vertices):
        Qv.append(False)
        Av.append(None)
        Kv.append(float('inf'))
        Ev.append(None)
        Ev.append(None)

    Kv[0] = 0
    while False in Qv:
        min = -1
        for i in range(vertices):
            if min == -1 and not(Qv[i]):
                min = Kv[i]
                u = i+1
            elif min > Kv[i] and not(Qv[i]):
                min = Kv[i]
                u = i+1

        uVert = graph.GetLabel(u)
        Qv[u-1] = True

        for neighbor in graph.GetNeighborhood(uVert):
            weight = graph.GetWeight(uVert, neighbor)
            
            if weight < Kv[graph.GetIndex(neighbor)-1] and [neighbor, uVert] not in Ev: 
                Ev[(graph.GetIndex(uVert)-1)*2] = [neighbor, uVert]
                Ev[(graph.GetIndex(uVert)*2)-1] = [uVert, neighbor]
                Av[graph.GetIndex(neighbor)-1] = u
                Kv[graph.GetIndex(neighbor)-1] = weight
        # print("Kv: ", Kv)
        # print("Av: ", Av)
        # print("Qv: ", Qv)
        # print("Ev: ", Ev)

        sumKv = sum(Kv)
    return sumKv, Av

if __name__ == '__main__':
    g = Graph()
    g.Read('agm_tiny.txt')
    sum, tree = Prim(g)
    print(sum)
    resTree = []
    for i in range(len(tree)):
        if tree[i] != None:
            resTree.append(f'{i+1}-{tree[i]}')
    print(", ".join(resTree))
