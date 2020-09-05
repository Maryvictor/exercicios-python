# PG
N = int(input("Digite a quantidade de termos: "))
P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))
Soma = 0
i = 1
while i <= N:
    print(P, end=" ")
    Soma = Soma + P
    P = P * R
    i = i + 1
print("\nSoma de todos = ", Soma)
print("\n\n\nFim do Programa")
    
