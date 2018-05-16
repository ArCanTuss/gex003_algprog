def possuiNoVetor(n, vet):
	for i in vet:
		if i == n:
			return True
	
	return False;

def uniao(vetA, vetB):
	vetC = []
	for val in vetA: #Adiciona os elementos do vetor A
		if not possuiNoVetor(val, vetB):
			vetC.append(val)
	
	qtdFalta = 10 - len(vetC) #Adiciona 0 até o vetor possuir 10 elementos
	for i in range(qtdFalta):
		vetC.append(0)
	
	return vetC

A = [3, 4, 5, 6, 7, 8, 10, 11, 25, 45]
B = [21, 8, 25, 10, 17, 25, 9, 1, 2, 55]

C = uniao(A, B)
print(C)