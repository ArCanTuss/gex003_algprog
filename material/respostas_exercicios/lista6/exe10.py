qtdGrao = 2 #Na primeira casa há 1 grão, na segunda casa há 2 grãos

#Laço para calcular a quantidade das 62 casas restantes
for i in range(62):
	qtdGrao = qtdGrao * 2
	print(i, qtdGrao)
	
print("Quantidade de grãos recebidos:", qtdGrao)