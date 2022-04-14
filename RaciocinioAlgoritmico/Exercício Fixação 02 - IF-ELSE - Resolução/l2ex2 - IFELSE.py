# -*- coding: utf-8 -*-
#Informe se a pessoa digitou uma vogal ou consoante
L = input("Digite uma letra: ")

#Utilizo 'ou' pois apenas uma delas precisa ser True
if (L == 'a' or L == 'e' or  L == 'i' or L == 'o' or L == 'u'):
    print('A letra digitada é uma vogal')
else:
    print('A letra digitada é uma consoante')
