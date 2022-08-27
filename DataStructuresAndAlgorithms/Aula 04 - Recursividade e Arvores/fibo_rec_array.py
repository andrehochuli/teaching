def fibo(n):

    if n == 1:
        return [0]

    if n == 2:
        arr = fibo(n-1) + [1]
        return arr
    
    arr = fibo(n-1)
    arr += [sum(arr[-2:])]

    return arr

#Pos:  1 2 3 4 5 6 7 8  9  
#Elem: 0 1 1 2 3 5 8 13 21

print(fibo(7))

