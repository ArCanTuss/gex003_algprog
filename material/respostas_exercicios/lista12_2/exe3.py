class Jogo:
	nome = ""
	estilo = ""
	fabricante = ""
	precoUSS = 0.0
	
def ler_jogo():
	jogo = Jogo()
	print()
	jogo.nome = input("Informe o nome do jogo: ")
	jogo.estilo = input("Informe o estilo do jogo: ")
	jogo.fabricante = input("Informe o fabricante do jogo: ")
	jogo.precoUSS = float(input("Informe o preço do jogo (US$): "))
	return jogo

def imprime_jogo(jg):
	print("\nDados do jogo:")
	print("Nome:", jg.nome)
	print("Estilo:", jg.estilo)
	print("Fabricante:", jg.fabricante)
	print("Preço US$: {:.2f}".format(jg.precoUSS))
	print("Preço R$: {:.2f}".format(jg.precoUSS * 3.98))


#Principal...
jogos = []
for i in range(5):
	jogos.append(ler_jogo())

for jogo in jogos:
	imprime_jogo(jogo)
