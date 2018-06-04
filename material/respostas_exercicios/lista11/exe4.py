import csv

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

#A - Total de vendas para cada cliente
clientes    = []
valor_venda = []
for linhaArq in leitorcsv: 
	if clientes.count(linhaArq[col_cliente]) > 0: #Se o cliente existe na lista 
		idx = clientes.index(linhaArq[col_cliente]) #Recupera o índice do vetor onde o cliente foi inserido
		valor_venda[idx] += float(linhaArq[col_valor_venda])   #Incrementa o valor da venda no índice correspondente ao cliente
	else:
		clientes.append(linhaArq[col_cliente]) #Inicializa os vetores, inserindo o cliente e o valor da venda
		valor_venda.append(float(linhaArq[col_valor_venda]))

print("\nA - Total de vendas para cada cliente")
for i in range(len(clientes)):
	print("Cód. cliente: {0} - Vendas: R$ {1:7.2f}".format(clientes[i], valor_venda[i]))

#B - Total de vendas para cada produto
produtos = []
valor_venda.clear()
arquivo.seek(0) #Retorna o curso para o início do arquivo
for linhaArq in leitorcsv: 
	if produtos.count(linhaArq[col_produto]) > 0: #Se o produto existe na lista 
		idx = produtos.index(linhaArq[col_produto]) #Recupera o índice do vetor onde o produto foi inserido
		valor_venda[idx] += float(linhaArq[col_valor_venda])   #Incrementa o valor da venda no índice correspondente ao produto
	else:
		produtos.append(linhaArq[col_produto]) #Inicializa os vetores, inserindo o produto e o valor da venda
		valor_venda.append(float(linhaArq[col_valor_venda]))

print("\nB - Total de vendas para cada produto")
for i in range(len(produtos)):
	print("Cód. produto: {0} - Vendas: R$ {1:7.2f}".format(produtos[i], valor_venda[i]))
	
#C - Total de vendas
total_vendas = 0
arquivo.seek(0) #Retorna o cursor para o início do arquivo
for linhaArq in leitorcsv:
	total_vendas += float(linhaArq[col_valor_venda])
print("\nC - Total de vendas: R$ {0:7.2f}".format(total_vendas))

arquivo.close()



