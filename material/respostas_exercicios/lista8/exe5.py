#Leitura do gabarito
gabarito = []
print("----Gabarito----")
for i in range(13):
	n = int(input("Informe o jogo {}: ".format(i+1)))
	gabarito.append(n)

#Leitura do aposta
aposta = []
print("\n----Aposta----")
for i in range(13):
	n = int(input("Informe o jogo {}: ".format(i+1)))
	aposta.append(n)

#Calcula a qtd de acertos
qtdAcertos = 0
for i in range(13):
	if gabarito[i] == aposta[i]:
		qtdAcertos += 1 
	
print("\nNúmero de acertos:", qtdAcertos)
if qtdAcertos == 13:
	print("GANHADOR, PARABÉNS")