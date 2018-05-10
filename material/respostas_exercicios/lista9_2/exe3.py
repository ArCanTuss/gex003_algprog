ordem = 5

#Leitura da matriz
matriz = []
for i in range(ordem):
	linha = []
	print()
	print("Linha", i)
	for j in range(ordem):
		n = int(input("Informe um número para a coluna {}: ".format(j)))
		linha.append(n)
	matriz.append(linha)
	
SL = [0, 0, 0, 0, 0]
SC = [0, 0, 0, 0, 0]

#Calcula a soma das linhas e das colunas
for i in range(ordem):
	for j in range(ordem):
		SL[i] += matriz[i][j]
		SC[j] += matriz[i][j]
		
		
print("\nSoma das linhas:")
for i in range(ordem):
	print("Linha {}: {}".format(i, SL[i]))
	
print("\nSoma das colunas:")
for i in range(ordem):
	print("Coluna {}: {}".format(i, SC[i]))
