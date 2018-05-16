def primo(n):
	for div in range(2, n):
		if n % div == 0:
			return False
	return True

def conta_primos(A, B):
	conta = 0
	for i in range(A, B+1):
		if primo(i): #Chama a função que verificar se i é primo
			conta += 1
	
	return conta

#Código principal
N1 = int(input("Informe N1: "))
N2 = int(input("Informe N2: "))

qtd_primos = conta_primos(N1, N2) #Chama a função que irá fazer a contagem de números primos entre N1 e N2
print("Quantidade de primos entre {} e {} = {}".format(N1, N2, qtd_primos))