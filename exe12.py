print('============= calculando desconto ================')
preço = float(input(' qual e o preço do  produto R$'))
novo =  preço - (preço*5/100)
print(' o produto  que  custava R${} ,  na  promoção com  desconto de 5%  vai custar  R${}'.format(preço, novo))