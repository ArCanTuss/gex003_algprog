def caracteres_repetidos(palavra):
	retorno = ""
	for p in palavra:
		if palavra.count(p) > 1 and retorno.count(p) == 0:
			retorno += p
	return retorno

pal = input("Informe a palavra: ")

print("Caracteres repetidos da palavra [{}]: {}".format(pal, caracteres_repetidos(pal)))

