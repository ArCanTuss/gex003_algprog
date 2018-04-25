#Leitura dos números
numeros = []
for i in range(10):
	n = int(input("Informe o N{}: ".format(i+1)))
	numeros.append(n)
	
#Leitura do alvo
alvo = int(input("Informe o alvo: "))

print("Vezes que o alvo aparece no vetor:", numeros.count(alvo))