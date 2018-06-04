arquivo = open("numeros.txt", "r")

maior = -999999999

linhas = arquivo.read().splitlines() #Leitura do arquivo
for lin in linhas:
	numero = float(lin)
	if numero > maior:
		maior = numero
arquivo.close()

print("Maior número do arquivo [numeros.txt]:", maior)
