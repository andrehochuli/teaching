plv="#@nDr3Gust@v045#"
cont_maisc = 0
cont_minus = 0
cont_espec = 0
cont_nums = 0

#Varre a string 
print(plv)
for i in range(0,len(plv)):
    

    #ORD: Converte ASCII
    cod_asc = ord(plv[i])

    #Maisculas
    if cod_asc >= 65 and cod_asc <= 90: 
        cont_maisc += 1
        min_char = chr(cod_asc + 32)
        print(min_char,end='')

    #Minusculas   
    elif cod_asc >= 97 and cod_asc <= 122:
        cont_minus += 1
        mais_char = chr(cod_asc - 32)
        print(mais_char,end='')

    #Numeros 0-9
    elif cod_asc >= 48 and cod_asc <= 57:
        cont_nums += 1
        print(plv[i],end='')
    else:
        cont_espec += 1      
        print(plv[i],end='')

print("\nMaisculas: ",cont_maisc)
print("Minusculas: ",cont_minus)
print("Numeros: ", cont_nums)
print("Especiais: ",cont_espec)

if len(plv) < 8:
    print("Tamanho minimo 8")
elif cont_maisc < 2:
    print("Minimo 2 maiusculos")
elif cont_nums < 2:
    print("Minimo 2 numeros")
elif cont_espec < 3:
    print("Minimo 3 especiais")
else:
    print("Senha valida")








