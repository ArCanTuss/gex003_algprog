N = int(input("Número: "))
acuDivisores = 0
cont = 1

while cont < N:
	if N % cont == 0:
		acuDivisores = acuDivisores + cont
	cont = cont + 1
	
if acuDivisores == N:
	print("O número {0} é perfeito".format(N))
else:
	print("O número {0} não é perfeito".format(N))