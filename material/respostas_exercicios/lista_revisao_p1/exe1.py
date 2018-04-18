print("início")

for j in range(2):
	i = j + 2
	y = 1
	
	while y >= 0:
		k = y;
		if j == 0 or y == 9: 
			z = j + y * 2
			if z == 0:
				print("X", end="")
			elif y == 2 or y == 0:
				print("Y", end="")
			else:
				print("Z", end="")
		else:
			if j < 1 and y != 0:
				print("S", end="")
		
		y -= 1
		print("W")
	print("-")

print("fim")
