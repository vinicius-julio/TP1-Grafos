class Grafo:
    #Implementa Grafos nao direcionados ponderados

    def __init__(self, vertices):
        self.vertices = vertices
        self.listaAdj = [[] for i in range(self.vertices+1)] #conteudo das linhas em branco, vertices = numero de linhas

    def adicionaAresta(self, u, v, peso):
        self.listaAdj[u].append([v, peso]) #adiciona v e o peso na linha/vertice u
        self.listaAdj[v].append([u, peso]) #adiciona u e o peso na linha/vertice v

    def imprimeGrafo(self):
        for i in range(1,self.vertices+1):
            print(f'{i}:', end='  ')
            for j in self.listaAdj[i]:
                print(f'{j} -', end='  ')
            print('')
        print('')

    def exibeInformacoes(self):
        v_b=1
        print(f'Grafo de Ordem: {self.ordemGrafo()}')
        print(f'Grafo de tamanho: {self.tamanhoGrafo()}')
        v = int(input("\nDigite um Vértice: "))
        print(f'Vizinhos do vértice: {self.retornaVizinhos(v)}')
        print(f'Grau do vértice: {self.grauVertice(v)}')
        print(f'Lista da busca: {self.dfs(v_b)}')
                
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
    def dfs(self, vertice):
        visitados = set()
        teste=[]
        def dfs_iterativa(self, vertice_fonte):
            visitados.add(vertice_fonte)
            falta_visitar = [vertice_fonte]
            
            while falta_visitar:
                vertice = falta_visitar.pop()
                for vizinho in self.listaAdj[vertice]:
                    teste.append(vizinho[0])
                    if vizinho[0] not in visitados:
                        visitados.add(vizinho[0])
                        falta_visitar.append(vizinho[0])

        dfs_iterativa(self, vertice)
        return teste
    def DFSUtil(self, temp, v, visited):
 
        #Marcar Vertice atual como visitado
        visited[v] = True
 
        # armazenar o vestice na lista 
        temp.append(v)
 
        # Repita para todos os vértices adjacentes
        # para o vertice v
        for i in self.listaAdj[v]:
            print("PROVA: ",i)
            aux= i[0]
            print("TESTE: ",aux)
            if visited[aux] == False:
 
                # atualizar a lista
                temp = self.DFSUtil(temp, aux, visited)
        return temp    
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.vertices+1):
            visited.append(False)
        for v in range(self.vertices+1):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc
    def NumberOfconnectedComponents(self):
         
        # marcar todos vertices como n visitados
        visited = [False for i in range(self.vertices+1)]
         
        # armazenar o numero de componentes conectados
        count = 0
         
        for v in range(self.vertices+1):
            if (visited[v] == False):
                self.DFSUtil2(v, visited)
                count += 1
                 
        return count
    def DFSUtil2(self, v, visited):
 
        # marcar o no como visitado
        visited[v] = True
 
        # recorrer para todos vertices adjacentes ao vertice v
  
        for i in self.listaAdj[v]:
            if (not visited[i[0]]):
                self.DFSUtil2(i[0], visited)
 
    

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
