#Leitura dos números
numeros = []
for i in range(20):
	n = int(input("Informe o N{}: ".format(i+1)))
	numeros.append(n)
	
#Troca as posições dos números
ultimo = 19
for i in range(10):
	aux = numeros[i]
	numeros[i] = numeros[ultimo]
	numeros[ultimo] = aux
	ultimo -= 1
	
print()
print(numeros)