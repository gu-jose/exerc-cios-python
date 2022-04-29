print(' ===============================desafio 08 -========================')
medida = float(input(' uma  distancia em metros :'))
cm = medida * 100
mm = medida * 1000
print(' a  medida  de  {}  em  cm e {:.1f} e  em mm e {:.1f}  '.format(medida ,  cm  ,  mm ))	

print('======================   mais  dificil ======================')
m = float(input(' uma  distancia em metros '))
km = m / 1000
hc = m  / 100
dc = m / 10
dm = m * 10
cm = m  * 100
ml = m  * 1000 
print('{} em quilometros e {}km , \n   {} em hectometro e {}hc '.format (m ,  km , m , hc ))
print('{} em  decâmetro  {}dc  \n  {}  em  decimetro  e {}dm '.format (m, dc , m , dm ))
print('{} em  centimetro e {}cm  \n e  {} em  milemetro  e {}ml '.format (m , cm , m , ml ))
			   
			   
