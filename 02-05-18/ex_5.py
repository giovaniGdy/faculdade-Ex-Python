frase = str(input("Digite uma frase: "))

nospace = frase.strip()
qntdpalavras = nospace.count(' ')

valorfinal = (qntdpalavras + 1)

print("Sua frase possui", valorfinal, "palavras!")