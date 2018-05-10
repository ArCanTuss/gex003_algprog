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

print()
N = int(input("Informe um número N: "))

print()

encontrouN = False
for i in range(ordem):
	for j in range(ordem):
		if matriz[i][j] == N:
			print("{} encontrado na posição [{}][{}]".format(N, i, j))
			encontrouN = True
			
if not encontrouN:
	print("{} não existe na matriz!".format(N))
		
