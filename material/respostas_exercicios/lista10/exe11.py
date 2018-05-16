def uniao(vetA, vetB):
	vetC = []
	for val in vetA: #Adiciona os elementos do vetor A
		vetC.append(val)
	
	for val in vetB: #Adiciona os elementos do vetor B
		vetC.append(val)
	
	vetC.sort()
	return vetC

A = [3, 4, 5, 6, 7, 8, 10, 11, 25, 45]
B = [21, 24, 25, 36, 17, 18, 9, 1, 2, 55]

C = uniao(A, B)
print(C)