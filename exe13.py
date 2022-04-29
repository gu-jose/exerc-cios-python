print('=============== reajuste salarial ============')
salario =float(input('qual e o seu salario ? '))
novo = salario + (salario*15/100)
print('um funcionario que ganhava R${:.2f} com 15% de aumento de aumento, passa a receber R${} '.format(salario, novo))			   
			   