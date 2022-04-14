#A partir de três notas de um aluno e informe o conceito a partir da média:
#Média de aproveitamento                  Conceito
#Entre 9.0 e 10.0                              A
#Entre 7.5 e 9.0                               B
#Entre 6.0 e 7.5                               C
#Entre 4.0 e 6.0                               D
#Entre 4.0 e zero                              E


n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))

media = (n1+n2+n3)/3


if media >= 9.0:
    conceito = 'A'
elif media >= 7.5:
    conceito = 'B'
elif media >= 6.0:
    conceito = 'C'
elif media >= 4.0:
    conceito = 'D'
else:    
    conceito = 'E'


if media > 6.0:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

print("Voce obteve o conceito %c e esta %s" % (conceito, situacao))
