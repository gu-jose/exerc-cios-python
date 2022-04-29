print(' vamos  pintar   a megumin  no quarto , quantas latas de tinta e necessario ? \n  vamos  ver !')
print('='*12)
larg = float(input(' quantos de largura  tem a parede  em que vocẽ  vai pintar  a megumin ? '))
alt = float(input(' qual  e  altura da parede  ?'))
area = larg*alt
print('   as  medidas  que  você  vai usar para pintar  a parede são {} x {}  e area dessa parede e {}'.format(larg, alt, area))
tinta = area/2
print('  e vocẽ  tambem precisarar de  {} litros de tinta para  pintar a megumin '.format(tinta))
