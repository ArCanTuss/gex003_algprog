import math #biblioteca para a função de raiz quadrada

a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))

delta = b**2 - (4*a*c)

if delta > 0:
	raiz1 = (-b + math.sqrt(delta)) / (2 * a)
	raiz2 = (-b - math.sqrt(delta)) / (2 * a)
	print("As raizes são:", raiz1, raiz2)
else:
	print("A equação não possui raízes que pertencem aos números reais")