impar = False #Variável para controlar se algum número ímpar foi digitado 
maior = -10000000 #Se um número bem pequeno como maior

n1 = int(input("Digite o número 1: "))
if n1 % 2 != 0:
	impar = True
	if n1 > maior:
		maior = n1

n2 = int(input("Digite o número 2: "))
if n2 % 2 != 0:
	impar = True
	if n2 > maior:
		maior = n2
			
n3 = int(input("Digite o número 3: "))	
if n3 % 2 != 0:
	impar = True
	if n3 > maior:
		maior = n3

if impar:
	print("Maior número ímpar:", maior)
else:
	print("Nenhum número ímpar foi informado")