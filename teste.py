print ("Código Especificação   Preço")
print (" 1     Salgado         R$4,00")
print (" 2     Cachorro Quente R$6,00")
print (" 3     Hamburguer      R$8,00")
print (" 4     X Burguer       R$10,00")
print (" 5     Refrigerante    R$4,50")
total = float(0)
cont =(input("Deseja fazer um lançamento de vendas?"))
q1 = 0
q2 = 0
q3 = 0
q4 = 0
q4 = 0
q5 = 0
while cont == "Sim":
    item = int(input("Entre com o código do item desejado:"))
    Q = int(input("Entre com a quantidade de item:"))
    if item == 1:
        preco = 4.00
        q1 = q1 + 1
    elif item == 2:
        preco = 6.00
        q2 = q2 + 1
    elif item == 3:
        preco = 8.00
        q3 = q3 + 1
    elif item == 4:
        preco = 10.00
        q4 = q4 + 1
    elif item == 5:
        preco = 4.50
        q5 = q4 + 1
    else:
        print ("Código inválido")
        total = 0
        break

    valor = float(Q * preco)
    print ("{} - {} - {}",Q,preco,valor)
    #Para calculo do total deverão ser somados todos os valores
    total = 
cont = (input("Deseja lançar mais itens [Sim/Não]?")       
print ("Foram vendidos 1:{} unidades - 2:{} unidades - 3:{} unidades - 4:{} uinidades - 5:{} unidades", q1,q2,q3,q4,q5)                   
print ("O total foi de R${}",total)                    
                                     
       
               
               
    
