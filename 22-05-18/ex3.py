import csv

with open( 'produtos.csv', 'w', newline = '') as ex3:
	writer = csv.writer(ex3)
	writer.writerow(['Descricao,Preco'])
	writer.writerow(['Mouse,15.00'])
	writer.writerow(['Teclado,28.00'])
	writer.writerow(['Monitor Full HD,522.11'])
	writer.writerow(['SSD 120GB,199,00'])
	writer.writerow(['Pendrive 16GB,28.00'])