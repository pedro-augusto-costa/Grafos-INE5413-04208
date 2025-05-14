# Trabalho 2 - INE5413
# Leonardo Luiz Gambalonga Alves de Oliveira (21201250)
# Lucas Gusmão Valduga (21103505)
# Questão 1

from Q_Representacao import Graph

def ComponentesFortementeConexas(graph: Graph):
    #s = graph.GetIndex(list(graph.adjList)[0])
    vertices = graph.GetVerticesQuantity()
    Cv = [] # Vertices visitados
    Iv = [] # Inicio Tempo
    Fv = [] # Final Tempo
    Ct = [] # verticies visitados transposto
    Ca = [] # vertices visitados como resposta
    Ans = [] # resposta

    # Configurando todos os vértices
    for _ in range(vertices):
        Ct.append(False)
        Cv.append(False)
        Ca.append(False)
        Iv.append(float('inf'))
        Fv.append(0)

    for vert in range(vertices):
        if Cv[vert] == False:
            Cv = [False for _ in range(graph.GetVerticesQuantity())]
            Fv = [float('inf') for _ in range(graph.GetVerticesQuantity())]
            Iv = [float('inf') for _ in range(graph.GetVerticesQuantity())]
            s = vert + 1
            Ct, Cv, Iv, Fv = DFS(graph, s, Ct, False, Cv, Iv, Fv)


    OrdFv = Fv.copy()
    PosFv = Fv.copy()
    OrdFv = quickSortHelper(OrdFv, 0, len(OrdFv)-1)
    
    Fv = [float('inf') for _ in range(graph.GetVerticesQuantity())]
    Iv = [float('inf') for _ in range(graph.GetVerticesQuantity())]

    for i in range(len(OrdFv), 0, -1):
        s = PosFv.index(OrdFv[i-1])+1
        
        if Ct[s-1] == False:
            Ct, Cv, Iv, Fv = DFS(graph, s, Ct, True, Cv, Iv, Fv)
            for i in range(len(Ct)):
                if Ct[i] == True and Ca[i] == False:
                    Ans.append(str(i+1))
                    Ca[i] = True
            for i in range(len(Ans)):
                if not(graph.GetNeighborhoodTrans(graph.GetLabel(int(Ans[i])))):
                    for j in range(len(Ans)):
                        print(Ans[j])
                    Ans.clear()
                    break
            if not(Ans == []):
                print(",".join(Ans))
            Ans.clear()


def DFS(graph: Graph, s: int, Ct: list, 
        trans: bool, Cv: list, Iv: list, Fv: list):
    tempo = 0
    tempo, Fv, Iv, Cv = DFS_visit(graph, Cv, tempo, Iv, Fv, s, trans, Ct)
    # print("Fv: ", Fv)
    # print("Iv: ", Iv)
    # print("Cv: ", Cv)
    # print("Ct: ", Ct)
    # print("")
    return Ct, Cv, Iv, Fv

def DFS_visit(graph: Graph, Cv: list, tempo: int, 
              Iv: list, Fv: list, s: int, trans: bool, Ct: list):
    Cv[s-1] = True
    if trans:
        Ct[s-1] = True
    tempo = tempo + 1
    Iv[s-1] = tempo
    if trans:
        neighbors = graph.GetNeighborhoodTrans(graph.GetLabel(s))
    else:
        neighbors = graph.GetNeighborhood(graph.GetLabel(s))
    # print(f'visinhos {s} :  {graph.GetNeighborhood(graph.GetLabel(s))} ')
    # if not(graph.GetNeighborhood(graph.GetLabel(s))):
    #     print("a")
    for vert in neighbors:
        vert = g.GetIndex(vert)
        if Cv[vert-1] == False and not(trans):
            u = vert
            tempo, Fv, Iv, Cv  = DFS_visit(graph, Cv, tempo, Iv, Fv, u, trans, Ct)
        if Ct[vert-1] == False and trans:
            if (graph.GetNeighborhood(graph.GetLabel(vert))):
                u = vert
                tempo, Fv, Iv, Cv  = DFS_visit(graph, Cv, tempo, Iv, Fv, u, trans, Ct)
        
    tempo = tempo + 1
    Fv[s-1] = tempo
    return tempo, Fv, Iv, Cv
 
#algoritmo de quicksort
def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)
   return alist


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

if __name__ == '__main__':
    g = Graph()
    g.Read('dirigido2.txt')
    ComponentesFortementeConexas(g)

# def DFS2(graph: Graph):
#     Cv = [] # Vertices visitados
#     Iv = [] # Tempo
#     Av = [] # Antecessor do vertice no caminho definido a partir de (s)
    
#     s = graph.GetIndex(list(graph.adjList)[0])
#     vertices = graph.GetVerticesQuantity()
#     # Configurando todos os vértices
#     for _ in range(vertices):
#         Cv.append(False)
#         Iv.append(float('inf'))
#         Av.append(None)
    
#     Cv[s-1] = True
#     S = [] #pilha
#     tempo = 0
#     S.append(s)
#     while len(S) != 0:
#         tempo = tempo + 1
#         u = S.pop()
#         Iv[u-1] = tempo
#         for vert in g.GetNeighborhood(g.GetLabel(u)):
#             vert = g.GetIndex(vert)
#             if Cv[vert-1] == False:
#                 Cv[vert-1] = True
#                 Av[vert-1] = u
#                 S.append(vert)
        
#     print("Iv2: ", Iv)
#     print("Av2: ", Av)
#     print("Cv2: ", Cv)