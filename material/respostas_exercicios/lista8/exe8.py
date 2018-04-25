#Leitura dos números da lista 1
lista1 = []
print("----Lista 1----")
for i in range(9):
	n = int(input("Informe o N{}: ".format(i+1)))
	lista1.append(n)
	
#Leitura dos números da lista 2
lista2 = []
print("----Lista 2----")
for i in range(9):
	n = int(input("Informe o N{}: ".format(i+1)))
	lista2.append(n)
	
#Leitura dos números da lista 3
lista3 = []
print("----Lista 3----")
for i in range(9):
	n = int(input("Informe o N{}: ".format(i+1)))
	lista3.append(n)
	
#Monta a lista de saída
saida = lista1[0:3] + lista2[3:6] + lista3[6:9]
print()
print(saida)