cont = 1
nomeAlturaMax = input("Informe o nome de uma pessoa {0}: ".format(cont))
alturaMax = float(input("Informe a altura da pessoa {0}: ".format(cont)))

nomePesoMax = nomeAlturaMax
pesoMax = float(input("Informe o peso da pessoa {0}: ".format(cont)))

cont = cont + 1
while cont <= 4:
	print()
	
	nome = input("Informe o nome de uma pessoa {0}: ".format(cont))
	
	altura = float(input("Informe a altura da pessoa {0}: ".format(cont)))
	if altura > alturaMax:
		alturaMax = altura
		nomeAlturaMax = nome
	
	peso = float(input("Informe o peso da pessoa {0}: ".format(cont)))
	if peso > pesoMax:
		pesoMax = peso
		nomePesoMax = nome
	
	cont = cont + 1
	
print()
print("Pessoa mais alta: {0} - Altura: {1:.2f}".format(nomeAlturaMax, alturaMax))
print("Pessoa mais pesada: {0} - Peso: {1:.2f}".format(nomePesoMax, pesoMax))