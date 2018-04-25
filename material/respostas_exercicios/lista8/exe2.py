#Leitura das palavras
palavras = []
for i in range(10):
	palavra = input("Informe a palavra {}: ".format(i+1))
	palavras.append(palavra)
	
#Encontra a maior palavra
maior = 0
maiorPalavra = ""
for p in palavras:
	if len(p) > maior:
		maior = len(p)
		maiorPalavra = p
		
print("\nMaior palavra:", maiorPalavra)