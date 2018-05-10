ordem = 4

#Leitura da matriz
matriz = []
for i in range(ordem):
	linha = []
	print()
	print("Linha", i+1)
	for j in range(ordem):
		n = int(input("Informe um número para a coluna {}: ".format(j+1)))
		linha.append(n)
	matriz.append(linha)

somaA = 0
somaB = 0
somaC = 0
somaD = 0
for i in range(ordem):
	for j in range(ordem):
		if (i == 0 or i == 1) and (j == 0 or j == 1):
			somaA += matriz[i][j]
			
		if (i == 2 or i == 3) and (j == 2 or j == 3):
			somaB += matriz[i][j]
			
		if i >= j:
			somaC += matriz[i][j]
			
		if i < j:
			somaD += matriz[i][j]

print()
print("Soma a):", somaA)
print("Soma b):", somaB)
print("Soma c):", somaC)
print("Soma d):", somaD)
