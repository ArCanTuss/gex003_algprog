cont = 0

while cont < 10:
	num = int(input("Informe um número {0}: ".format(cont+1)))
	print("Antecessor:", num-1,"| Sucessor:", num+1)
	print()
	cont = cont + 1
