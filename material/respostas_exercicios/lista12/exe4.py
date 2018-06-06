class Estadio: #Estrutura estádio
	nome = ""
	capacidadePublico = 0
	recordPublico = 0

def maior_capacidade(lista):
	maiorEstadio = Estadio()
	for est in lista: #Acessa direto a lista no for
		if est.capacidadePublico > maiorEstadio.capacidadePublico:
			maiorEstadio = est
	return maiorEstadio

def maior_publico(lista):
	maiorPublico = Estadio()
	for i in range(5): #Acessa a lista pelo índice gerado com range
		if lista[i].recordPublico > maiorPublico.recordPublico:
			maiorPublico = lista[i]
	
	return maiorPublico

estadios = []
for i in range(5):
	print()
	e = Estadio()
	e.nome = input("Informe o nome do estádio: ")
	e.capacidadePublico = int(input("Informe a capacidade: "))
	e.recordPublico = int(input("Informe o record de público: "))
	estadios.append(e)
	
maiorEstadio = maior_capacidade(estadios)	
maiorRecord = maior_publico(estadios)

print()
print("O maior estádio é o {}, com capacidade de {} pessoas.".format(maiorEstadio.nome, maiorEstadio.capacidadePublico))
print("O maior (record) publico foi no estádio {}, com total de {} pessoas.".format(maiorRecord.nome, maiorRecord.recordPublico))
	
