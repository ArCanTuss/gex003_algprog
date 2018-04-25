#Leitura dos números
numeros = []
for i in range(5):
	n = int(input("Informe o N{}: ".format(i+1)))
	numeros.append(n)
	
#Troca a ordem, armazenando o novo vetor em aux
aux = []
for n in numeros:
	aux.insert(0, n)
	
numeros = aux
print(numeros)