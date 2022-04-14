#Verifique entre duas pessoas quem tem o maior nome e a mais velha. 
#DICA1: use a função len() para calcular o tamanho de um nome)
#DICA2: Atente-se ao que foi solicitado, informa a pessoa mais velha, nao a idade

nome1 = input("Digite um nome: ")
idade1 = int(input("Digite uma idade: "))

nome2 = input("Digite outro nome: ")
idade2 = int(input("Digite outra idade: "))

#Utilizo a funcao len() para saber quantos caracteres tem a string (comprimento)
#Ex: len("Bom dia"), tem 7 caracteres. O espaço em branco é um caractere!

tam1 = len(nome1)
tam2 = len(nome2)

#Uma outra forma de formatar o print, é informar uma string com os tipos a serem impressos
print("O %s tem %d caracteres e %d anos" % (nome1,tam1,idade1))
print("O %s tem %d caracteres e %d anos" % (nome2,tam2,idade2))

#Informo quem tem o maior nome
if (tam1 > tam2):
    print("Logo, %s é maior que %s " % (nome1,nome2))        
else:
    print("Logo, %s é maior que %s " % (nome2,nome1))        
    
#Informo que é o mais velho          
if( idade1 > idade2):
    print("E, %s é mais velho que %s" % (nome1,nome2))
else:
    print("E, %s é mais velho que %s" % (nome2,nome1))

    
    
    
    




