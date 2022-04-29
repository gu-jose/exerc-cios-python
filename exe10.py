print('============conversor  de moeda==================' )
real = float(input('quanto   de dinheiro vocẽ tem na  carteira ?'))
dolar = real/5.43
euro  = real*6.1
print('com  {:.2f}R$ voce pode comprar  {:.2f} USD '.format(real, dolar))
print(' com  {:.2f}R$  vocẽ pode comprar {:.2f}€ '.format(real, euro))