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

#Leitura matriz A
A = []
print("----Matriz A----")
for i in range(N_linha):
	linha = []
	print("Linha", i+1)
	for j in range(N_coluna):
		n = int(input("Informe um número para a coluna {}: ".format(j+1)))
		linha.append(n)
	A.append(linha)

#Leitura matriz B
B = []
print("\n----Matriz B----")
for i in range(N_linha):
	linha = []
	print("Linha", i+1)
	for j in range(N_coluna):
		n = int(input("Informe um número para a coluna {}: ".format(j+1)))
		linha.append(n)
	B.append(linha)

#Chama a função para fazer o cálculo da matriz C
C = soma_matriz(A, B)

#Impressão da matriz C
print("\nMatriz C (A + B):")
for i in range(N_linha):
	for j in range(N_coluna):
		print("{:3}".format(C[i][j]), end=" ")
	print()
