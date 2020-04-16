print("Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa.")
print("\nPor exemplo: OSSO e OVO são palíndromos.")
print("\nEm textos mais complexos os espaços e pontuação são ignorados.")

print("\nDescubra se uma frase é um palíndromo!")
print("**Por favor, não use acentos!**")
frase = str(input("Digite sua frase: "))

espaco = frase.replace(' ', '')

contrario = espaco[::-1]

frase2 = espaco.upper()
contrario2 = contrario.upper()

if (contrario2 == frase2):
	print("Essa frase é um palíndromo!")
else:
	print("Essa frase não é um palíndromo!")