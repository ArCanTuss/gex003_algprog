ordem = 5

#Leitura da matriz A
print("Leitura da matriz A:")
matrizA = []
for i in range(ordem):
	linha = []
	print()
	print("Linha", i)
	for j in range(ordem):
		n = int(input("Informe um número para a coluna {}: ".format(j)))
		linha.append(n)
	matrizA.append(linha)
	
#Leitura da matriz B
print("\nLeitura da matriz B:")
matrizB = []
for i in range(ordem):
	linha = []
	print()
	print("Linha", i)
	for j in range(ordem):
		n = int(input("Informe um número para a coluna {}: ".format(j)))
		linha.append(n)
	matrizB.append(linha)


#Multiplica as matrizes
matrizC = []
for i in range(ordem):
	linha = []
	for j in range(ordem):
		val = 0
		for k in range(ordem):
			val += matrizA[i][k] * matrizB[k][j]
		linha.append(val)
	matrizC.append(linha)
    
#Imprime a matriz
print("\nMatrizes multiplicadas:")
for i in range(ordem):
	for j in range(ordem):
		print("{:5}".format(matrizC[i][j]), end=" ")
	print()
		
