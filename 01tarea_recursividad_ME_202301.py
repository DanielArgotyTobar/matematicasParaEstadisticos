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

# Ejemplo de uso
# num = 100
# y = gen_n(num)
# print(y)

## Final. Listo ##
def list_number(end, start=1):
    if start > end:
        return []
    elif start >= 1:
        return [start] + list_number(end, start+1)

# Ejemplo de uso
# num = 20;
# y = list_number(num, start=1);
# print(y)


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

# Ejemplo de uso
#n = 5
#y = recursive_sum(n)
#print(y)




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

# Ejemplo de uso
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

# Ejemplo de uso
# m = 1;
# n = 5;
# y = pascal_triangle(m,n)
# print(y);





### 4. convertir de Decimal A Binario

def num_to_vector(num):
    vector_num = []
    str_num = str(num)
    range_num = len(str_num)
    for number in range(range_num):
        vector_num.append(str_num[number])
    return vector_num

# Ejemplo de uso
# num = 10.5
# y = num_to_vector(num)
# print(y)
# Funcion para pasar numero naturales a numeros binarios

def int_decimal_to_binary(num):
    #print(num)
    if num < 2:
        return num
    else:
        return num%2 + (int_decimal_to_binary(num//2) * 10)
    
# Ejemplo de uso
# num1 = 5
# z = int_decimal_to_binary(num1)
# print(z)
# print("============================================================")

def float_decimal_to_binary(num):  
    parte_entera = int(num)
    parte_decimal2 = num - parte_entera
    
    if num == 0:
        return []
    else:
        return [int(num)] + float_decimal_to_binary(parte_decimal2 * 2)
# Ejemplo de uso
#num = 2.9022
# num = 10.5
# y = float_decimal_to_binary(num)
# print(y)
# y.remove(y[0])
# print("======================")
# print(y)


def list_to_string(lista):
    string = ""
    for i in range(len(lista)):
        string += str(lista[i])
    return string


def decimal_to_binary(num):
    
    # Parte entera del número a binario
    int_part = int(num)
    int_binary = int_decimal_to_binary(int_part)
     
    # Parte decimal del número a binario
    lista_float_binary = float_decimal_to_binary(num)
    lista_float_binary.remove(lista_float_binary[0])
    float_binary = list_to_string(lista_float_binary)
    
    # Resultado final
    if len(float_binary) == 0:
         num_binary = str(int_binary)
    else:
        num_binary = str(int_binary) + "." + float_binary
    
    return num_binary

# Ejemplo de uso
#num = 2.9022
#num = 10
#y = decimal_to_binary(num)
#print(y)





### 5. Binario a decimal

# binario = "1010"
# decimal = int(binario, 2)
# print(decimal)



def int_part_to_decimal(lista1, i = 0):
    if not lista1:
        return []
    else:
        return [lista1[0]*2**(i)] + int_part_binary(lista1[1:], i + 1)

def float_part_to_decimal(lista2, i = -1):
    if not lista2:
        return []
    else:
        return [lista2[0]*2**(i)] + float_part_binary(lista2[1:], i - 1)

def binary_to_decimal(num):
    binario = float(num)
    str_bin = str(binario)
    # Dividir el numero en parte entera y fraccionaria
    parts = str_bin.split('.')
    int_part = parts[0]
    float_part = parts[1]
    # Agregar las partes del numero en listas
    int_digits = []
    float_digits = []
    for int_digit in int_part:
        int_digits.append(int(int_digit))
    for float_digit in float_part:
        float_digits.append(int(float_digit))
    int_digits.reverse()
    # Transformar el numero binario a decimal
    int_binary = int_part_to_decimal(int_digits)
    float_binary = float_part_to_decimal(float_digits)
    decimal_num = sum(int_binary) + sum(float_binary)
    
    return decimal_num

# bin = 10.111001
# y = binary_to_decimal(bin)
# print(y)



### 6. Generar termino de la sucesión T(n)

# Termino enesimo
def T(n):
    if n == 0:
        return 3
    else:
        return 5*n + 2 + T(n-1)
# Ejemplo de uso
# num = 2
# y = T(num)
# print(y)


# Primeros n terminos de la sucesion
def terms_of_succession(n):
    list_terms_of_succession = []
    for term in range(n):
        list_terms_of_succession.append(T(term))
    return list_terms_of_succession
# Ejemplo de uso
# num = 5
# y = terms_of_succession(num)
# print(y)



### 7. Una poblacion se triplica cada año
# Grafico coweb
# https://www.geogebra.org/m/wQejYhpt

def population_triples(years, initial_population):
    if years == 0:
        return initial_population
    else:
        return population_triples(years - 1, initial_population * 3)

# Ejemplo de uso
# year = 2
# poblacion_inicial = 1
# y = population_triples(year, poblacion_inicial)
# print(y)


### 8. Modelo poblacional

def modelo_poblacional_1(n):
    if n == 0:
        return 0.2
    else:
        return (3.7) * modelo_poblacional_1(n-1) * (1 - modelo_poblacional_1(n-1))
# Ejemplo de uso
# n = 2
# y = modelo_poblacional_1(n)
# print(y)

########################################################################
# valores_modelo_poblacional_1 = []
# for i in range(20):
#     valores_modelo_poblacional_1.append(modelo_poblacional_1(i))
# #print(valores_modelo_poblacional_1)
# y_valores = valores_modelo_poblacional_1

# # Grafica modelo poblacional 1 x0 = 0.2
# import matplotlib.pyplot as plt

# # Datos de ejemplo
# x = list_number(20)
# y = valores_modelo_poblacional_1

# # Graficar los datos
# plt.plot(x, y, "-o")

# # Dibujar las líneas paralelas para cada valor de y
# for y_val in [i/10 for i in range(11)]:
#     plt.axhline(y=y_val, color='grey', linestyle='--')
    
# # Poner nombre a los ejes
# plt.xlabel("iteración")
# plt.ylabel("3.7x(1-x)")

# # Poner titulo a la grafica
# plt.title("Modelo poblacional con x0 = 0.2")

# # Definir los valores y etiquetas del eje x
# valores_x = range(1, len(x) + 1)
# etiquetas_x = [str(i) for i in valores_x]

# # Establecer los valores y etiquetas del eje x
# plt.xticks(valores_x, etiquetas_x)

# # Mostrar el gráfico
# plt.show()
########################################################################

def modelo_poblacional_2(n):
    if n == 0:
        return 0.71
    else:
        return (3.7) * modelo_poblacional_2(n-1) * (1 - modelo_poblacional_2(n-1))
# Ejemplo de uso
# n = 2
# y = modelo_poblacional_2(n)
# print(y)

#################################################################
# valores_modelo_poblacional_2 = []
# for i in range(25):
#     valores_modelo_poblacional_2.append(modelo_poblacional_2(i))

# # Grafica modelo poblacional 2 x0 = 0.71
# import matplotlib.pyplot as plt

# # Datos de ejemplo
# x = list_number(25)
# y = valores_modelo_poblacional_2

# # Graficar los datos
# plt.plot(x, y, "-o")

# # Dibujar las líneas paralelas para cada valor de y
# for y_val in [i/10 for i in range(11)]:
#     plt.axhline(y=y_val, color='grey', linestyle='--')
    
# # Poner nombre a los ejes
# plt.xlabel("iteración")
# plt.ylabel("3.7x(1-x)")

# # Poner titulo a la grafica
# plt.title("Modelo poblacional con x0 = 0.71")

# # Definir los valores y etiquetas del eje x
# valores_x = range(1, len(x) + 1)
# etiquetas_x = [str(i) for i in valores_x]

# # Establecer los valores y etiquetas del eje x
# plt.xticks(valores_x, etiquetas_x)

# # Mostrar el gráfico
# plt.show()
####################################################################




#### 10. 
# import math

# def f(x):
#     return math.cos(x) - x

# def df(x):
#     return (math.sin(x)*(-1)) - 1

def newton_raphson(x0, precision, max_iter):
    i = 0
    while i < max_iter:
        fx0 = f(x0)
        dfx0 = df(x0)
        x1 = x0 - fx0 / dfx0
        if abs(x1 - x0) < precision:
            return x1
        x0 = x1
        i += 1
    print("no se hubo convergencia en ", max_iter, "iteraciones.")
    return None

# Ejemplo de uso
# x0 = 3  # Valor inicial
# precision = 0.001  # precision
# max_iter = 100  # Número de iteraciones
# raiz = newton_raphson(x0, presicion, max_iter)

# if raiz is not None:
#     print("La raiz de la funcion es:", raiz)
# else:
#     print("No se encontro una raiz en las iteraciones permitidas.")



### 11. Raiz cuadrada de 3

def f(x):
    return x**(2) - 3

def df(x):
    return 2*x

x0 = 1  # Valor inicial
presicion = 0.00001  # precision
max_iter = 100  # Número de iteraciones
raiz = newton_raphson(x0, presicion, max_iter)

if raiz is not None:
    print("La raiz de la funcion es:", raiz)
else:
    print("No se encontro una raiz en las iteraciones permitidas.")








    
    
    
    