string1 = str(input("Diga uma String: "))
string2 = str(input("Diga outra String: "))

tamanho1 = len(string1)
tamanho2 = len(string2)

print("\n'", string1, "'", "Possui:", tamanho1, "Caracteres.")
print("\n'", string2, "'", "Possui:", tamanho2, "Caracteres.")

if (tamanho1 == tamanho2):
	print("\nAmbas as Strings possuem o mesmo tamanho.")
else:
	print("\nAs Strings possuem tamanhos diferentes.")