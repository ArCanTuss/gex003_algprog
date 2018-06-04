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

#Leitura do arquivo e cálculo do valor total de vendas por cliente
arquivo = open("vendas.csv", 'r')
leitorcsv = csv.reader(arquivo)

clientes    = []
valor_venda = []
for linhaArq in leitorcsv: 
	if clientes.count(linhaArq[col_cliente]) > 0: #Se o cliente existe na lista 
		idx = clientes.index(linhaArq[col_cliente]) #Recupera o índice do vetor onde o cliente foi inserido
		valor_venda[idx] += float(linhaArq[col_valor_venda])   #Incrementa o valor da venda no índice correspondente ao cliente
	else:
		clientes.append(linhaArq[col_cliente]) #Inicializa os vetores, inserindo o cliente e o valor da venda
		valor_venda.append(float(linhaArq[col_valor_venda]))

arquivo.close()

#Escrita do novo arquivo
'''
Dicionário de dados do novo arquivo:
Coluna 1: código do cliente
Coluna 2: valor total de vendas para o cliente
'''
arquivo_saida = open("vendas_cliente.csv", 'w')
for i in range(len(clientes)):
	print("{0},{1:.2f}".format(clientes[i], valor_venda[i]), file=arquivo_saida)
arquivo_saida.close()

print("Arquivo vendas_cliente.csv escrito com sucesso!")
