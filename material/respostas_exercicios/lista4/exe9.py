pares = 0    #variável para acumular a soma dos números pares
impares = 0  #variável para acumular a soma dos números ímpares

num1 = int(input("Informe o número 1: "))
num2 = int(input("Informe o número 2: "))
num3 = int(input("Informe o número 3: "))
num4 = int(input("Informe o número 4: "))

if num1 % 2 == 0:
	pares = pares + num1   
else:
	impares = impares + num1

if num2 % 2 == 0:
	pares = pares + num2
else:
	impares = impares + num2
	
if num3 % 2 == 0:
	pares = pares + num3
else:
	impares = impares + num3
	
if num4 % 2 == 0:
	pares = pares + num4
else:
	impares = impares + num4
	
print("Soma dos pares:", pares, ", Soma dos impares:", impares)