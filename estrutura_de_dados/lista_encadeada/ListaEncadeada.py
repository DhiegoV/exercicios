
from estrutura_de_dados.util.No import No


class ListaEncadeada:

    def __init__(self):
        self.inicio = None

    # MANIPULACAO
    def inserir(self, valor, indice):
        no_anterior = None
        no_corrente = self.inicio
        indice_corrente = 0
        novo_no = No(valor)

        while indice_corrente != indice and no_corrente.proximo != None:
            indice_corrente += 1
            no_anterior = no_corrente
            no_corrente = no_corrente.proximo
        if indice_corrente == indice:
            no_anterior.proximo = novo_no
            novo_no.proximo = no_corrente

    def inserir_inicio(self, valor):
        novo_no = No(valor)

        if self.inicio == None:
            self.inicio = novo_no
        else:
            novo_no.proximo = self.inicio
            self.inicio = novo_no

    def inserir_final(self, valor):
        ultimo = self.buscar_final()
        novo_no = No(valor)

        if ultimo == None:
            self.inicio = novo_no
        else:
            ultimo.proximo = novo_no
    
    def remover(self, indice):
        no_anterior = None
        no_corrente = self.inicio
        indice_corrente = 0

        if indice_corrente == indice:
            self.remover_inicio()
            return

        while indice_corrente != indice and no_corrente.proximo != None:
            indice_corrente += 1
            no_anterior = no_corrente
            no_corrente = no_corrente.proximo
        if indice_corrente == indice:
            no_anterior.proximo = no_corrente.proximo
            no_corrente.proximo = None

    def remover_inicio(self):
        temp = self.inicio

        if temp == None:
            return

        self.inicio = temp.proximo
        temp.proximo = None

    def remover_final(self):
        no_anterior = None
        no_corrente = self.inicio

        while no_corrente.proximo != None:
            no_anterior = no_corrente
            no_corrente = no_corrente.proximo

        no_anterior.proximo = None
        
    # BUSCA
    def buscar_final(self):
        if self.inicio == None:
            return

        temp = self.inicio
        while temp.proximo != None:
            temp = temp.proximo
        return temp

    def buscar_por_indice(self, indice):
        no_corrente = self.inicio
        indice_corrente = 0
        
        while indice_corrente != indice and no_corrente.proximo != None:
            indice_corrente += 1
            no_corrente = no_corrente.proximo
        if indice_corrente == indice:
            return no_corrente

    def buscar_por_valor(self, valor):
        no_corrente = self.inicio

        while no_corrente.dado != valor and no_corrente.proximo != None:
            no_corrente = no_corrente.proximo
        if no_corrente.dado == valor:
            return no_corrente

    # IMPRESSAO
    def imprimir_valores(self):
        temp = self.inicio

        while temp != None:
            print(temp.dado)
            temp = temp.proximo

    def imprimir_valores_ilustrados(self):
        temp = self.inicio

        print("lista\n"
              "\t\\", end="")
        while temp != None:
            print("->|", temp.dado, "|", sep="", end="")
            temp = temp.proximo
        print("¬")
