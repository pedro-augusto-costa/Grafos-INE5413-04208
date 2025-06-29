# Trabalho 3 - INE5413
# Leonardo Luiz Gambalonga Alves de Oliveira (21201250)
# Lucas Gusmão Valduga (21103505)
# Questão 1 

from A1_1 import Graph
import sys

def BFS_adapted(g: Graph, parent: list, quantityV: int) -> bool:
    V = [False]*quantityV
    
    Q = []
    Q.append(g.GetIndex("s"))
    V[g.GetIndex("s")-1] = True

    while Q:
        u = Q.pop(0)
        for neighbors in g.GetNeighborhood(g.GetLabel(u)):
            ind = g.GetIndex(neighbors)
            if V[ind-1] == False and g.GetWeight(g.GetLabel(u), g.GetLabel(ind)) > 0:
                # print("val: ", g.GetWeight(g.GetLabel(u), g.GetLabel(ind)))
                # print("ind: ", ind)
                Q.append(g.GetIndex(neighbors))
                V[ind-1] = True
                parent[ind-1] = u

                if neighbors == "t":  #verificar se ta certo isso
                    return True
    return False

def weightValue(u: int, v: int, path_flow: int):
    weight = g.GetWeight(g.GetLabel(v), g.GetLabel(u))
    if weight == float("inf"):
        return path_flow
    else:
        return path_flow + weight

def edmondsKarp(g: Graph):
    quantityV = g.GetVerticesQuantity()
    parent = [-1]*quantityV

    max_flow = 0

    while BFS_adapted(g, parent, quantityV):
        path_flow = float("Inf")
        # print("parent", parent)
        s = g.GetIndex("t")
        while (s != g.GetIndex("s")):
            # print("parent[s-1]: ", parent[s-1])
            path_flow = min(path_flow, (g.GetWeight(g.GetLabel(parent[s-1]), g.GetLabel(s))))
            # print("miN", min(path_flow, (g.GetWeight(g.GetLabel(parent[s-1]), g.GetLabel(s)))))
            # print("cam", (g.GetWeight(g.GetLabel(parent[s-1]), g.GetLabel(s))))
            # print("path_flow", path_flow)
            # print(parent)
            # print("s", s)
            # sleep(3)
            s = parent[s-1]
        
        max_flow += path_flow

        v = g.GetIndex("t")
        while (v != g.GetIndex("s")):
            u = parent[v-1]
            g.SetWeight(g.GetLabel(u), g.GetLabel(v), (g.GetWeight(g.GetLabel(u), g.GetLabel(v))-path_flow))  
            g.SetWeight(g.GetLabel(v), g.GetLabel(u), weightValue(u, v, path_flow))
            v = parent[v-1]
            
    return max_flow

if __name__ == '__main__':
    g = Graph()
    terminalEntry = sys.argv
    g.Read(terminalEntry[1])
    print(edmondsKarp(g))
