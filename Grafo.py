class Grafo:
    #Implementa Grafos nao direcionados ponderados

    def __init__(self, vertices):
        self.vertices = vertices
        self.listaAdj = [[] for i in range(self.vertices+1)] #conteudo das linhas em branco, vertices = numero de linhas

    def adicionaAresta(self, u, v, peso):
        self.listaAdj[u].append([v, peso]) #adiciona v e o peso na linha/vertice u
        self.listaAdj[v].append([u, peso]) #adiciona u e o peso na linha/vertice v

    def imprimeGrafo(self, arqOut):
        for i in range(1,self.vertices+1):
            print(f'{i}:', end='  ')
            arqOut.write(f'{i}: ')
            for j in self.listaAdj[i]:
                print(f'{j} -', end='  ')
                arqOut.write(f'{j} - ')
            print('')
            arqOut.write('\n')
        print('')
        arqOut.write('\n')


    '''def exibeInformacoes(self, v):
        print(f'Grafo de Ordem: {self.ordemGrafo()}')
        print(f'Grafo de tamanho: {self.tamanhoGrafo()}')
        print(f'Vizinhos do vértice {v}: {self.retornaVizinhos(v)}')
        print(f'Grau do vértice {v}: {self.grauVertice(v)}')
        print(f'Lista da busca: {self.dfs(v)}')
        print(f'Número de componentes conexas: {self.NumberOfconnectedComponents()}')
        print(f'Vértices de componentes conexas: {self.connectedComponents()}')'''
                
    def ordemGrafo(self):
        return self.vertices

    def tamanhoGrafo(self): #tamanho = nVértices + nArestas (n arestas = Soma dos Graus dos vertices/2)
        somaGraus = 0
        for i in range(self.vertices):
            somaGraus += self.grauVertice(i)

        return int(self.vertices + somaGraus/2)

    def retornaVizinhos(self, u):
        vizinhos = []
        listaVizinhos = self.listaAdj[u]
        i=0
        while (i<len(listaVizinhos)):
            vizinhos.append(listaVizinhos[i][0])
            i+=1
        return vizinhos

    def grauVertice(self, u): #Grau = n de vertices ligados a ele/ n de vizinhos
        return len(self.retornaVizinhos(u))

    @staticmethod
    def leArquivo(nomeArquivo): #Função para ler e criar grafo a partir de arquivo, retorna o grafo criado
        with open(nomeArquivo, 'r') as arq: #Para chamar utilize nomeGrafo = Grafo.leArquivo(nomeArquivo)
            vertices = arq.readline() #lê a primeira linha
            vertices = int(vertices)
            g = Grafo(vertices) #cria o grafo G com a quantidade de vértices
            for line in arq:
                u, v, peso = line.rstrip('\n').split(' ')
                g.adicionaAresta(int(u), int(v), int(peso))
        return g
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.vertices+1):
            visited.append(False)
        for v in range(self.vertices+1):
            if visited[v] == False:
                temp = []
                #cc.append(self.DFSUtil(temp, v, visited))
                cc.append(self._DFS(v, visited, temp))
        return cc[1:]
    def NumberOfconnectedComponents(self):
         
        # marcar todos vertices como n visitados
        visited = [False for i in range(self.vertices+1)]
         
        # armazenar o numero de componentes conectados
        count = 0
        temp = []
        for v in range(self.vertices+1):
            if (visited[v] == False):
                #self.DFSUtil2(v, visited)
                self._DFS(v, visited, temp)
                count += 1

        return count-1

    def _DFS(self, s, visited, temp):  # prints all vertices in DFS manner from a given source.
                    # Initially mark all verices as not visited


        # Create a stack for DFS
        stack = []

            # Push the current source node.
        stack.append(s)

        while (len(stack)):
            # Pop a vertex from stack and print it
            s = stack[-1]
            stack.pop()
            # Stack may contain same vertex twice. So
            # we need to print the popped item only
            # if it is not visited.
            if (not visited[s]):
                temp.append(s)
                #print(s, end=' ')
                visited[s] = True

            # Get all adjacent vertices of the popped vertex s
            # If a adjacent has not been visited, then push it
            # to the stack.
            for node in self.listaAdj[s]:
                    if (not visited[node[0]]):
                        stack.append(node[0])
        return temp
    def DFSlista(self, s, visited, temp):  # prints all vertices in DFS manner from a given source.
        # Initially mark all verices as not visited
        # Create a stack for DFS
        stack = []
        arestas= []
        # Push the current source node.
        stack.append(s)
        while (len(stack)):
            # Pop a vertex from stack and print it
            s = stack[-1]
            stack.pop()
            # Stack may contain same vertex twice. So
            # we need to print the popped item only
            # if it is not visited.
            if (not visited[s]):
                temp.append(s)
                #print(s, end=' ')
                visited[s] = True
            # Get all adjacent vertices of the popped vertex s
            # If a adjacent has not been visited, then push it
            # to the stack.
            for node in self.listaAdj[s]:
                
                if (not visited[node[0]]):
                    stack.append(node[0])
                    arestas.append(node[0])
        while 0 in temp:
            temp.remove(0)
        return temp,arestas
'''#g = Grafo(None)
g = Grafo.leArquivo("grafo_teste");
g.adicionaAresta(1, 2, 5)
g.adicionaAresta(1, 3, 7)
g.adicionaAresta(1, 4, 6)
g.adicionaAresta(2, 3, 9)
g.imprimeGrafo()
print('')
print(f'Grafo de Ordem: {g.ordemGrafo()}')
print(f'Grafo de tamanho: {g.tamanhoGrafo()}')
print(f'Vizinhos do vértice: {g.retornaVizinhos(1)}')
print(f'Grau do vértice: {g.grauVertice(1)}')
'''
'''
- Retornar a ordem do grafo - ok
- Retornar o tamanho do grafo - ok
- Retornar os vizinhos de um vértice fornecido - ok
- Determinar o grau de um vértice fornecido - ok
- Determinar a sequência de vértices visitados na busca em profundidade e informar
a(s) aresta(s) de retorno- falta as arestas
 - Determinar o número de componentes conexas do grafo e os vértices de cada
componente-ok
- Verificar se um vértice é articulação
- Verificar se uma aresta é ponte 
Para o teste da biblioteca faça um programa principal que leia o arquivo
texto e salve em um arquivo texto as diversas informações sobre o grafo lido.
O formato do grafo no arquivo será o seguinte: a primeira linha informa o número
de vértices do grafo, cada linha subsequente informa as arestas com seu respectivo peso
(ver o exemplo anterior).
4
1 2 5
1 3 7
1 4 6
2 3 9
'''
