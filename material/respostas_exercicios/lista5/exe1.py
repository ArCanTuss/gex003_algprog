somaPar   = 0
somaImpar = 0

num = int(input("Informe um número: "))
while num != 0:
	if num % 2 == 0:
		somaPar = somaPar + num
	else:
		somaImpar = somaImpar + num
	num = int(input("Informe um número: "))
	
print()
print("Soma dos pares:", somaPar)
print("Soma dos impares:", somaImpar)
