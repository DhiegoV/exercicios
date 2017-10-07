from ListaEncadeada import ListaEncadeada

lista = ListaEncadeada()

valores = [1, 2, 3, 4, 5]
for valor in valores:
    lista.inserir_final(valor)

lista.imprimir_valores_ilustrados()

print("inserindo no inicio...")
lista.inserir_inicio("no inicio")

print("inserindo terceiro...")
lista.inserir("terceiro", 2)

print("inserindo no final...")
lista.inserir_final("no final")

lista.imprimir_valores_ilustrados()

print("removendo terceiro...")
lista.remover(2)

print("removendo primeiro...")
lista.remover(0)

print("removendo ultimo...")
lista.remover_final()

lista.imprimir_valores_ilustrados()

