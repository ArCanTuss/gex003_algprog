class Data: #Estrutura Data
	ano = 0
	mes = 0
	dia = 0

maiorData = Data()

for i in range(5):
	data = Data()
	print()
	data.ano = int(input("Informe o ano: "))
	data.mes = int(input("Informe o mês: "))
	data.dia = int(input("Informe o dia: "))
	
	maiorAno = data.ano > maiorData.ano
	maiorMes = data.ano == maiorData.ano and data.mes > maiorData.mes
	maiorDia = data.ano == maiorData.ano and data.mes == maiorData.mes and data.dia > maiorData.dia
	print(maiorAno, maiorMes, maiorDia)
	
	if maiorAno or maiorMes or maiorDia:
		print("Entrou")
		maiorData = data

print()
print("Maior data:")
print("{}/{}/{}".format(maiorData.dia, maiorData.mes, maiorData.ano))