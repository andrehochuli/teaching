#Peça o login e senha de uma pessoa e informe se o login é valido.

user = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

#Uso o and pois ambos precisam ser verdadeiros. Caso um seja falso, não executa
#Lembrete: letras maisculas e minusculas são diferentes em programação
if (user == 'carlos.silva@edu.br' and senha == '#a1B1c1@'):
    print("Login Efetuado")
else:
    print("Login Não Realizado. Usuário ou senha incorretos")
