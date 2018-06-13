def ler_matriz(ordem):
	mat = []
	for i in range(ordem):
		linha = []
		for j in range(ordem):
			n = int(input("Informe matriz[{}][{}]: ".format(i, j)))
			linha.append(n)
		mat.append(linha)
	return mat

def imprime_matriz(matriz, ordem):
	for i in range(ordem):
		for j in range(ordem):
			print("{:3}".format(matriz[i][j]), end=" ")
		print()

def multiplica_matriz(matriz, num):
	for i in range(4):
		for j in range(4):
			matriz[i][j] *= num 

#Principal....
print("Leitura da matriz:")
matriz = ler_matriz(4)

num = int(input("Informe o número para mutiplicar: "))

multiplica_matriz(matriz, num)

print("\nImpressão da matriz:")
imprime_matriz(matriz, 4)
