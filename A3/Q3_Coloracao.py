# Trabalho 3 - INE5413
# Leonardo Luiz Gambalonga Alves de Oliveira (21201250)
# Lucas Gusmão Valduga (21103505)
# Questão 3

from Representacao import Graph

def welshPowell(g: Graph):
    V = []
    Vquantity = g.GetVerticesQuantity()

    for i in range(1, Vquantity+1):             # ordena vértices por grau decrescentemente
        vert = g.GetDegree(g.GetLabel(i))
        if i == 1:
            V.append([i, vert])
        else:
            for j in range(len(V)):
                if vert > V[j][1]:
                    V.insert(j, [i, vert])
                    break
                elif (j == len(V)-1):
                    V.append([i, vert])
    # print(V)
    C = []      # lista de cores
    for i in range(1, Vquantity+1):         # adiciona possíveis cores para cada vértice -> ver algoritmo de welsh & powell
        ci = []
        for j in range(1, V[0][1]+1):
            ci.append(j)
            if i == j:
                break
        C.append(ci)
    

    #V[0][1] são o numero de cores disponíveis (mas ainda nao pode ser considerado minimo)
    Vcolor = [1]

    for i in range(0, Vquantity):          # parte mais complicada do código
        for j in range(i, Vquantity):                                       # começa assumindo que o vértice com maior grau é cor 1
            if g.VerifyEdge(g.GetLabel(V[i][0]), g.GetLabel(V[j][0])):      # verifica quais vértices tem contato com ele e remove o 1 de suas respectivas listas de cores possíves, já que o 1 não é mais uma cor possível
                C[j].remove(Vcolor[i])                                      # passa para o próximo vértice, o próximo vértice vai receber a primeira cor de sua lista
                                                                            # não se verifica os vértices anteriores
        if i < Vquantity-1:         
            Vcolor.append(C[i+1][0])
    colors = [0]*Vquantity
    for i in range(0, Vquantity):
        colors[(V[i][0])-1] = Vcolor[i] 
        pass
    return len(set(Vcolor)), colors

if __name__ == '__main__':
    g = Graph()
    g.Read('cor3.net')
    color, colors = welshPowell(g)

    print("Quantidade da coloração mínima: ", color)
    print("Cores em cada vértice: ")
    color_list_str = ', '.join(f'{i+1}: {colors[i]}' for i in range(len(colors)))
    print(color_list_str)
