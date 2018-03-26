segundos = int(input("Informe a quantidade de segundos: "))

dias  = segundos // (60*60*24)
resto = segundos % (60*60*24)

horas = resto // (60*60)
resto = resto % (60*60)

minutos = resto // 60
segundos = resto % 60

print("Você esperou", dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos")