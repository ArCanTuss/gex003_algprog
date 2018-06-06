class Aluno: #Estrutura Aluno
	matricula = 0
	n1 = 0.0
	n2 = 0.0
	
def media_aluno(aluno):
	return (aluno.n1 + aluno.n2) / 2

for i in range(5):
	print()
	aluno = Aluno()
	aluno.matricula = int(input("Informe a matrícula: "))
	aluno.n1 = float(input("Informe a nota 1: "))
	aluno.n2 = float(input("Informe a nota 2: "))
	media = media_aluno(aluno)
	print("O aluno {} possui média {:.1f}".format(aluno.matricula, media))
	
	