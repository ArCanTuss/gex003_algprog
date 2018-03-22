preco_parafuso = 0.10
preco_porca = 0.08
preco_arruela = 0.03

nome = input("Informe o nome do cliente: ")
qtd_parafuso = int(input("Informe o número de parafusos vendidos: "))
qtd_porca = int(input("Informe o número de porcas vendidas: "))
qtd_arruela = int(input("Informe o número de arruelas vendidas: "))

valor_parafuso = (qtd_parafuso * preco_parafuso)
valor_porca = (qtd_porca * preco_porca)
valor_arruela = (qtd_arruela * preco_arruela)

valor_total = valor_parafuso * 0.8 + valor_porca * 0.9 + valor_arruela * 0.7

print()
print("Cliente:", nome)
print("Valor de parafusos R$:", valor_parafuso)
print("Valor de porcas R$:", valor_porca)
print("Valor de arruelas R$:", valor_arruela)
print("Total de desconto R$:", (valor_parafuso + valor_porca + valor_arruela) - valor_total)
print("Total da compra R$:", valor_total)