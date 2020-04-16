numero = int(input("Digite um número inteiro: "))

fat = 1
i = 0

for i in range(1, numero):
	fat = fat * i

print ("O fatorial de", numero, "é igual a", fat)