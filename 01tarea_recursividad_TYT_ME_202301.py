### Tarea 01. recursividad. Semana 03 ###

### 1.a Generar los números de 1 a n 

def gen_n(num):
    #vector = []
    if num == 1:
        print(num)
        #return num
    else:
        gen_n(num-1)
        print(num)
        #return num
        
#y = gen_n(-1)
#print(y)
    
## Final. Listo ##  
def list_number(end, start=1):
    if start > end:
        return []
    elif start >= 1:
        return [start] + list_number(end, start+1)
    



### 1.b Sumatoria recursiva de 1 hasta n enteros positivos

def recursive_sum(num):
    if type(num) == float:
        return None
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    elif num > 1:
        return num + recursive_sum(num-1)
    else:
        return None 

n = 5
y = recursive_sum(n)
print(y)




### 2. Calcular potencia positiva entera de un número real mediante un método recursivo ###

def exponentiation(base, exp):
    if exp == 0:
        return 1
    elif base == 0 and exp == 0:
        return None
    elif exp == 1:
        return base
    else:
        return base * exponentiation(base, exp-1)
    
# base = -2
# exp = 5
# y = exponentiation(base, exp)
# print(y)


### 3. Generar un termino cualquiera del Triangulo de Pacal

def pascal_triangle(m,n):
    if (m==0 or n==0):
        return 1
    else: 
        return pascal_triangle(m,n-1) + pascal_triangle(m-1,n)


### 4. convertir de Decimal A Binario
def decimal_to_binary(num):
    
    if num <2:
        return num
    else:
        integer_part = num%2 + (decimal_to_binary(num//2) * 10)
        float_part = None
        return integer_part

# num = 7
# y = decimal_to_binary(num)
# print(y)