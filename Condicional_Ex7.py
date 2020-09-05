A = 0
while A == 0:
    A = float(input("Digite coeficiente A: "))
B = float(input("Digite coeficiente B: "))
C = float(input("Digite coeficiente C: "))
print("Equação de segundo grau usando: A = {}, B = {}, C = {}".format(A, B, C))
Delta = B ** 2 - 4 * A * C
if Delta > 0:
    X1 = (-B - Delta ** 0.5) / (2 * A)
    X2 = (-B + Delta ** 0.5) / (2 * A)
    print("As raízes são: X1 = {:.3} e X2 = {:.3}".format(X1, X2))
elif Delta == 0:
    X = -B / (2 * A)
    print("As raízes são iguais: X1 = X2 = {:.3}".format(X))
else:
    print("Não tem raízes reais")
print("Fim do Programa")
    
