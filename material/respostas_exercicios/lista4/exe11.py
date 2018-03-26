dias     = int(input("Informe a quantidade de dias: "))
horas    = int(input("Informe a quantidade de horas: "))
minutos  = int(input("Informe a quantidade de minutos: "))
segundos = int(input("Informe a quantidade de segundos: "))

segundos = segundos + (dias*60*60*24) + (horas*60*60) + (minutos*60)
print("Você esperou", segundos, "segundos")