def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag para otimização: Se nenhum elemento for trocado, o vetor já está ordenado
        troca = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Troca os elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                troca = True
        # Se não houve trocas, o vetor já está ordenado
        if not troca:
            break
    return arr
    
    
arr = [23,-2,30,-20]
 
arr = bubble_sort(arr)
print(arr)
