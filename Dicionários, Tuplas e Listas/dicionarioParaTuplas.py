
def fazerTuplaDeChaves(dicionario):
	chaves = []
	for chave in dicionario.keys():
		chaves.append(chave)
	return tuple(chaves)

def fazerTuplaDeValores(dicionario):
	valores = []
	for valor in dicionario.values():
		valores.append(valor)
	return tuple(valores)

dicio = {}

# Entrada de dados
for i in range(3):
	print("\n",
		  "Pessoa ",i+1,"/",3, sep="")
	nome = input("Nome: ")
	matricula = input("Matricula de "+nome+": ")

	dicio[matricula] = nome

tuplaChaves = fazerTuplaDeChaves(dicio)
tuplaValores = fazerTuplaDeValores(dicio)

print("",
	  "Dicionário resultante:",
	  dicio,
	  "",
	  "Tupla de chaves:",
	  tuplaChaves,
	  "Tupla de valores:",
	  tuplaValores,
	  sep="\n")