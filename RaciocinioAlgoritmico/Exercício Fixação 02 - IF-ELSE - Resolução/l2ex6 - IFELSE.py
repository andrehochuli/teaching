#Informe se um ano é bissexto ou não.
#Anos bissextos são aqueles que são múltiplos de 4, como 1996, 2000, 2004 etc (que podem ser divididos por 4 deixando resto 0).
#Porém, há uma exceção: múltiplos de 100 que não sejam múltiplos de 400.

#Uma das duas condições a seguir deve ser verdadeira:
#Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
#Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)


ano = int(input('Digite o Ano para verificação bissexto: '))

#Lembrando '%' é o modulo da divisão inteira
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('Ano é Bissexto')
else:
    print('Ano não é bissexto')

