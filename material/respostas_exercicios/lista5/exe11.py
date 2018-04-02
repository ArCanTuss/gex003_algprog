N = int(input("Número: "))
dividiu = False
aux = N-1

while (not dividiu) and (aux > 1):
	if N % aux == 0:
		dividiu = True
	aux = aux - 1
	
if dividiu:
	print("O número {0} não é primo".format(N))
else:
	print("O número {0} é primo".format(N))