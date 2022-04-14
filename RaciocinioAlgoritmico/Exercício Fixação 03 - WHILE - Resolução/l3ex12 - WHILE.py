#Juros Compostos: Calcule quanto um investimento deve render em X anos. Imprima a evolução do montante ano a ano
valor = float(input("Qual o montante a ser investido?"))
juros = float(input("Qual a taxa de juros anual?"))
anos = int(input("Por quantos anos deseja manter o investimento?"))


#Converto o juros entre 0 e 1
juros = juros/100.

i = 1
while( i <= anos):
    
    valor += valor*juros
    print("Em %d anos, o montante será de R$ %.2f" % (i,valor))
    i+=1
