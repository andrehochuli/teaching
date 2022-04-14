# -*- coding: utf-8 -*-
#Implemente um seletor de canais para informar que canal a pessoa está assistindo:
num = input("Digite o número do canal: ")
num = int(num)



if (num == 2):
    print("Bandeirantes")
elif (num == 4):
    print("SBT")
elif (num == 6):
    print("CNT")
elif (num == 7):
    print("RECORD")
elif (num == 9):
    print("CULTURA")
elif (num == 12):
    print("GLOBO")
else:
    print("Canal Invalido")
