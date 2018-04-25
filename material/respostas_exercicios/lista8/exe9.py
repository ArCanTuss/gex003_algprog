#Leitura dos números
numeros = []
for i in range(15):
	n = int(input("Informe o N{}: ".format(i+1)))
	numeros.append(n)
	
	
#Acumula os resultados
for i in range(14):
	numeros[i+1] += numeros[i]
	
print(numeros)