for x in range(2, 9, 2): #2, 4, 6, 8
	for y in range(1, 8, 2): #1, 3, 5, 7
		print("x={}, y={}, f(x,y)={}".format(x, y, (x + 3*x*y + y) / (2*x*y + 3*x + 4*y +2)))
