n1 = int(input("Informe um número N1: "))
n2 = int(input("Informe um número N2: "))

'''SOLUÇÃO 1
quoc = 0
resto = 0
while n1 > 0 and resto == 0:
	if n2 > n1:
		resto = n1
	else:
		n1 = n1 - n2
		quoc += 1
	

print("Quociente: {0} | Resto: {1}".format(quoc, resto))
'''

#SOLUÇÃO 2
quoc = 0
while n1 >= n2:
	n1 = n1 - n2
	quoc += 1
	

print("Quociente: {0} | Resto: {1}".format(quoc, n1))
