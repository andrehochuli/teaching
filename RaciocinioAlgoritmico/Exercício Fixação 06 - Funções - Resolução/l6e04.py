'''4. Validar um CPF'''
#para efeito didatico, nao consideramos os pontos e tracos
    #Ex: 987.654.321-00 -> 98765432100

#CPF VALIDO: https://www.macoratti.net/alg_cpf.htm
 
def valida_primeiro_digito(cpf):

    soma = 0
    #Calculo a regra para os digitos das posicoes 1-9 do cpf
    for i in range(10,1,-1):
        
        num = int(cpf[10-i])
        
        soma += num * i

    rest = soma % 11
    
    #Defino o digito a partir do resto da divisao
    if rest < 2:
        dig = 0
    else:
        dig = 11 - rest

    #valida o digito    
    if int(cpf[9]) == dig:
        return True
    else:
        return False

def valida_segundo_digito(cpf):

    soma = 0
    #Calculo a regra para os digitos das posicoes 1-10 do cpf
    for i in range(11,1,-1):
        
        num = int(cpf[11-i])
        
        soma += num * i

    rest = soma % 11
    
    #Defino o digito a partir do resto da divisao
    if rest < 2:
        dig = 0
    else:
        dig = 11 - rest

    #valida o digito    
    if int(cpf[10]) == dig:
        return True
    else:
        return False



cpf = input("Digite seu CPF: ")

if len(cpf) != 11:
    print("[ERRO] CPF Invalido. Nao tem 11 digitos")

else:
    ret1 = valida_primeiro_digito(cpf)
    ret2 = valida_segundo_digito(cpf)

    if ret1 == False or ret2 == False:
        print("[ERRO] CPF INVALIDO")
    else:
        print("[OK] CPF VALIDO")

#Dica, voce pode melhorar este codigo para apenas uma funcao
#Pense no primeiro e segundo digito como parametro
#Veja que as funções mudam muito pouco :)
