class Data: #Estrutura Data
	ano = 0
	mes = 0
	dia = 0

def ler_data():
	data = Data()
	print()
	data.ano = int(input("Informe o ano: "))
	data.mes = int(input("Informe o mês: "))
	data.dia = int(input("Informe o dia: "))
	return data
	

menorData = ler_data()

for i in range(5):
	data = ler_data()
	
	menorAno = data.ano < menorData.ano
	menorMes = data.ano == menorData.ano and data.mes < menorData.mes
	menorDia = data.ano == menorData.ano and data.mes == menorData.mes and data.dia < menorData.dia
	
	if menorAno or menorMes or menorDia:
		menorData = data

print()
print("Menor data:")
print("{}/{}/{}".format(menorData.dia, menorData.mes, menorData.ano))
