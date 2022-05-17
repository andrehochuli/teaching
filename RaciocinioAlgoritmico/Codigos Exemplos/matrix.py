import random
print("MAT 2x2")
#mat 2x2
mat = [[10,20],
       [30,40]]

for l in range(0,2):        
    for c in range(0,2):        
        print("[%d][%d] = %d" % (l,c,mat[l][c]))

print("MAT 3x2")
#mat 3x2
mat = [[10,20],
       [30,40],
       [50,60]]

for l in range(0,3):       
    for c in range(0,2):    
        print("[%d][%d] = %d" % (l,c,mat[l][c]))

print("Mat 10x10 Aleatoria")
#Criando Mat 10x10
mat = []
for l in range(0,10):
    mat.append([])    
    for c in range(0,10):        
        mat[l].append(random.randint(10,60))




        
    
