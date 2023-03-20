import random as rd

### EJERCICIO 1 ### listo
def T(m,n):
    if (m==0 or n==0):
        return 1
    else: 
        return T(m,n-1) + T(m-1,n)
        

# num1 = rd.randint(0,4)
# num2 = rd.randint(0,4)

num1 = 2
num2 = 1

run = T(num1,num2)
print(f"({num1}, {num2})")
print(run)


### EJERCICIO 2.a ### listo
def secuencia_cuadratica(n):#2
    if n==0:
        return 0.8
    else:
        return secuencia_cuadratica(n-1)**(2)
    
#print(secuencia_cuadratica(4))


### EJERCICIO 2.b### 
def secuencia_cubica(n):
    if n==0:
        return 0.8
    else:
        return (secuencia_cubica(n-1)**3)-0.5 

#print(secuencia_cubica(3))