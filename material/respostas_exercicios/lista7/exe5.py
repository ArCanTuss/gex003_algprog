for i in range(10): #dez linhas
	for j in range(10): #dez colunas
		if i == j or i == 0 or i == 9 or j == 0 or j == 9:
			print("*", end=" ")
		else:
			print(" ", end=" ")
	print()
