opcao = int(input("Informe a opção: "))
if opcao == 2 or opcao == 3 or opcao == 4:
	num1 = int(input("Informe o primeiro número: "))
	num2 = int(input("Informe o segundo número: "))
	num3 = int(input("Informe o terceiro número: "))
	
	if opcao == 2:
		print(num1)
	elif opcao == 3:
		print(num2)
	else:
		print(num3)
else:
	print("Opção inválida")