N = int(input("Informe um número: "))

if N <= 10:
	print("F1")
else:
	if N > 10 and N <= 100:
		print("F2")
	else: #caso seja maior que 100
		print("F3")
