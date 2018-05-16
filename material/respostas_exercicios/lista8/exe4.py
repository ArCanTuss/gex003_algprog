#Leitura dos números
numeros = []
for i in range(20):
	n = int(input("Informe o N{}: ".format(i+1)))
	numeros.append(n)
	
#Remove os número não pares
i = 0
while i < len(numeros):
	if numeros[i] % 2 != 0:
		numeros.pop(i)
	else:
		i += 1
		
	
print()
print(numeros)
