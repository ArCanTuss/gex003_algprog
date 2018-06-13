def aviso(i):
	i = i + 1
	if i == 0:
		print("Aviso:", i);
	else:
		print("Outro aviso:", i)

def numero_par(i): 
	resto = i % 2
	resultado = resto == 0
	return resultado

for i in range(3):
	if numero_par(i):
		aviso(-1)
	else:
		aviso(i)
