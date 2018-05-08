import turtle 

des = turtle.Turtle()

tam = 110
tamDecr = 10
x = 0
y = 0
posAlt = 5

for i in range(10): #Laço para gerar os 10 quadrados
	for j in range(4): #Laço para gerar cada um dos quadrados
		des.forward(tam)
		des.right(90)
	
	tam -= tamDecr
	x += posAlt
	y -= posAlt
	
	des.penup()
	des.setposition(x, y)
	des.pendown()
	
turtle.done()
