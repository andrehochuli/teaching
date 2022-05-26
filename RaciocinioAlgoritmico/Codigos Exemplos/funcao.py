#funcao que dobra o valor de x
def f(x):

    y = 2*x    

    return y

#maximo entre dois elementos
def m_max(a,b):
    if a > b:
      return a
    else:
      return b   

x = 10
y = f(x)
print(y) #20

x = 30 
y = f(x)
print(y) #60

y = m_max(120,150)
print(y) #150




    
