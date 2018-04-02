salarioAlto = -9999999999999999
salarioBaixo = 9999999999999999

acuSalario = 0
contaFunc  = 0
nomeAlto = ""
nomeBaixo = ""

nome = input("Informe o nome do funcionário: ")
while nome != "fim":
	salario = float(input("Informe o salário: "))
	acuSalario += salario
	contaFunc += 1
	
	if salario > salarioAlto:
		salarioAlto = salario
		nomeAlto = nome
	
	if salario < salarioBaixo:
		salarioBaixo = salario
		nomeBaixo = nome
	
	print()
	nome = input("Informe o nome do funcionário: ")

print()
if contaFunc > 0:
	print("Salario mais baixo: {0}, R$ {1:.2f}".format(nomeBaixo, salarioBaixo))
	print("Salario mais alto: {0}, R$ {1:.2f}".format(nomeAlto, salarioAlto))
	print("Média dos salários: R$ {:.2f}".format(acuSalario/contaFunc))
else:
	print("Nenhum funcionário informado!")