segundos = int(input("Ingrese la cantidad de segundos:"))
horas = segundos//3600
minutos = (segundos%3600)/60

print(f"{segundos} segundos equivalen a {horas} horas y {minutos} minutos.")
