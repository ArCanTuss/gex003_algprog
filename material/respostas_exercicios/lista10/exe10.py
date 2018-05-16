def inverte_vetor(v):
	v2 = []
	for i in range(len(v)-1, -1, -1): #percorre o vetor de traz pra frente
		v2.append(v[i])
	return v2

vetor = [2, 10, 9, 5, 3]
vetor = inverte_vetor(vetor)

print("Vetor invertido:", vetor)