mat = [ [1,  8,  3,  22, 30],
	    [21, 12, 9,  16, 31],
	    [14, 7,  5,  8,  19],
	    [10, 25, 24, 4,  9],
	    [5,  18, 16, 26, 20] ]

coluna = 0
while coluna < len(mat[0]): #Testa o número de colunas da primeira linha
	if mat[0][coluna] % 2 == 0: #Número par
		for i in range(5):
			mat[i].pop(coluna) #Exclui a coluna da linha I
	else:
		coluna += 1 #Testa a próxima coluna
			
#Imprime a matriz
for i in range(5):
	for j in range(len(mat[0])):
		print("{:3}".format(mat[i][j]), end=" ")
	print()
