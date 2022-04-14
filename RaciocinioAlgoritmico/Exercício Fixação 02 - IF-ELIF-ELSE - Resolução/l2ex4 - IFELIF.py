# -*- coding: utf-8 -*-
#Informe o imposto a recolher de um salário, seguindo a tabela abaixo:


sal = float(input("Qual o salario: "))
aliquota = 0.0
          
if (sal <= 1903.98):
    aliquota = 0.0
          
elif (sal <= 2826.65):
    aliquota = 0.075
          
elif (sal <= 3751.05):
    aliquota = 0.15

elif (sal <= 4664.68):
    aliquota = 0.225

else:
    aliquota = 0.275


vlr_imp = sal * aliquota

print("O valor a recolher eh de %.2f: " % (vlr_imp))


          
