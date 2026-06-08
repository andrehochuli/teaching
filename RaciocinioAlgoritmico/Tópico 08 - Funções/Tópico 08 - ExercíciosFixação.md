```python
# ============================================================
# Tópico 05 - Exercícios de Fixação - Funções
# ============================================================


# 1.1 Maior elemento de um vetor
def max_(vetor):
    maior = vetor[0]

    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]

    return maior


# 1.2 Menor elemento de um vetor
def min_(vetor):
    menor = vetor[0]

    for i in range(1, len(vetor)):
        if vetor[i] < menor:
            menor = vetor[i]

    return menor


# 1.3 Inverte um vetor
def invert_(vetor):
    invertido = []

    for i in range(len(vetor) - 1, -1, -1):
        invertido.append(vetor[i])

    return invertido


# 1.4 Converte todos os caracteres para minúsculo
def lower_(texto):
    resultado = ""

    for c in texto:
        codigo = ord(c)

        if codigo >= ord('A') and codigo <= ord('Z'):
            resultado += chr(codigo + 32)
        else:
            resultado += c

    return resultado


# 1.5 Converte todos os caracteres para maiúsculo
def upper_(texto):
    resultado = ""

    for c in texto:
        codigo = ord(c)

        if codigo >= ord('a') and codigo <= ord('z'):
            resultado += chr(codigo - 32)
        else:
            resultado += c

    return resultado


# 1.6 Verifica se é um dígito
def isdigit_(c):
    return c >= '0' and c <= '9'


# 1.7 Verifica se é um caractere alfabético
def ischar_(c):
    return (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z')


# 1.8 Ordena um vetor
def sort_(vetor):
    ordenado = vetor.copy()

    for i in range(len(ordenado)):
        for j in range(0, len(ordenado) - 1 - i):
            if ordenado[j] > ordenado[j + 1]:
                aux = ordenado[j]
                ordenado[j] = ordenado[j + 1]
                ordenado[j + 1] = aux

    return ordenado


# 1.9 Verifica se um valor existe no vetor
def exist_(vetor, valor):
    for elemento in vetor:
        if elemento == valor:
            return True

    return False


# 1.10 Retorna a média e o desvio padrão
def dev_padrao(vetor):
    soma = 0

    for valor in vetor:
        soma += valor

    media = soma / len(vetor)

    soma_diferencas = 0

    for valor in vetor:
        soma_diferencas += (valor - media) ** 2

    variancia = soma_diferencas / len(vetor)
    desvio = variancia ** 0.5

    return media, desvio


# 1.11 Concatena dois vetores
def concatena_(vetor1, vetor2):
    resultado = []

    for valor in vetor1:
        resultado.append(valor)

    for valor in vetor2:
        resultado.append(valor)

    return resultado


# ============================================================
# 2. Retorna os índices que possuem números pares
# ============================================================

def indices_pares(vetor):
    indices = []

    for i in range(len(vetor)):
        if vetor[i] % 2 == 0:
            indices.append(i)

    return indices


# Exemplo:
# [10, 11, 12, 13, 14] -> [0, 2, 4]


# ============================================================
# 3. Retorna a frequência dos elementos
# ============================================================

def frequencia(vetor):
    resultado = []

    for i in range(len(vetor)):
        valor = vetor[i]
        ja_contado = False

        for j in range(len(resultado)):
            if resultado[j][0] == valor:
                ja_contado = True

        if not ja_contado:
            cont = 0

            for k in range(len(vetor)):
                if vetor[k] == valor:
                    cont += 1

            resultado.append([valor, cont])

    return resultado


# Exemplo:
# [1,2,1,3,3,4,3,1,2,1,1]
# -> [[1,5], [2,2], [3,3], [4,1]]


# ============================================================
# 4. Validação de CPF
# ============================================================

def valida_cpf(cpf):
    # Remove caracteres que não são dígitos
    apenas_digitos = ""

    for c in cpf:
        if isdigit_(c):
            apenas_digitos += c

    cpf = apenas_digitos

    # CPF precisa ter 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais
    todos_iguais = True

    for i in range(1, len(cpf)):
        if cpf[i] != cpf[0]:
            todos_iguais = False

    if todos_iguais:
        return False

    # Cálculo do primeiro dígito verificador
    soma = 0
    peso = 10

    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    if digito1 != int(cpf[9]):
        return False

    # Cálculo do segundo dígito verificador
    soma = 0
    peso = 11

    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    if digito2 != int(cpf[10]):
        return False

    return True
```
