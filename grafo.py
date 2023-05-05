import queue
from collections import deque

BRANCO = 1
CINZA = 2
PRETO = 3

class Grafo:
  def __init__(self, nvertices):
    self.vertices = nvertices
    self.matriz = [[0 for _ in range(nvertices)] for _ in range(nvertices)]
    self.lista = [[] for _ in range(nvertices)]
    self.vetorPai = [None for _ in range(nvertices)]
    self.vetorDistnc = [float("inf") for _ in range(nvertices)]
    self.vetorCor = [BRANCO for _ in range(self.vertices)]


  def BFS(self, vRaiz):
    vetorCor = [BRANCO for _ in range(self.vertices)] 
    vetorCor[vRaiz] = CINZA
    self.vetorDistnc[vRaiz] = 0
    fila = queue.Queue()
    fila.put(vRaiz)
    while fila.empty() == False:
        vRaiz = fila.get()
        for elem in self.lista[vRaiz]:
            if vetorCor[elem] == BRANCO:
                vetorCor[elem] = CINZA
                self.vetorDistnc[elem] = self.vetorDistnc[vRaiz] + 1
                self.vetorPai[elem] = vRaiz
                fila.put(elem)
        vetorCor[vRaiz] = PRETO

  def caminho_vertices(self, vRaiz, vFinal):
     self.BFS(vRaiz)
     contd = self.vetorDistnc[vFinal]
     if(contd == 0 or contd == float("inf")):
        print("Não ha caminho entre os vertices.")
     else:
        vPercorridos = self.vetorPai[vFinal]
        pilhaCaminho = deque()
        pilhaCaminho.append(vFinal)
        while(contd != 0):
            pilhaCaminho.append(vPercorridos)
            vPercorridos = self.vetor_pai[vPercorridos]
            contd -=1
        caminho = []
        for _ in range(self.vetorDistnc[vFinal] + 1):
           caminho.append(pilhaCaminho.pop())
        print(f"Caminho do vertice {vRaiz} ao vertice {vFinal}:", caminho)

  def DFS(self):
     for i in range(self.vertices):
        if(self.vetorCor[i] == BRANCO):
           self.dfs_visit(i)


  def dfs_visit(self, vVerificado):
    pilha = [vVerificado]
    self.vetorCor[vVerificado] = CINZA
    
    while pilha:
        v_atual = pilha[-1]
        vizinhoNverificado = False
        
        for vizinho in self.lista[v_atual]:
            if self.vetorCor[vizinho] == BRANCO:
                vizinhoNverificado = True
                self.vetorPai[vizinho] = v_atual
                self.vetorCor[vizinho] = CINZA
                pilha.append(vizinho)
                break
        
        if not vizinhoNverificado:
            pilha.pop()
            self.vetorCor[v_atual] = PRETO

def print_info(self):
    print("Matriz de Adjacencia:")
    for i in range(self.vertices):
        print(self.matriz[i])
    print()
    print("Lista de Adjacencia:")
    print(self.lista)
    print()
    print("Vetor distancia:")
    print(self.vetorDistnc)
    print()
    print("Vetor Pai:")
    print(self.vetorPai)
    print()
    print("Vetor cor:")
    print(self.vetorCor)
    print()

def ler_arquivo(nome_arquivo):
    f = open(nome_arquivo, 'r')
    num_linhas = int(f.readline())
    g = Grafo(num_linhas)
    
    i = 0
    for linhas in f:
        numeros = linhas.split('\t') #Isso é uma lista
        j = 0
        for k in range(g.vertices):
            valor_aresta = int(numeros[k])
            if valor_aresta > 0:
                g.matriz[i][j] = valor_aresta
                g.lista[i].append(j)
            
            j += 1
        i += 1   
    
    return g

grafo = ler_arquivo("pcv10.txt")
grafo.BFS(2)
grafo.print_info()
grafo.caminho_vertices(9, 6)
print("----------------------------------------------")
print("DFS iterativo.")
grafo2 = ler_arquivo("pcv4.txt")
grafo2.DFS()
grafo2.print_info()