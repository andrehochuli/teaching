#A partir de três notas de um aluno e informe se ele passou por média (7.0 ou mais)

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
 
media = (n1 + n2 + n3)/3

#Tem media maior que 7.0?
if (media >= 7.0):
    print("Passou por média. Nota final: ", media)
else:
    print("Infelizmente não atingiu a média. Nota final: ", media)
    

#Dica: Como limitar as casas decimais impressas ?
#Utilize o %.2f para duas casas decimais
#Ex:
    
num = 8.123456789

print("Num = ", num)
print("1 casa = %.1f" % num)
print("2 casas = %.2f" % num)
print("3 casas = %.3f" % num)
print("E assim por diante")

    
    
    
    




