import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt

'''soluçao da questao 1'''
### funçao da lista passada que recebe um poinomio em forma de string e o retorna em forma de dicionario
### Já tentei consertar o erro. Agora parece que esta dando certo
def poly(polinomio: str):
    dicionario = {}
    polinomio += '-'  # Adicionar um sinal no final para capturar o último termo
    polinomio = polinomio.replace('^', '')  # Remover o símbolo de potência
    polinomio = polinomio.replace(' ', '')
    numero_de_iteracoes = 0
    pointer = 0
    if polinomio[0] != '-' and polinomio[0] != '+':
        polinomio = '+' + polinomio 
    # Contar o número de termos
    for i in polinomio:
        if i == '+' or i == '-':
            numero_de_iteracoes += 1
    numero_de_iteracoes -= 1
    for _ in range(numero_de_iteracoes):
        string = ''
        if polinomio[pointer] == '+':
            string += '+'
            pointer += 1
        elif polinomio[pointer] == '-':
            string += '-'
            pointer += 1
        while polinomio[pointer] != '+' and polinomio[pointer] != '-':
            string += polinomio[pointer]
            pointer += 1
        # Separar coeficiente e expoente
        if 'x' in string:
            coeficiente, _, expoente = string.partition('x')
            if coeficiente == '+' or coeficiente == '':
                coeficiente = 1
            elif coeficiente == '-':
                coeficiente = -1
            else:
                coeficiente = float(coeficiente)
            if expoente == '':
                expoente = 1
            else:
                expoente = float(expoente)
        else:
            coeficiente = float(string)
            expoente = 0
        dicionario[expoente] = coeficiente
    return dicionario
def avaliation_pol(poly: dict, x): 
    #essa funçao avalia o polinomio no ponto x
    valor = 0
    for exp in poly:
        valor += (x**exp)*poly[exp]
    return valor
def pontos(interval, polinomio: str):
    list_points = []
    poly_dict = poly(polinomio)
    for i in np.linspace(interval[0], interval[1], 1000):
        list_points.append([i,avaliation_pol(poly_dict, i)])
    return list_points

def save(polinomio: str, interval: list, FileName):
    with open(FileName, 'w') as file:
        Head = ['x', 'y']
        fl = csv.DictWriter(file, fieldnames=Head)
        fl.writeheader()
        for i in pontos(interval, polinomio):
            fl.writerow({'x':i[0], 'y':i[1]})
    
def x_y(FileName):
    with open(FileName, 'r') as file:
        fl = pd.read_csv(file)
        lista_x = []
        lista_y = []
        for i in fl['x']:
            lista_x.append(i)
        for i in fl['y']:
            lista_y.append(i)
    return lista_x, lista_y

def plot(FileName):
    XX, YY = x_y(FileName)
    fig, ax = plt.subplots()
    ax.plot(XX, YY)
    plt.show()

#polinomio = 'x^8-3x^4+2x^3-2x^2-x+2'
#save(polinomio, [-3/2, 3/2], 'polinomioFile.csv')
#x_y('polinomioFile.csv')
#plot('polinomioFile.csv')
#print(pd.read_csv('polinomioFile.csv'))
'''fim da soluçao da questao 1'''

'''soluçao da questao 2'''

def merge_intervals(intervals):
    inter = sorted(intervals)
    lista_intervals = []
    if len(inter) == 1:
        return inter
    for i in range(len(intervals) - 1):
        if inter[i][1] >= inter[i+1][0]:
            lista_intervals.append([inter[i][0], max([inter[i+1][1], inter[i][1]])])
            lista_intervals += inter[i+2:]
            return merge_intervals(lista_intervals)
        else:
            lista_intervals.append(inter[i])
    lista_intervals.append(inter[len(inter) - 1])
    return lista_intervals
    
'''fim da soluçao da questao 2'''


'''soluçao da questao 3'''
######## Considerarei aqui que, sob hipotese alguma, tenha numeros repetidos na lista
##### e tanbem que realmente tenha algum item faltando #######
def idx_missing_int(sequencia):
    # função auxiliar do missing_int
    a = sequencia[:len(sequencia)//2]
    b = sequencia[len(sequencia)//2:]
    pointer = 0
    if b[0] - a[len(a) - 1] > 1:
        return len(a) - 1
    if a[len(a) - 1] - a[0] > len(a) - 1:
        pointer += 0 
        return pointer + missing_int(a)
    elif b[len(b) - 1] - b[0] > len(b) - 1:
        pointer += len(b) - 1
        return pointer + (missing_int(b))
    return 0

def missing_int(sequencia):
    return sequencia[idx_missing_int(sequencia)] + 1
'''fim da soluçao da questao 3'''
 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class List:
    def __init__(self):
        self.elem = None
        self.next = None

    def append(self, other):
        #Essa função adiciona o elemento other a lista
        pointer = self.elem
        if self.elem is None:
            self.elem = Node(other)

        else:
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(other)
         
    def __len__(self):
        #Essa função retorna o tamanho da lista
        pointer = self.elem
        if self.elem:
            lenght = 1
            while pointer.next:
                lenght += 1
                pointer = pointer.next
            return lenght
        else:
            return 0
        
    def index(self, i):
        #essa função vai buscar um elemento na lista dada a sua posição
        pointer = self.elem
        for i in range(i):
            pointer = pointer.next
        return pointer.data

    def invert_ordem(self):
        #Vamos criar uma nova lista com a posição dos elementos invertidas
        list_inverse = List()
        for i in range(len(self)):
            list_inverse.append(self.index(len(self) - 1 - i))
        return list_inverse
        #representation = ['{}'.format(list_inverse.index(k)) for k in range(len(list_inverse))]
        #return representation
    
    def __str__(self):
        return str([self.index(k) for k in range(len(self))])
lista = List()
lista.append(3)
lista.append(4)
lista.append(5)
lista.append(5)
lista.append(2)
lista.append(6)
lista.append(556757)
lista.append(6)
lista.append(2)
lista.append(5)
lista.append(5)
lista.append(4)
lista.append(3)

def is_palindrome(lista_encadeada: List):
    inverse = lista_encadeada.invert_ordem()
    for i in range(len(lista_encadeada)):
        if lista_encadeada.index(i) != inverse.index(i):
            return False
    return True
print(is_palindrome(lista))





