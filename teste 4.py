print ("Código Especificação   Preço")
print (" 1     Salgado         R$4,00")
print (" 2     Cachorro Quente R$6,00")
print (" 3     Hamburguer      R$8,00")
print (" 4     X Burguer       R$10,00")
print (" 5     Refrigerante    R$4,50")
total = float(0)
cont = str("Sim")
i = int(1)
print(input("Deseja fazer um pedido?"))      
while cont == "Sim":
    item = int(input("Entre com o código do item desejado:"))
    if item > 5:
        print ("Código inaválido")
        break
    Q = int(input("Entre com a quantidade de item:"))
         if item == 1:
           preco = 4.00
         elif item == 2:
           preco = 6.00
         elif item == 3:
           preco = 8.00
         elif item == 4:
           preco = 10.00
         elif item == 5:
           preco = 4.50
         else:
        
    valor = float(Q * preco)
    print ("{} - {} - {} - {} - {}",Q,i,item,preco,valor)
    total = total + valor
    i = i + 1
cont = (input("Deseja mais itens [Sim/Não]?")
    print("Total da compra:R${}",total)
    
                   
