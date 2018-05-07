mat = [ [1,  8,  3,  22, 30],
	    [21, 12, 9,  16, 31],
	    [14, 7,  5,  8,  19],
	    [10, 25, 24, 4,  9],
	    [5,  18, 16, 26, 20] ]

for i in range(5):
	for j in range(5):
		if mat[i][j] % 2 == 1: #Número ímpar
			mat[i][j] = 0

#Imprime a matriz
for i in range(5):
	for j in range(5):
		print("{:3}".format(mat[i][j]), end=" ")
	print()
