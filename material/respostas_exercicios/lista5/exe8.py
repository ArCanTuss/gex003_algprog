N = int(input("Número: "))
cont = 1
fib1 = 0
fib2 = 1

if N > 0:
	if N == 1:
		print(fib1, end=".")
	elif N == 2:
		print(fib1, fib2, sep=", ", end=".")
	else:
		while cont <= N:
			if N == cont:
				print(fib1, end=".")
			else:
				print(fib1, end=", ")
			
			aux = fib1 + fib2
			fib1 = fib2
			fib2 = aux
			cont = cont + 1

print() #print para quebrar linha ao fim do programa