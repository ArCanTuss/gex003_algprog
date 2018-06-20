class Computador:
	processador = ""
	qtd_ram = 0
	qtd_hd = 0
	
def ler_computador():
	comp = Computador()
	print()
	comp.processador = input("Informe o processador: ")
	comp.qtd_ram = int(input("Informe a memória RAM (GB): "))
	comp.qtd_hd = int(input("Informe a memória HD (GB): "))
	return comp
	
def imprimir_computador(comp):
	print()
	print("Processador:", comp.processador)
	print("RAM (GB):", comp.qtd_ram)
	print("HD (GB):", comp.qtd_hd)
	
#Principal
computadores = []
for i in range(3):
	computadores.append(ler_computador())
	
print("\nImpressão de computadores:")
for comp in computadores:
	imprimir_computador(comp)
	
	
