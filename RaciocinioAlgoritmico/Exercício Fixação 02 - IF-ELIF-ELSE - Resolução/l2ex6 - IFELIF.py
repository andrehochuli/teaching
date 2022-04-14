#Sistema de recomendação de compra de carros


resp1 = input("Voce deseja um carro para trabalho (s/n) ?")

resp2 = input("Precisa de motor forte (s/n) ?")

resp3 = input("Sua familia é maior que 3 pessoas ?")

resp4 = input("Sua distância diaria é maior que 20km ?")


if (resp1 == 's') and (resp2 == 'n'):
    print("Um veiculo popular hatch com motor 1.0 pode ser interessante")


elif ((resp1 == 's') and (resp2 == 's')) or (resp3 == 's'):
    print("Uma suv como motor acima de 1.6 é uma opção interessante.")

elif ((resp1 == 'n') and (resp2 == 'n') and (resp3 == 'n')):
    print("Uma sedan acima de 1.4 é uma opção interessante.")

else:
    print("Baseado nas suas escolhas não consigo identificar uma opção adequada. Peça ajuda a um especialista!")

#OBS: Aqui procuro avaliar uma expressão lógica para direcionar o melhor veiculo.
#Crie expressões lógicas e clasúlas elif para criar condições de seleção mais adequadas.










