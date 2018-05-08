import turtle 

des = turtle.Turtle()
des.penup()
des.backward(500)
des.pendown()

tam = 150

for i in range(10): #Laço para gerar os 10 triângulos
	for j in range(3): #Laço para gerar os 3 lados do triângulo
		des.forward(tam)
		des.left(120)
	
	des.penup()
	des.forward(tam + 15)
	des.pendown()
	
	tam -= 15

	
turtle.done()
