def retornaMediaArquivo(nomeArquivo):
	arquivo = open(nomeArquivo, "r")
	
	soma = 0
	conta = 0
	
	linhas = arquivo.read().splitlines() #Leitura do arquivo
	for lin in linhas:
		soma = soma + float(lin) #Converte para foat
		conta += 1
	
	arquivo.close()
	
	return soma/conta


#Código principal
media = retornaMediaArquivo("exe1_notas.txt")
print("A média das notas é {:.2f}.".format(media))
