def tabuada(n):
	print("Tabuada do {}:".format(n))
	for i in range(1, 11):
		print("{} x {} = {}".format(n, i, n*i))
		
		
#Código principal
for i in range(2, 13):
	print() #Linha em branco
	tabuada(i) #Chamada da função para imprimir a tabuada
