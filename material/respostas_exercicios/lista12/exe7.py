import csv

class Venda:
	codCliente = 0
	codProduto = 0
	valor = 0.0

class VendaCliente:
	codCliente = 0
	valor = 0.0

'''
Dicionário de dados do arquivo:
Coluna 1: código do cliente
Coluna 2: código do produto
Coluna 3: valor da venda
'''
col_cliente = 0
col_produto = 1
col_valor_venda = 2

arquivo = open("vendas.csv", 'r')
leitorcsv = csv.reader(arquivo)

#Leitura do arquivo para a estrutura
vendas = []
for linhaArq in leitorcsv: 
	venda = Venda()
	venda.codCliente = linhaArq[col_cliente]
	venda.codProduto = linhaArq[col_produto]
	venda.valor = float(linhaArq[col_valor_venda])
	vendas.append(venda)

arquivo.close() #Fecha o arquivo, pois já está armazenado na estrutura

#Imprime todas a vendas
for v in vendas:
	print()
	print("Cód. Cliente:", v.codCliente)
	print("Cód. Produto:", v.codProduto)
	print("Valor: {:.2f}".format(v.valor))


