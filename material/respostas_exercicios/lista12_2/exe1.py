def conta_caractere(palavra, carac):
	conta = 0
	for p in palavra:
		if p == carac:
			conta += 1
	return conta

pal   = input("Informe a palavra: ")
carac = input("Informe o caractere a ser encontado na palavra: ")

conta = conta_caractere(pal, carac)
print("Existem {} caracteres [{}] na palavra [{}].".format(conta, carac, pal))

