N = 5 #Tamanho da matriz
matriz = []
for i in range(N):
	linha = []
	print()
	print("Linha", i+1)
	for j in range(N):
		n = int(input("Informe um número para a coluna {}: ".format(j+1)))
		linha.append(n)
	matriz.append(linha)

#Percorre a matriz para identificar os números pares
print("\nNúmeros pares da matriz lida:")
for i in range(N):
	for j in range(N):
		if matriz[i][j] % 2 == 0:
			print(matriz[i][j], end=" ")

print()
