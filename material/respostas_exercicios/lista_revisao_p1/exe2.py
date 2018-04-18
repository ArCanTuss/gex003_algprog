qtdPrimos = 0

while True:
	N = int(input("Informe um número: "))
	if N <= 1:
		break
	
	primo = True
	for div in range(2, N):
		if N % div == 0:
			primo = False
			break
	
	if primo:
		qtdPrimos += 1
	
print("Quantidade de números primos:", qtdPrimos)
