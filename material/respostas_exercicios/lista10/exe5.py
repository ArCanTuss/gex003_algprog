def equacao(x, y):
	return (x**2 + 3*x*y + y) / (2*x*y + 3*x + 4*y + 2)

#Código principal
for x in 2, 4, 6, 8:
	for y in 1, 3, 5, 7:
		print("x = {}, y = {}, (x² + 3xy + y) / (2xy + 3x + 4y +2) = {:.2f}".format(x, y, equacao(x, y)))
