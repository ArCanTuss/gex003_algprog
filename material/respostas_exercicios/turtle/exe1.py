import turtle 

des = turtle.Turtle()

for i in range(4): #Laço para gerar os quatro lados do quadrado
	des.forward(100)
	des.right(90)
	
des.penup()
des.setposition(10, -10)
des.pendown()

for i in range(4): #Laço para gerar os quatro lados do quadrado
	des.forward(80)
	des.right(90)
	
turtle.done()
