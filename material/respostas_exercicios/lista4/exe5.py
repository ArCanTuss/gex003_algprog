nome = input("Informe o nome do funcionário: ")
categoria = input("Informe a categoria do funcionário: ")
salario = float(input("Informe o salário do funcionário: "))

if categoria in "ACFH":
	salario = salario * 1.10
elif categoria in "BDEIJT":
	salario = salario * 1.15
elif categoria in "KR":
	salario = salario * 1.25
elif categoria in "LMNOPQS":
	salario = salario * 1.35
elif categoria in "UVXYWZ":
	salario = salario * 1.50

print()
print("Nome:", nome)
print("Categoria:", categoria)
print("Salário reajustado:", salario)
