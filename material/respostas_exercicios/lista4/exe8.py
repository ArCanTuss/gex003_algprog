nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
opcao = int(input("Informe a opção de média: "))
	
if opcao == 1:
	print("Média aritmética:", (nota1 + nota2 + nota3) / 3)
elif opcao == 2:
	print("Média ponderada (3, 3, 4):", (nota1*3 + nota2*3 + nota3*4) / 10)
else:
	print("Opção inválida")