from Grafo import Grafo

nome_arquivo = input("Digite o nome do arquivo: ")
g = Grafo.leArquivo(nome_arquivo)

g.imprimeGrafo()
g.exibeInformacoes()
