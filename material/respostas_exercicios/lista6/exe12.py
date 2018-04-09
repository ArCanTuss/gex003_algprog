N1 = int(input("Informe N1: "))
N2 = int(input("Informe N2: "))
multiplicacao = 0

for i in range(N2):
	multiplicacao += N1
	
print("{0} X {1} = {2}".format(N1, N2, multiplicacao))