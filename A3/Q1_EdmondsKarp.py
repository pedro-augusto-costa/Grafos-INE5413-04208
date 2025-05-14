# Trabalho 3 - INE5413
# Leonardo Luiz Gambalonga Alves de Oliveira (21201250)
# Lucas Gusmão Valduga (21103505)
# Questão 1 

from Representacao import Graph
from queue import  Queue

def EdmondsKarp(g: Graph, s: int, t: int):
    F = 0
    Gf = g.SetGf()
    p = BuscaLargura(g, s, t, Gf)
    while p != None:
        fp = 0
        p = BuscaLargura(g, s, t, Gf)
    return F

def BuscaLargura(s: int, t: int, Gf: Graph):
    C = []
    A = []
    for _ in range(Gf.GetVerticesQuantity()):
        C.append(False)
        A.append(None)
    
    C[s] = True
    Q = Queue()
    Q.put(s)
    
    while not(Q.empty()):
        u = Q.get()
        for neighbor in Gf.GetNeighborhood(Gf.GetLabel(u)):
            if C[Gf.GetIndex(neighbor)-1] == False and Gf.GetWeight(Gf.GetLabel(u), Gf.GetLabel(neighbor)) > 0:
                C[Gf.GetIndex(neighbor)-1] = True
                A[Gf.GetIndex(neighbor)-1] = u
                if Gf.GetIndex(neighbor) == t:
                    p = [t]
                    w = t
                    while w != s:
                        w = A[w]
                        p.insert(0,w)
                    return p
                Q.put(Gf.GetIndex(neighbor))
    return None