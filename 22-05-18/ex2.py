ex2 = open( 'carros.txt', 'r' )

linhas = ex2.readlines()
linhas.sort()

print(linhas)

ex2.close()