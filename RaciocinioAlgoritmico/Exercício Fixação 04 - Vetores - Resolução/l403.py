#3. Adicione os primeiros 40 elementos de Fibonacci em um vetor
fibo = [0,1]

#40 element fibonacci
for i in range(2,40):
    fibo.append(fibo[i-1] + fibo[i-2])

print(fibo)

