mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
	   "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

while True:
	num = int(input("Informe um número de 1 à 12: "))
	if num >= 1 and num <= 12:
		break;
	else:
		print("Número inválido!")
		
print("Mês:", mes[num-1])
