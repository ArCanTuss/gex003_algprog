def divisao_inteira(n1, n2):
	if n2 == 0:
		print("Divisão por 0 é inválida!")
		return 0
	
	conta = 0
	while n1 >= n2:
		conta += 1
		n1 -= n2
	return conta

#Código principal
N1 = int(input("Informe N1: "))
N2 = int(input("Informe N2: "))

div = divisao_inteira(N1, N2)
print("Divisão inteira de {} por {} = {}".format(N1, N2, div))