def imprime_matriz(matriz, ordem):
	for i in range(ordem):
		for j in range(ordem):
			print("{:3}".format(matriz[i][j]), end=" ")
		print()


#Código principal
N = int(input("Informe a ordem da matriz: ")) #Tamanho da matriz
matriz = []
for i in range(N):
	linha = []
	print()
	print("Linha", i+1)
	for j in range(N):
		n = int(input("Informe um número para a coluna {}: ".format(j+1)))
		linha.append(n)
	matriz.append(linha)
	
print("\nImpressão da matriz:")
imprime_matriz(matriz, N) #Chamada da função para imprimir a matriz
