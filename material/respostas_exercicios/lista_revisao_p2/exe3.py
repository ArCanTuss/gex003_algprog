def imprime_lista(lista):
	for i in lista:
		print(i, end=" ")
	print()

def inverte_lista(lista):
	retorno = []
	for i in range(len(lista)-1, -1, -1):
		retorno.append(lista[i])
	return retorno

def numero_primo(num):
	if num < 2:
		return False
	
	for div in range(2, num):
		if num % div == 0:
			return False
	return True

def primos_lista(lista):
	retorno = []
	for i in lista:
		if numero_primo(i):
			retorno.append(i)
	return retorno

inteiros = []
for i in range(15):
	num = int(input("Informe o número {}: ".format(i+1)))
	inteiros.append(num)

inteiros_inv = inverte_lista(inteiros)
print("\nA - Vetor em ordem inversa:")
imprime_lista(inteiros_inv)

primos = primos_lista(inteiros)
primos = inverte_lista(primos)
print("\nB - Primos em ordem inversa:")
imprime_lista(primos)
