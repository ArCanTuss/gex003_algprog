import csv
import matplotlib.pyplot as pyplot
import numpy as np

def leArquivoCSV(nomeArquivo):
	matriz = []
	arquivo = open(nomeArquivo, 'r')
	leitorcsv = csv.reader(arquivo)
	for linhaArq in leitorcsv: 
		linhaMat = [] #Cria a linha da matriz
		linhaMat.append(float(linhaArq[0])) #Adiciona o ponto X
		linhaMat.append(float(linhaArq[1])) #Adiciona o ponto Y
		matriz.append(linhaMat)
	
	arquivo.close()
	return matriz

#Código principal
matriz = leArquivoCSV("xy.csv")

valoresX = []
valoresY = []

for linhaMatriz in matriz:
	valoresX.append(float(linhaMatriz[0]))
	valoresY.append(float(linhaMatriz[1]))
	
#Gera o gráfico
pyplot.plot(np.array(valoresX), np.array(valoresY))
pyplot.show()
