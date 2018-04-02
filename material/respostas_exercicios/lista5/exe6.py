N = int(input("Número: "))
aux = N
fatorial = 1

while N > 0:
	fatorial = fatorial * N
	N += -1
	
print("O fatorial de {0} é {1}".format(aux, fatorial))