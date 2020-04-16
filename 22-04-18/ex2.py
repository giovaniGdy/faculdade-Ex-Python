peso1 = float(input("Digite o peso1: "))
peso2 = float(input("Digite o peso2: "))
peso3 = float(input("Digite o peso3: "))

total = peso1 + peso2 + peso3
excesso = total - 500

if (excesso < 0):
	print ("Não há multa.")
elif (excesso > 0) and (excesso <= 100):
	valor_multa = (excesso * 5.0)
	print ("Valor da multa:", valor_multa)
elif (excesso > 100) and (excesso <= 500):
	valor_multa = (excesso * 8)
	print ("Valor da multa:", valor_multa)
elif (excesso > 500) and (excesso <= 1000):
	valor_multa = (excesso * 10)
	print ("Valor da multa:", valor_multa)
elif (excesso > 1000):
	valor_multa = (excesso * 15)
	print ("Valor da multa:", valor_multa)