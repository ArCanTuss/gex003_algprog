op = 1
while op != 0:
	print()
	print("---Menu principal---")
	print("1- Boas vindas a CC")
	print("2- Primeiro programa")
	print("3- Condições")
	print("4- Repetições")
	print("0- Sair do programa")
	
	print()
	op = int(input("Informe a opção:"))
	
	if op == 1:
		print("Seja bem vindo ao curso de Ciência da Computação da UFFS")
	elif op == 2:
		print("Alô Mundo em Python")
	elif op == 3:
		print("IF, ELIF e ELSE")
	elif op == 4:
		print("WHILE")
	elif op == 0:
		exit()
	else:
		print("Opção inválida!")
