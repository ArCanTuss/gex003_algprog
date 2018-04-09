N = int(input("Número: "))
fatorial = 1

for i in range(N, 0, -1):
	fatorial = fatorial * i
	
print("O fatorial de {0} é {1}".format(N, fatorial))