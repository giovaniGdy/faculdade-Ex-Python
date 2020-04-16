print ("Equação 1° grau => -ax + b = 0")

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))

if (a != 0):
	x = -(b/a)
	print ("Resultado de x é: ", x)
else:
	print ("Não há raizes reais.")