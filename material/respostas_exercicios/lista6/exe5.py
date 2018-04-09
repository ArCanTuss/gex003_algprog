N = int(input("Número: "))
fib1 = 0
fib2 = 1

if N > 0:
	if N == 1:
		print(fib1, end=".")
	elif N == 2:
		print(fib1, fib2, sep=", ", end=".")
	else:
		for i in range(N):
			if N-1 == i:
				print(fib1, end=".")
			else:
				print(fib1, end=", ")
			
			aux = fib1 + fib2
			fib1 = fib2
			fib2 = aux

print() #print para quebrar linha ao fim do programa