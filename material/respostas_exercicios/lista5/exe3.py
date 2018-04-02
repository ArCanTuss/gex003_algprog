n1 = int(input("Informe um número N1: "))
n2 = int(input("Informe um número N2: "))

quoc = 0
resto = 0
while n1 > 0 and resto == 0:
	n1 = n1 - n2
	quoc += 1
	
	if n2 > n1:
		resto = n1

print("Quociente: {0} | Resto: {1}".format(quoc, resto))