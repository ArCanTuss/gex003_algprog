conta = input("Informe a conta bancária: ")
saldo = float(input("Informe saldo atual R$: "))
operacao = input("Informe a operação (D ou R): ")
if operacao == "D" or operacao == "R":
	valor = float(input("Informe o valor da operação R$: "))
	if operacao == "D":
		novo_saldo = saldo + valor;
	else:
		novo_saldo = saldo - valor;
		
	print()
	print("A conta", conta, "possui saldo de R$", novo_saldo)
	if novo_saldo < 0:
		print("ATENÇÂO! Conta estourada!")
else:
	print("Operação inválida!")