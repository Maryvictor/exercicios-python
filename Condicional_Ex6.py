Nome = input("Digite o nome: ")
Peso = float(input("Digite o peso: "))
if Peso < 65:
    Categoria = "Pena"
elif Peso < 72:
    Categoria = "Leve"
elif Peso < 79:
    Categoria = "Ligeiro"
elif Peso < 86:
    Categoria = "Meio médio"
elif Peso < 93:
    Categoria = "Médio"
elif Peso < 100:
    Categoria = "Meio pesado"
else:
    Categoria = "Pesado"

print("O lutador {} pesa {} e é categoria {}".format(Nome, Peso, Categoria))

print("Fim do Programa")
    
