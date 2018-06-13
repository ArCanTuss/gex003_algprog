contador = 0

def verifica(valor):
	global contador
	saida = 0
	if valor > contador:
		saida = 1
	contador = 5
	return saida

num = 10
contador = 100
r1 = verifica(num)
print("Verificação 1 = ", r1)
r2 = verifica(num)
print("Verificação 2 = ", r2)
