i = 1
nomeAlturaMax = input("Informe o nome de uma pessoa {0}: ".format(i))
alturaMax = float(input("Informe a altura da pessoa {0}: ".format(i)))

nomePesoMax = nomeAlturaMax
pesoMax = float(input("Informe o peso da pessoa {0}: ".format(i)))

for i in range(2, 5):
	print()
	
	nome = input("Informe o nome de uma pessoa {0}: ".format(i))
	
	altura = float(input("Informe a altura da pessoa {0}: ".format(i)))
	if altura > alturaMax:
		alturaMax = altura
		nomeAlturaMax = nome
	
	peso = float(input("Informe o peso da pessoa {0}: ".format(i)))
	if peso > pesoMax:
		pesoMax = peso
		nomePesoMax = nome
	
print()
print("Pessoa mais alta: {0} - Altura: {1:.2f}".format(nomeAlturaMax, alturaMax))
print("Pessoa mais pesada: {0} - Peso: {1:.2f}".format(nomePesoMax, pesoMax))