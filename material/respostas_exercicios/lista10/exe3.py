N_linha = 5  #VARIÁVEL GLOBAL - Tamanho das linhas da matriz
N_coluna = 4 #VARIÁVEL GLOBAL - Tamanho das colunas da matriz

def soma_matriz(matA, matB):
	#Cálculo da matriz matC (matA + matB)
	matC = []
	for i in range(N_linha):
		linha = []
		for j in range(N_coluna):
			linha.append(matA[i][j] + matB[i][j])
		matC.append(linha)
	return matC

def le_matriz():
	matriz = []
	for i in range(N_linha):
		linha = []
		print("Linha", i+1)
		for j in range(N_coluna):
			n = int(input("Informe um número para a coluna {}: ".format(j+1)))
			linha.append(n)
		matriz.append(linha)
	
	return matriz

def imprime_matriz(matriz):
	for i in range(N_linha):
		for j in range(N_coluna):
			print("{:3}".format(matriz[i][j]), end=" ")
		print()

#Leitura matriz A
print("----Matriz A----")
A = le_matriz()

#Leitura matriz B
print("\n----Matriz B----")
B = le_matriz()

#Chama a função para fazer o cálculo da matriz C
C = soma_matriz(A, B)

#Impressão da matriz C
print("\nMatriz C (A + B):")
imprime_matriz(C)
