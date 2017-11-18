
from estrutura_de_dados.util.No import No


class Pilha:

    def __init__(self):
        self.topo = None

    def push(self, dado):
        novo_no = No(dado)

        if not self.estah_vazia():
            novo_no.proximo = self.topo
            self.topo = novo_no
        else:
            self.topo = novo_no

    def pop(self):
        if not self.estah_vazia():
            antigo_no = self.topo
            self.topo = antigo_no.proximo
            antigo_no.proximo = None
            return antigo_no.dado

    def estah_vazia(self):
        return self.topo == None

    def __str__(self):
        temp = Pilha()
        saida = ""

        while not self.estah_vazia():
            dado = self.pop()
            saida += str(dado)+"\n"
            temp.push(dado)

        while not temp.estah_vazia():
            dado = temp.pop()
            self.push(dado)

        return saida
