qtdGraoCasa = 1 #Na primeira casa há 1 grão
totalGrao   = 1 #Total de grãos

#Laço para calcular a quantidade das 63 casas restantes
for i in range(2, 65):
	qtdGraoCasa = qtdGraoCasa * 2
	print(i, qtdGraoCasa)
	totalGrao = totalGrao + qtdGraoCasa
	

print("Quantidade de grãos recebidos:", totalGrao)
