SomaPos = 0
SomaNeg = 0
X = int(input("Digite X: "))
while X != 0:
    if X > 0:
        SomaPos = SomaPos + X
    else:
        SomaNeg = SomaNeg + X
    X = int(input("Digite X: "))
    if X == 99:
        break

print("Soma dos positivos = {}".format(SomaPos))
print("Soma dos negativos = {}".format(SomaNeg))

print("\n\n\nFim do Programa")
    
