soma = 0

print("Números pares entre 85 e 907:")
for i in range(85, 908):
	if (i % 2) == 0:
		print(i, end="\t")
		soma = soma + i

print()
print("Soma dos números pares entre 85 e 907: ", soma)