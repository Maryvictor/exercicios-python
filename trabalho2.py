cont = 0
arq = open('vendas.txt' , encoding = 'utf-8')
L = arq.readlines()
for a in L:
    a = a.strip().split(";")
    print(a)
    cod = int(a[0])
    q = int(a[1])
    v = float(a[2]

L 0]=(int("Digite o código"))
    if cod >= 10000 ^ cod <= 21000 :
              
            total = q*v
            print(total)
            cont = cont + 1  
    elif cod == 0:
              
                break
         
    else:
                print("Código Inválido")
            
