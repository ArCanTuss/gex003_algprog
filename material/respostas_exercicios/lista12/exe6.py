class NomePessoa:
	nome = ""
	sobrenome = ""

#Código principal
pes = NomePessoa()
pes.nome = input("Informe o primeiro nome da pessoa: ")
pes.sobrenome = input("Informe o sobrenome da pessoa: ")

print()
print(pes.nome + " " + pes.sobrenome) #Para concatenar strings, utilizar o operador +
nomeInvertido = ""
for c in pes.nome:
	nomeInvertido = c + nomeInvertido
nomeInvertido = " " + nomeInvertido  #Adiciona um espaço entre o nome e o sobrenome
for c in pes.sobrenome:
	nomeInvertido = c + nomeInvertido	
print(nomeInvertido)
