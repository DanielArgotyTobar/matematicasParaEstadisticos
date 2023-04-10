# import matplotlib.pyplot as plt

# # Datos de ejemplo
# x = [1, 2, 3, 4, 5]
# y = [15, 25, 35, 45, 55]

# # Graficar los datos
# plt.plot(x, y)

# # Definir los valores y etiquetas del eje x
# valores_x = range(1, len(x) + 1)
# etiquetas_x = [str(i) for i in valores_x]

# # Establecer los valores y etiquetas del eje x
# plt.xticks(valores_x, etiquetas_x)

# # Mostrar el gráfico
# #plt.show()


# import matplotlib.pyplot as plt

# # Datos de ejemplo
# x = [1, 2, 3, 4, 5]
# y = [10, 15, 13, 17, 20]

# # Graficar los datos
# plt.plot(x, y)

# # Dibujar las líneas paralelas
# plt.axhline(y=12, color='grey', linestyle='--')
# plt.axhline(y=18, color='grey', linestyle='--')

# # Mostrar el gráfico
# plt.show()

# import matplotlib.pyplot as plt

# # Datos de ejemplo
# x = [1, 2, 3, 4, 5]
# y = [10, 15, 13, 17, 20]

# # Graficar los datos
# plt.plot(x, y)

# # Dibujar las líneas paralelas para cada valor de y
# for y_val in y:
#     plt.axhline(y=y_val, color='grey', linestyle='--')

# # Mostrar el gráfico
# plt.show()



# import matplotlib.pyplot as plt

# # Datos de ejemplo
# x = [1, 2, 3, 4, 5]
# y = [0.2, 0.5, 0.8, 0.3, 0.7]

# # Graficar los datos
# plt.plot(x, y)

# # Dibujar las líneas paralelas para cada valor de y entre 0 y 1
# for y_val in [i/10 for i in range(11)]:
#     plt.axhline(y=y_val, color='grey', linestyle='--')

# # Mostrar el gráfico
# plt.show()
# import matplotlib.pyplot as plt

# # Datos de ejemplo
# x = [1, 2, 3, 4, 5]
# y = [10, 15, 13, 17, 20]

# # Graficar un scatter plot de los datos
# plt.scatter(x, y)

# # Poner nombre a los ejes
# plt.xlabel('Eje x')
# plt.ylabel('Eje y')

# # Mostrar el gráfico
# plt.show()


import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

# Graficar un connected scatter plot de los datos
plt.plot(x, y, '-o')

# Poner nombre a los ejes
plt.xlabel('Eje x')
plt.ylabel('Eje y')

# Mostrar el gráfico
plt.show()