#Leitura dos números
numeros = []
for i in range(20):
	n = int(input("Informe o N{}: ".format(i+1)))
	numeros.append(n)
	
#Remove os número não pares
for n in numeros:
	if n % 2 != 0:
		numeros.remove(n)
	
print()
print(numeros)