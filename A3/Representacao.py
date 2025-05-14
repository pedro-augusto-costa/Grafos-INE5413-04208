# Trabalho 1 - INE5413
# Leonardo Luiz Gambalonga Alves de Oliveira (21201250)
# Lucas Gusmão Valduga (21103505)
# Questão 1 

class Graph():
    def __init__(self) -> None:
        self.adjList = {} # lista de adjacencias
        self.numEdges = 0
        self.labels = []
        self.arcTrans = {}
        self.directed = False

    def GetVerticesQuantity(self) -> int:
        return len(self.adjList)
    
    def GetEdgesQuantity(self) -> int:
        return self.numEdges
    
    def GetDegree(self, vertex: str) -> int:
        return len(self.adjList[vertex]['neighborhood'])
    
    def GetLabel(self, index: int) -> str:
        return self.labels[index - 1]
    
    def GetIndex(self, label: str) -> int:
        for i in range(len(self.labels)):
            if label == self.labels[i]:
                return i+1
    
    def GetNeighborhood(self, vertex: str) -> list:
        return list(self.adjList[vertex]['neighborhood'].keys()) 
    
    def GetNeighborhoodTrans(self, vertex: str) -> list:
        return list(self.arcTrans[vertex]['neighborhood'].keys())
    
    def VerifyEdge(self, vertexU: str, vertexV: str) -> bool:
        if vertexV in self.adjList[vertexU]['neighborhood']:
            return True
        else:
            return False
    
    def GetWeight(self, vertexU: str, vertexV: str) -> float:
        try:
            weight = self.adjList[vertexU]['neighborhood'][vertexV]
        
        except:
            weight = float('inf')
            
        return weight
    
    def SetWeight(self, vertexU: str, vertexV: str, weight: float):
        self.adjList[vertexU]['neighborhood'][vertexV] = weight
        return
    
    def Read(self, file) -> None:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            n = int(lines[0].split()[1]) # numero de vertices
            
            # Lendo vertices
            # Usado o numero de vertices para determinar o laço
            for i in range(1, n+1): 
                vertexLabel = lines[i].split()[1:]
                vertexLabel = ' '.join(vertexLabel)
                self.labels.insert(i, vertexLabel)
                
                # dicionario idenficado pelo rotulo do vertice, armazena sua vizinhança e seu index
                self.adjList.update({vertexLabel: {'neighborhood': {}}})
                self.arcTrans.update({vertexLabel: {'neighborhood': {}}})
            
            if "*arcs" in lines[n+1]: 
                self.directed = True
            # Lendo arestas
            # Lendo array de linhas do arquivo a partir de n+2
            # n+2 = numero de vertices + linhas com "*vertices" "*arestas"
            for line in lines[n+2:]: #
                self.numEdges += 1 # contando o numero de arestas
                
                vertexU, vertexV, weight = line.split()
                vertexU = int(vertexU)
                vertexV = int(vertexV)
                weight = float(weight)
                
                # dicionario de vizinhança, armazena o rotulo do vertice vizinho e o peso da aresta
                self.adjList[self.GetLabel(vertexU)]['neighborhood'].update({self.GetLabel(vertexV): weight}) 
                self.arcTrans[self.GetLabel(vertexV)]['neighborhood'].update({self.GetLabel(vertexU): weight})
                
                if not(self.directed):
                    self.adjList[self.GetLabel(vertexV)]['neighborhood'].update({self.GetLabel(vertexU): weight})
                
if __name__ == '__main__':
    g = Graph()
    g.Read('fln_pequena.net')
    print(g.adjList)
    print(g.GetVerticesQuantity())
    print(g.GetEdgesQuantity())
    print(g.GetDegree('"Ponte"'))
    print(g.GetIndex('"Praia Mole"'))
    print(g.GetLabel(4))
    print(g.GetNeighborhood('"Universidade Federal de Santa Catarina"'))
    print(g.VerifyEdge('"Universidade Federal de Santa Catarina"','"Parque Municipal do Córrego Grande"'))
    print(g.GetWeight('"Lagoa da Conceição"','"Elevado Rio Tavares"'))