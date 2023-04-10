def factorial(n):
    if n == 1: return 1
    else: return n * factorial(n-1)
    
# n = 3
# x = factorial(n)
# print(x) 



def separar_numero(num):
    # Convertir el número a una cadena de caracteres
    num_str = str(num)
    
    # Separar la parte entera de la parte decimal
    entero, decimal = num_str.split(".")
    
    # Convertir la parte entera a un entero y agregarlo a la lista
    entero_list = [int(d) for d in entero]
    
    # Si la parte decimal es vacía, retornar la lista de la parte entera
    if not decimal:
        return entero_list
    
    # Si la parte decimal no es vacía, agregar el punto y continuar con la parte decimal
    decimal_list = [".", *separar_numero(float("0." + decimal))]
    
    # Retornar la concatenación de las dos listas
    return entero_list + decimal_list

# num = 123.456
# lista_num = separar_numero(num)
# print(lista_num)


#num = 10.00515
# num = float(10.00512)

# int_part = int(num)
# float_part = num - int_part
# range_float_part = len(str(num))


# partes = str(num).split('.')
# print(partes)
# decimales = partes[1] if len(partes) > 1 else ""
# print(decimales)
# cantidad_decimales = len(decimales)

# precision = cantidad_decimales
# round_num = f"{float_part:.{precision}}"
# float_part2 = float(round_num)

# sum1 = int_part + float_part
# sum2 = int_part + float_part2

# print(f"Numero: {num}")
# print(f"Parte decimal: {round_num}")
# print(f"Cantidad decimales: {cantidad_decimales}")
# print(f"Numero caracteres: {range_float_part}")
# print(f"Metodo 1: {num} = {int_part} + {float_part} = {sum1}")
# print(f"Metodo 2: {num} = {int_part} + {float_part2} = {sum2}")




def list_number(end, start=1):
    if start > end:
        return []
    elif start >= 1:
        return [start] + list_number(end, start+1)
    
def cantidad_decimales(num):
    num = float(num)
    #int_part = int(num)
    #float_part1 = num - int_part
    
    partes = str(num).split('.')
    decimales = partes[1] if len(partes) > 1 else ""
    cantidad_decimales = len(decimales)
    
    return cantidad_decimales
# Ejemplo de uso
# num = 123540.0214
# y = cantidad_decimales(num)
# print(y)

def float_part_precision(num):
    # # Separar el numero en parte entera y decimal
    num = float(num)
    int_part = int(num)
    float_part1 = num - int_part

    # Guardar la parte decimal en una lista
    partes = str(num).split('.')
    decimales = partes[1] if len(partes) > 1 else ""
    cantidad_decimales = len(decimales) # contar el numero de decimales
    
    # Redondear el numero decimales interpretados por el computador
    # al numero de decimales usados
    precision = cantidad_decimales
    round_num = f"{float_part1:.{precision}}"
    float_part2 = float(round_num)
    return float_part2
# Ejemplo de uso
# num = 1235410.00012000543
# y = float_part(num)
# print(y)






################## 5. Decimal a binario #################################################################
binario = "1010.0"
partes = binario.split('.')
parte_entera = partes[0]
print(f"parte entera: {type(parte_entera)}")
parte_fraccionaria = partes[1]
print(f"parte fraccionaria: {parte_fraccionaria}")

decimal_entero = int(parte_entera, 2)
decimal_fraccionario = 0

for i in range(len(parte_fraccionaria)):
    decimal_fraccionario += int(parte_fraccionaria[i]) * pow(2, -(i+1))

decimal = decimal_entero + decimal_fraccionario
print(type(decimal))
print(decimal)



# def has_fraccion(str_num):
#    if "." in str_num:
#        return True
#    else:
#        return False
       
    
# bin = 10.0
# str_bin = str(bin)
# print(f"numero: {str_bin}")

# if has_fraccion(str_bin) is True:
    # partes = str_bin.split('.')
    # parte_entera = partes[0]
    # print(f"parte entera: {parte_entera}")
    # #print(f"parte entera: {type(parte_entera)}")
    # parte_fraccionaria = partes[1]
    # print(f"parte fraccionaria: {parte_fraccionaria}")
    # #print(f"parte entera: {type(parte_fraccionaria)}")
    
    # digitos_enteros = []
    # digitos_fraccion = []
    # for digito1 in parte_entera:
    #     digitos_enteros.append(int(digito1))
    # for digito2 in parte_fraccionaria:
    #     digitos_fraccion.append(int(digito2))
    
    digitos_enteros.reverse()

    print(f"lista parte entera: {digitos_enteros}")
    print(f"lista parte fraccionaria: {digitos_fraccion}") 
    

# def int_part_binary(lista1, i = 0):
#     if not lista1:
#         return []
#     else:
#         return [lista1[0]*2**(i)] + int_part_binary(lista1[1:], i + 1)
# y1 = int_part_binary(digitos_enteros)
# print(f"Lista binario entero: {y1}")
# print(f"Entero binario: {sum(y1)}")

# def float_part_binary(lista2, i = -1):
#     if not lista2:
#         return []
#     else:
#         return [lista2[0]*2**(i)] + float_part_binary(lista2[1:], i - 1)
# # Ejemplo de uso
# y2 = float_part_binary(digitos_fraccion)
# print(f"Lista binario fraccion: {y2}")
# print(f"fraccion binario: {sum(y2)}")
# print(f"Numero decimal: {sum(y1)+sum(y2)}")


# # libraries
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# # data
# df = pd.DataFrame({
#     'x_axis': range(1,20),
#     'y_axis': valores_modelo_poblacional_1
# })

# # plot
# plt.plot('x_axis', 'y_axis', data=df, linestyle='-', marker='o')
# plt.show()
