qtd = int(input("Números da sequência: "))

if qtd >= 3:
	ricci1 = int(input("Informe o primeiro número: "))
	ricci2 = int(input("Informe o segundo número: "))
	
	if ricci2 > ricci1:
		for i in range(qtd):
			print(ricci1, end=" ")
			aux = ricci1 + ricci2
			ricci1 = ricci2
			ricci2 = aux
	else:
		print("O primeiro número deve ser maior que o segundo!")
else:
	print("Número de elementos da sequência deve ser maior ou igual a 3!")

print() #print para quebrar linha ao fim do programa
