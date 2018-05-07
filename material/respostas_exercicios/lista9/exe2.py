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
	
somaLinha4  = 0
somaColuna2 = 0
somaDiagonalSec = 0
somaTodos = 0
for i in range(N):
	for j in range(N):
		if i == 3:
			somaLinha4 += matriz[i][j]
		if j == 1:
			somaColuna2 += matriz[i][j]
		if i+j == N-1:
			somaDiagonalSec += matriz[i][j]
		
		somaTodos += matriz[i][j]

print("Soma de todos os elementos da linha 4:", somaLinha4)
print("Soma de todos os elementos da coluna 2:", somaColuna2)
print("Soma de todos os elementos da diagonal:", somaDiagonalSec)
print("Soma de todos os elementos da matriz:", somaTodos)
