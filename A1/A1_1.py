# Trabalho 1 - INE5413
# Pedro Augusto Costa (19103248)
# Questão 1 

import sys

class Graph():  #geração de grafos por dicionarios.
    def __init__(self) -> None:
        self.adjList = {} # utilizando lista de adjacencias, criando o grafo como um dicionario vazio 
        self.numEdges = 0
    
    def GetVerticesQuantity(self) -> int: #pega a quantidade de vertices
        return len(self.adjList)
    
    def GetEdgesQuantity(self) -> int: #quantidade de arestas
        return self.numEdges
    
    def GetDegree(self, vertex: str) -> int:   #pega o "degree" do vertice.
        return len(self.adjList[vertex]['neighborhood'])
    
    def GetLabel(self, index: int) -> str: # rotulo
        for v in self.adjList.items():
            if v[1]['index'] == index:
                return v[0]
    
    def GetIndex(self, label: str) -> int: # index do dicionario como um index
        return self.adjList[label]['index']
    
    def GetNeighborhood(self, vertex: str) -> list: # Vizinhança
        return list(self.adjList[vertex]['neighborhood'].keys()) 
    
    def VerifyEdge(self, vertexU: str, vertexV: str) -> bool: #verifica se um vertice é considerado vizinho de outro
        if vertexV in self.adjList[vertexU]['neighborhood']:
            return True
        else:
            return False
    
    def GetWeight(self, vertexU: str, vertexV: str) -> float: #peso das arestas
        try:
            weight = self.adjList[vertexU]['neighborhood'][vertexV]
        
        except:
            weight = float('inf')
            
        return weight
    
    def Read(self, file) -> None: # essa função é para ler os arquivos do professor
        with open(file, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            n = int(lines[0].split()[1]) # numero de vertices
            
            # Lendo vertices
            # Usado o numero de vertices para determinar o laço
            for i in range(1, n+1): 
                vertexLabel = (lines[i].strip().split(" ", 1))[1]
                
                # dicionario idenficado pelo rotulo do vertice, armazena sua vizinhança e seu index
                self.adjList.update({vertexLabel: {'neighborhood': {} , 'index': i}})
            
            # Lendo arestas
            # Lendo array de linhas do arquivo a partir de n+2
            # n+2 = numero de vertices + linhas com "*vertices" "*arestas"
            for line in lines[n+2:]: #
                self.numEdges += 1 # contando o numero de arestas
                
                vertexU, vertexV, weight = line.split()
                weight = float(weight)

                vertexULabel = self.GetLabel(int(vertexU))
                vertexVLabel = self.GetLabel(int(vertexV))
                
                # dicionario de vizinhança, armazena o rotulo do vertice vizinho e o peso da aresta
                self.adjList[vertexULabel]['neighborhood'].update({vertexVLabel: weight}) 
                self.adjList[vertexVLabel]['neighborhood'].update({vertexULabel: weight})
                
if __name__ == '__main__': # aqui é apenas um teste interno 
    g = Graph()
    terminalEntry = sys.argv
    g.Read(terminalEntry[1])
    # Esses teste utilizam o grafo "fln_pequena.net"
    print(g.adjList)
    print(g.GetVerticesQuantity())
    print(g.GetEdgesQuantity())
    print(g.GetDegree('"Universidade Federal de Santa Catarina"'))
    print(g.GetIndex('"Elevado Rio Tavares"'))
    print(g.GetLabel(4))
    print(g.GetNeighborhood('"Lagoa da Conceição"'))
    print(g.VerifyEdge('"Elevado Rio Tavares"','"Lagoa da Conceição"'))
    print(g.GetWeight('"Beira Mar Norte"','"Elevado Rio Tavares"'))