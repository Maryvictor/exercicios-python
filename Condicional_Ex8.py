A = float(input("Digite o lado A: "))
B = float(input("Digite o lado B: "))
C = float(input("Digite o lado C: "))

if A + B > C and A + C > B and B + C > A:
    if A == B and A == C:
        print("Triangulo Equilátero")
    elif A == B or A == C or B == C:
        print("Triangulo Isóceles")
    else:
        print("Triangulo Escaleno")
else:
    print("Não é Triangulo")
    

print("Fim do Programa")
    
