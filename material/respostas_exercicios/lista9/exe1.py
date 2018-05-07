matriz = []
for i in range(4):
	linha = []
	print()
	print("Linha", i+1)
	for j in range(4):
		n = int(input("Informe um número para a coluna {}: ".format(j+1)))
		linha.append(n)
	matriz.append(linha)

soma = 0
for i in range(4):
	for j in range(4):
		if i > j:
			soma += matriz[i][j]

print(soma)
