mat = [ [1,  8,  3,  22, 30],
	    [21, 12, 9,  16, 31],
	    [14, 7,  5,  8,  19],
	    [10, 25, 24, 4,  9],
	    [5,  18, 16, 26, 20] ]

linha = 0
while linha < len(mat):
	if mat[linha][0] % 2 == 0: #Número par
		mat.pop(linha) #Exclui
	else:
		linha += 1 #Testa a próxima linha
			
#Imprime a matriz
for i in range(len(mat)):
	for j in range(5):
		print("{:3}".format(mat[i][j]), end=" ")
	print()
