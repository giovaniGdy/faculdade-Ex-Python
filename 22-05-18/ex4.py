import csv

total = float(0)
num = 0

with open( 'produtos.csv', 'r' ) as ex3:
	info = csv.DictReader(ex3, delimiter = ',')

	for linha in info:
		total = (total + float(linha['Preco']))
		num += 1
		media = (total / num)

		print(media)
		print(total)