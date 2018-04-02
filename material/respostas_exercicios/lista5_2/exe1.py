conta = input("Informe o número da conta: ")
saldo = float(input("Informe o saldo da conta: "))

print()
valor_op = float(input("Informe o valor da operação: "))
while valor_op != 0:
	op = input("Informe o tipo da operação (D) ou (R): ")
	if op.upper() == "D" or op.upper() == "R":
		if op.upper() == "D":
			saldo = saldo + valor_op
		else: #retirada
			saldo = saldo - valor_op
		
		print("Novo saldo = R$ {:.2f}".format(saldo))
		print()
	
		valor_op = float(input("Informe o valor da operação: "))
	else:
		print("Operação inválida!")
		print()
	
print()
print("Conta: {0} | Saldo: R$ {1:.2f}".format(conta, saldo))
if saldo < 0:
	print("Conta estourada!")
