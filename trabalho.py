print ("Especificação Código Preço")
print ("Salgado 1 R$4.00")
print ("Cachorro Quente 2 R$6.00")
print ("Hamburguer 3 R$8.00")
print ("X Burguer 4 R$10.00")
print ("Refrigerante 5 R$4.50")
total=float(0)
cont='S'
i = int(1)
while (cont == 'S'):
    item = int(raw_input("Entre com o item desejado:"))
    qnt = int(raw_input("Entre com a quantidade do item:"))
    if item == 1:
                        preco = 4.00
    elif item == 2:
                        preco = 6.00
    elif item == 3:
                        preco = 8.00
    elif item == 4:
                        preco =10.00
                        
    elif item ==5:
                        preco = 4.50
    else:
                        print ("Código Inválido)                
                        total = 0
 break
                               val = float (qnt*preco)
                               print("{} - {} - {} - {} - {}",format ((i,item,qnt,preco,val))
                                     
