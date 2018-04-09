produto = 1
for num in range(1, 16):
	if num % 2 == 1:
		produto *= num

print("Produto dos impares de 0 a 15: ", produto)