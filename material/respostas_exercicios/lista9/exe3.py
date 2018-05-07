N_linha = 5 #Tamanho das linhas da matriz
N_coluna = 4 #Tamanho das colunas da matriz

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

#Cálculo da matriz C (A + B)
C = []
for i in range(N_linha):
	linha = []
	for j in range(N_coluna):
		linha.append(A[i][j] + B[i][j])
	C.append(linha)

#Impressão da matriz C
print("\nMatriz C (A + B):")
for i in range(N_linha):
	for j in range(N_coluna):
		print("{:3}".format(C[i][j]), end=" ")
	print()
