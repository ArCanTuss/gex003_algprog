class Aluno:
	matricula = 0
	n1 = 0.0
	n2 = 0.0
	n3 = 0.0

def le_aluno():
	aluno = Aluno()
	aluno.matricula = int(input("Informe matrícula do aluno: "))
	aluno.n1 = float(input("Informe a nota 1 do aluno: "))
	aluno.n2 = float(input("Informe a nota 2 do aluno: "))
	aluno.n3 = float(input("Informe a nota 3 do aluno: "))
	return aluno

def imprime_turma(lista_alunos):
	for aluno in lista_alunos:
		print("\nAluno: ", aluno.matricula)
		print("Notas:", aluno.n1, aluno.n2, aluno.n3)

def calcula_media_aluno(aluno):
	soma = aluno.n1 + aluno.n2 + aluno.n3
	return soma / 3


#Código principal...
turma = []
for i in range(5):
	turma.append( le_aluno() ) #Função que lê a matrícula e 3 notas de um aluno, retornando-o
   
imprime_turma(turma) #Função que imprime os dados de todos os alunos
 
print()
for i in range(5):
	media = calcula_media_aluno(turma[i]) #Função que calcula e retorna média de um aluno
	print("Aluno: {} - Média: {:.1f}".format(turma[i].matricula, media))
