def primo(n):
	for div in range(2, n):
		if n % div == 0:
			return False
	return True


#Código principal
A = int(input("Informe A: "))
B = int(input("Informe B: "))

print("Números primos do intervalo entre {} e {}:".format(A, B))
for i in range(A, B+1):
	if primo(i): #Chama a função que verificar se i é primo
		print(i)
	
