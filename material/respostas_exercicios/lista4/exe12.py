salario_bruto = float(input("Informe o salário bruto: "))

imposto = 0
salario_aux = salario_bruto

#Faixa 5
salario_faixa = salario_aux - 4664.68
if salario_faixa > 0:
	imposto = imposto + (salario_faixa * 0.275)
	salario_aux = salario_aux - salario_faixa
	
#Faixa 4
salario_faixa = salario_aux - 3751.05
if salario_faixa > 0:
	imposto = imposto + (salario_faixa * 0.225)
	salario_aux = salario_aux - salario_faixa
	
#Faixa 3
salario_faixa = salario_aux - 2826.65
if salario_faixa > 0:
	imposto = imposto + (salario_faixa * 0.15)
	salario_aux = salario_aux - salario_faixa
	
#Faixa 2
salario_faixa = salario_aux - 1903.98
if salario_faixa > 0:
	imposto = imposto + (salario_faixa * 0.075)
	salario_aux = salario_aux - salario_faixa

print("Valor de imposto = R$ {:.2f} | Salário líquido = R$ {:.2f} | Alíquota efetiva: {:.2f}%".format(imposto, salario_bruto - imposto, (imposto/salario_bruto)*100))
