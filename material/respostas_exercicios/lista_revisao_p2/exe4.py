def ler_matriz():
	matriz = []
	for i in range(4):
		linha = []
		for j in range(3):
			linha.append(int(input("Informe um número para matriz[{}][{}]: ".format(i, j))))
		matriz.append(linha)
	return matriz

def imprime_matriz(mat):
	for i in range(4):
		for j in range(3):
			print("{:3}".format(mat[i][j]), end=" ")
		print()
		
#Código principal...
matriz = ler_matriz()

for i in range(4):
	for j in range(3):
		matriz[i][j] *= 2 #Múltiplica por 2

print("\nImpressão da matriz:")
imprime_matriz(matriz)
