from Grafo import Grafo
from converteJSON import converteJSON

opcao = 1
while (opcao!=0):
    print("Selecione uma opção:")
    print("1 - Ler grafo a partir de um arquivo")
    print("2 - Converter arquivo JSON para o formato de entrada")
    print("0 - Sair")
    opcao = int(input())
    if (opcao == 1): # Lê arquivo
        arqInput = input("Digite o nome do arquivo: ")
        g = Grafo.leArquivo(arqInput)
        nomeOut = input("Digite o nome do arquivo de saída: ")
        with open(nomeOut, "w") as arqOut:
            g.imprimeGrafo(arqOut)
            vertice = int(input("Selecione Vertice:" ))
            #g.exibeInformacoes(vertice)
            arqOut.write(f'Grafo de Ordem: {g.ordemGrafo()}\n')
            arqOut.write(f'Grafo de tamanho: {g.tamanhoGrafo()}\n')
            arqOut.write(f'Vizinhos do vértice {vertice}: {g.retornaVizinhos(vertice)}\n')
            arqOut.write(f'Grau do vértice {vertice}: {g.grauVertice(vertice)}\n')
            arqOut.write(f'Lista da busca: {g.dfs(vertice)}\n')
            arqOut.write(f'Número de componentes conexas: {g.NumberOfconnectedComponents()}\n')
            arqOut.write(f'Vértices de componentes conexas: {g.connectedComponents()}\n')
            print("Salvo como: " + nomeOut)

    if (opcao == 2): # Lê arquivo JSON
        arqJSON = input("Digite o nome do arquivo JSON: ")
        arqOut = input("Digite o nome do arquivo de saída: ")
        converteJSON(arqJSON, arqOut)
