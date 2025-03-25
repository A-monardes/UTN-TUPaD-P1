# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print ("Hola mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre1 = input("Ingrese su nombre: ")
print(f"Hola {nombre1}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre2 = input("Ingresa tu nombre:")
apellido = input("Ingresa tu apellido:")
edad = int(input("Ingresa tu edad:"))
residencia = input("Ingresa tu residencia:")

print(f"Soy {nombre2} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio = int(input("Ingrese el radio del circulo:"))
area = 3.14*radio**2
perimetro = 2*3.14*radio

print(f"El area del circulo es de {area} y su perimetro es de {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = int(input("Ingrese la cantidad de segundos:"))
horas = segundos//3600
minutos = (segundos%3600)/60

print(f"{segundos} segundos equivalen a {horas} horas y {minutos} minutos.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

num = int(input("Ingrese un numero:"))

print(f"La tabla del {num} es:\n{num}x1= {num*1}\n{num}x2= {num*2}\n{num}x3= {num*3}\n{num}x4= {num*4}\n{num}x5= {num*5}\n{num}x6= {num*6}\n{num}x7= {num*7}\n{num}x8= {num*8}\n{num}x9= {num*9}\n{num}x10= {num*10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

n1 = int(input("Introduci un numero distinto a 0:"))
n2 = int(input("Introduci otro:"))

print(f"La suma de {n1} y {n2} es {n1+n2}\nLa resta de {n1} y {n2} es {n1-n2}\nLa multiplicacion de {n1} y {n2} es {n1*n2}\nLa division de {n1} y {n2} es {n1/n2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. 

altura = float(input("Introduci tu altura en metros:"))
peso = float(input("Introduci tu peso en kilogramos:"))

imc = peso/(altura**2)

print(f"Tu indice de masa corporal es {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.

temp = float(input("Introduci la temperatura en Celsius "))

print(f"La temperatura {temp}°C en Fahrenheit es {((9/5)*temp)+32}°F")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

ni = float(input("Introduci 3 numeros para conocer su promedio: "))
nii = float(input())
niii = float(input())

print(f"El promedio de los 3 numeros es {(ni+nii+niii)/3:.2f}")