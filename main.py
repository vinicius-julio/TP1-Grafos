from Grafo import Grafo
from converteJSON import converteJSON

nome_arquivo = input("Digite o nome do arquivo: ")
g = Grafo.leArquivo(nome_arquivo)

g.imprimeGrafo()
g.exibeInformacoes()
vertice = int(input())
g.dfs(vertice)
g.connectedComponents()
g.NumberOfconnectedComponents()
arqJSON = input("Digite o nome do arquivo JSON: ")
arqOut = input("Digite o nome do arquivo de saída: ")
converteJSON(arqJSON, arqOut)
