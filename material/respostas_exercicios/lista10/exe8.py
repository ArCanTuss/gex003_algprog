def multiplicao(n1, n2):
	multi = 0
	for i in range(n2):
		multi += n1
	return multi

#Código principal
N1 = int(input("Informe N1: "))
N2 = int(input("Informe N2: "))

multi = multiplicao(N1, N2)
print("{} X {} = {}".format(N1, N2, multi))