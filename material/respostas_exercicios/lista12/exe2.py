class Banda: #Estrutura Banda
	nome = ""
	estilo = ""
	integrantes = 0
	
bandas = []
for i in range(5):
	print()
	banda = Banda()
	banda.nome = input("Informe o nome da banda: ")
	banda.estilo = input("Informe o estilo musical da banda: ")
	banda.integrantes = int(input("Informe o númerio de integrantes da banda: "))
	bandas.append(banda)

print()
num = int(input("Informe um número de 1 a 5: "))	
bandaSelecionada = bandas[num-1]

print()
print("Nome da banda:", bandaSelecionada.nome)
print("Estilo da banda:", bandaSelecionada.estilo)
print("Integrantes da banda:", bandaSelecionada.integrantes)
